from django.core.management.base import BaseCommand

from report.main_bot import updater


class Command(BaseCommand):
    help = 'Telegram-бот'

    def handle(self, *args, **options):
        updater.start_polling()
        updater.idle()
