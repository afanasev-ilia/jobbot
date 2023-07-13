from telegram import Bot
import asyncio

# Здесь укажите токен,
# который вы получили от @Botfather при создании бот-аккаунта
bot = Bot(token='****')
# Укажите id своего аккаунта в Telegram
chat_id = 718703260
text = 'Вам телеграмма!'
# Отправка сообщения


async def main():
    await bot.send_message(chat_id, text)


if __name__ == '__main__':
    asyncio.run(main())
