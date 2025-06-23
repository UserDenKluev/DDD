from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

# === Настройки ===
BOT_TOKEN = '7286373398:AAHur3oLwZ5KkvJcS_L73fYgZvfxt1vA0kI'  # Замените на ваш токен
GROUP_CHAT_ID = 5603212222  # ID целевой группы (всегда отрицательное число)

# === Обработчик входящих сообщений ===
async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message

    if user_message:
        try:
            # Отправляем сообщение в группу
            await context.bot.forward_message(
                chat_id=GROUP_CHAT_ID,
                from_chat_id=user_message.chat_id,
                message_id=user_message.message_id
            )
            # Опционально: подтверждение пользователю
            if update.message:
                await update.message.reply_text("Сообщение отправлено в группу!")
        except Exception as e:
            print(f"Ошибка при пересылке: {e}")
            if update.message:
                await update.message.reply_text(f"Ошибка: {e}")

# === Основная функция запуска бота ===
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Ловим все текстовые и медиа сообщения
    app.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, forward_message))

    print("Бот запущен...")
    app.run_polling()

# === Запуск ===
if __name__ == '__main__':
    main()