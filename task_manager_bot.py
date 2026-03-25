import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv  # Добавь эту строку!

# 1. Загружаем данные из файла .env
load_dotenv()

# 2. вызываем функцию
TOKEN = os.getenv("BOT_TOKEN")

# Включаем логирование, чтобы видеть ошибки в консоли
logging.basicConfig(level=logging.INFO)

# Объект бота и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Список для хранения задач (в оперативной памяти)
tasks = []

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет! Я твой менеджер задач. \nПросто напиши мне текст задачи, и я её запомню. \nКоманды: /tasks - список, /clear - очистить.")

# Хэндлер на команду /tasks (показать всё)
@dp.message(Command("tasks"))
async def show_tasks(message: types.Message):
    if not tasks:
        await message.answer("Твой список задач пока пуст!")
    else:
        response = "📌 Твои задачи:\n" + "\n".join([f"{i+1}. {task}" for i, task in enumerate(tasks)])
        await message.answer(response)

# Хэндлер на команду /clear
@dp.message(Command("clear"))
async def clear_tasks(message: types.Message):
    tasks.clear()
    await message.answer("Список задач очищен! 🧹")

# Хэндлер для любого текстового сообщения (добавление задачи)
@dp.message()
async def add_task(message: types.Message):
    if message.text:
        tasks.append(message.text)
        await message.answer(f"✅ Добавил в список: {message.text}")

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

    

