from django.core.management.base import BaseCommand
from django.conf import settings

from telegram import ReplyKeyboardMarkup, Update
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
        [['/work_report'], ['/after_work_report']], resize_keyboard=True
    )
    await context.bot.send_message(
        chat_id=chat.id,
        text='Здравствуйте! Пожалуйста, выберите тип отчета',
        reply_markup=button,
    )


async def work_report(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text('Введите номер счета что бы продолжить')
    return ORDER


async def order_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data[ORDER] = update.message.text
    await update.message.reply_text('Введите порядковый номер позиции из счета')
    return ITEM_ORDER


async def item_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data[ITEM_ORDER] = update.message.text
    await update.message.reply_text('Укажите время выполнения в минутах')
    return EXECUTION_TIME


async def time_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data[EXECUTION_TIME] = update.message.text
    await update.message.reply_text('Приложите фотографию')
    return IMAGE


async def image_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    print(context.user_data)


async def cancel_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
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
    help = "Telegram-бот"

    def handle(self, *args, **options):
        application = (
            Application.builder().token(token=settings.TELEGRAM_TOKEN).build()
        )

        conv_handler = ConversationHandler(
            entry_points=[CommandHandler("start", start)],
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

        application.add_handler(conv_handler)

        application.run_polling(allowed_updates=Update.ALL_TYPES)

        # updater.dispatcher.add_handler(CommandHandler('start', wake_up))
        # updater.dispatcher.add_handler(report_handler)
        # updater.dispatcher.add_handler(
        #     CommandHandler('after_work_report', after_work_report)
        # )

        # updater.start_polling()
        # updater.idle()
