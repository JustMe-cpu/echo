import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from config import TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Привет!")

@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer("Доступные команды:\n/start - приветствие\n/help - список команд")

@dp.message()
async def echo_message(message: Message):
    await message.answer(f"Ты написал:{message.text}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
