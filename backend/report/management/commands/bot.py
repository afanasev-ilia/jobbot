from django.core.management.base import BaseCommand
from django.conf import settings

from telegram.ext import CommandHandler, Updater
from telegram import ReplyKeyboardMarkup

from report.models import Employee


def work_report(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text='Отчет о работе')


def after_work_report(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text='Отчет в конце дня')


def wake_up(update, context):
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
        updater.dispatcher.add_handler(CommandHandler('start', wake_up))
        updater.dispatcher.add_handler(
            CommandHandler('work_report', work_report),
        )
        updater.dispatcher.add_handler(
            CommandHandler('after_work_report', after_work_report)
        )
        updater.start_polling()
        updater.idle()
