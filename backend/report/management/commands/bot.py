from django.core.management.base import BaseCommand
from django.conf import settings

from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import (
    CommandHandler,
    ConversationHandler,
    ContextTypes,
    Filters,
    MessageHandler,
    Updater,
)


from report.models import Employee


ORDER, ITEM_ORDER, EXECUTION_TIME, IMAGE = range(4)


def work_report(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    update.message.reply_text('Введите номер счета что бы продолжить')
    return ORDER


def order_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data[ORDER] = update.message.text
    update.message.reply_text('Введите порядковый номер позиции из счета')
    return ITEM_ORDER


def item_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data[ITEM_ORDER] = update.message.text
    update.message.reply_text('Укажите время выполнения в минутах')
    return EXECUTION_TIME


def time_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data[EXECUTION_TIME] = update.message.text
    update.message.reply_text('Приложите фотографию')
    return IMAGE


def image_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    print(context.user_data)


def cancel_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    update.message.reply_text('Отчет не отправлен')
    return ConversationHandler.END


def after_work_report(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE,
) -> int:
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id,
        text='Отчет об уборке рабочего места',
    )


def wake_up(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    chat = update.effective_chat
    Employee.objects.get_or_create(external_id=chat.id)
    button = ReplyKeyboardMarkup(
        [['/work_report'], ['/after_work_report']], resize_keyboard=True
    )
    context.bot.send_message(
        chat_id=chat.id,
        text='Здравствуйте! Пожалуйста, выберите тип отчета',
        reply_markup=button,
    )


class Command(BaseCommand):
    help = 'Telegram-бот'

    def handle(self, *args, **options):
        updater = Updater(token=settings.TELEGRAM_TOKEN)

        report_handler = ConversationHandler(
            entry_points=[
                CommandHandler('work_report', work_report),
            ],
            states={
                ORDER: [
                    MessageHandler(
                        Filters.all,
                        order_handler,
                        pass_user_data=True,
                    ),
                ],
                ITEM_ORDER: [
                    MessageHandler(
                        Filters.all,
                        item_handler,
                        pass_user_data=True,
                    ),
                ],
                EXECUTION_TIME: [
                    MessageHandler(
                        Filters.all,
                        time_handler,
                        pass_user_data=True,
                    ),
                ],
                IMAGE: [
                    MessageHandler(
                        Filters.all,
                        image_handler,
                        pass_user_data=True,
                    ),
                ],
            },
            fallbacks=[
                CommandHandler('cancel', cancel_handler),
            ],
        )

        updater.dispatcher.add_handler(CommandHandler('start', wake_up))
        updater.dispatcher.add_handler(report_handler)
        updater.dispatcher.add_handler(
            CommandHandler('after_work_report', after_work_report)
        )

        updater.start_polling()
        updater.idle()
