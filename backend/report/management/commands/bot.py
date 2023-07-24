from django.core.management.base import BaseCommand
from django.conf import settings

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)


from report.models import Employee


ORDER, ITEM_ORDER, EXECUTION_TIME, IMAGE = range(4)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    chat = update.effective_chat
    Employee.objects.get_or_create(external_id=chat.id)
    button = ReplyKeyboardMarkup(
        [['Отчет о проделанной работе'], ['Отчет об уборке рабочего места']],
        resize_keyboard=True,
    )
    await context.bot.send_message(
        chat_id=chat.id,
        text='Здравствуйте! Пожалуйста, выберите тип отчета',
        reply_markup=button,
    )


async def work_report(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE,
) -> int:
    await update.message.reply_text(
        'Введите номер счета что бы продолжить',
        reply_markup=ReplyKeyboardRemove(),
    )
    return ORDER


async def order_handler(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
) -> int:
    context.user_data[ORDER] = update.message.text
    await update.message.reply_text(
        'Введите порядковый номер позиции из счета',
    )
    return ITEM_ORDER


async def item_handler(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
) -> int:
    context.user_data[ITEM_ORDER] = update.message.text
    await update.message.reply_text('Укажите время выполнения в минутах')
    return EXECUTION_TIME


async def time_handler(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
) -> int:
    context.user_data[EXECUTION_TIME] = update.message.text
    await update.message.reply_text('Приложите фотографию')
    return IMAGE


async def image_handler(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
) -> int:
    await update.message.reply_text('Спасибо! Отчет отправлен!')
    print(context.user_data)
    return ConversationHandler.END


async def cancel_handler(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
) -> int:
    await update.message.reply_text('Отчет не отправлен')
    return ConversationHandler.END


async def after_work_report(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE,
) -> int:
    chat = update.effective_chat
    await context.bot.send_message(
        chat_id=chat.id,
        text='Отчет об уборке рабочего места',
    )


class Command(BaseCommand):
    help = 'Telegram-бот'

    def handle(self, *args, **options):
        application = (
            Application.builder().token(token=settings.TELEGRAM_TOKEN).build()
        )

        report_handler = ConversationHandler(
            entry_points=[
                MessageHandler(
                    filters.Text('Отчет о проделанной работе'),
                    work_report,
                ),
            ],
            states={
                ORDER: [
                    MessageHandler(
                        filters.ALL,
                        order_handler,
                    ),
                ],
                ITEM_ORDER: [
                    MessageHandler(
                        filters.ALL,
                        item_handler,
                    ),
                ],
                EXECUTION_TIME: [
                    MessageHandler(
                        filters.ALL,
                        time_handler,
                    ),
                ],
                IMAGE: [
                    MessageHandler(
                        filters.ALL,
                        image_handler,
                    ),
                ],
            },
            fallbacks=[
                CommandHandler('cancel', cancel_handler),
            ],
        )

        application.add_handler(CommandHandler('start', start))
        application.add_handler(report_handler)
        application.add_handler(
            MessageHandler(
                filters.Text('Отчет об уборке рабочего места'),
                after_work_report,
            ),
         )
        application.run_polling(allowed_updates=Update.ALL_TYPES)
