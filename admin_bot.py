# admin_bot.py — (можно не запускать, достаточно просто читать сообщения в этом боте)
# Но если хочешь логировать или добавить функции — вот база:

import asyncio
from telegram.ext import Application, MessageHandler, filters, ContextTypes

BOT_ADMIN_TOKEN = "8502932521:AAHzcEhethHY7fuKNTIKhZCJSdVAO97Hkf8"

async def handle_incoming(update: ContextTypes.DEFAULT_TYPE, context):
    # Это сообщения от user_bot.py
    # Ты можешь просто читать их в интерфейсе Telegram — обработка не обязательна
    pass

def main():
    app = Application.builder().token(BOT_ADMIN_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT, handle_incoming))
    app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())