from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import os

# === Настройки ===
BOT_TOKEN = '7992500011:AAGSfiGHolxiSYlZJocjOOfdXb4wwSFLWec'  # Замените на ваш токен
GROUP_CHAT_ID = 5603212222  # ID целевой группы (всегда отрицательное число)

# === Обработчик входящих сообщений ===
async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message

    if user_message:
        try:
            await context.bot.forward_message(
                chat_id=GROUP_CHAT_ID,
                from_chat_id=user_message.chat_id,
                message_id=user_message.message_id
            )
            if update.message:
                await update.message.reply_text("Сообщение отправлено в группу!")
        except Exception as e:
            print(f"Ошибка при пересылке: {e}")
            if update.message:
                await update.message.reply_text(f"Ошибка: {e}")

# === Основная функция запуска бота ===
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, forward_message))

    print("Бот запущен через webhook...")

    # Получаем порт из переменной окружения Render
    port = int(os.environ.get("PORT", 8443))
    # URL, по которому Telegram будет отправлять обновления (замените на ваш Render-домен)
    webhook_path = f"/{BOT_TOKEN}"
    webhook_url = f"https://ddd-h0w2.onrender.com{webhook_path}"

    app.run_webhook(
        listen="0.0.0.0",
        port=port,
        webhook_url=webhook_url
    )

if __name__ == '__main__':
    main()