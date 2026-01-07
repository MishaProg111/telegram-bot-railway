# user_bot.py
import asyncio
import telegram
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Токены
BOT_USER_TOKEN = "8539362103:AAG26IpsNQRUPhCGGdyOPk5HpsduaqdtaDQ"
BOT_ADMIN_TOKEN = "8502932521:AAHzcEhethHY7fuKNTIKhZCJSdVAO97Hkf8"
YOUR_TELEGRAM_ID = 8181435720  # Замени на свой ID

admin_bot = telegram.Bot(token=BOT_ADMIN_TOKEN)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Это бот для связи с @userradarov. "
        "Если у тебя есть спам-блок — просто напиши сюда своё сообщение, "
        "и оно обязательно дойдёт до меня. Я отвечу в ближайшее время!"
    )

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    message_text = update.message.text

    # Формируем сообщение для тебя
    formatted_msg = (
        f"📩 Новое сообщение от пользователя @{user.username or user.id}\n\n"
        f"«{message_text}»"
    )

    try:
        await admin_bot.send_message(chat_id=YOUR_TELEGRAM_ID, text=formatted_msg)
        await update.message.reply_text("✅ Сообщение отправлено! Спасибо, я скоро отвечу.")
    except Exception as e:
        await update.message.reply_text("❌ Произошла ошибка при отправке. Попробуй позже.")
        print(f"Ошибка отправки: {e}")

def main():
    app = Application.builder().token(BOT_USER_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_message))
    app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())