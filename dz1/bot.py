import asyncio
import logging
import random

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from config import TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher()
@dp.message(CommandStart())
async def start_bot(message: Message):
    await message.reply("добрый день вас приветствует игра угадай число ")
@dp.message(Command("help"))
async def help(message: Message):
    await message.reply("бог поможет")
@dp.message(F.text == "Как дела?")
async def how_are_you(message: Message):
    await message.reply("Хорошо, спасибо!")
@dp.message(F.text.in_({'Привет', 'привет', 'салам'}))
async def greeting(message: Message):
    await message.answer("Привет!")
@dp.message(F.text.in_({'1', '2', '3'}))
async def guess_number(message: Message):
    user_guess = int(message.text)
    random_number = random.randint(1, 3)
    if user_guess == random_number:
        await message.answer_photo(
            photo="https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg",
            caption="Правильно, вы угадали!")
    else:
        await message.answer_photo(
            photo="https://media.makeameme.org/created/sorry-you-lose.jpg",
            caption=f"Неправильно, я загадал {random_number}. Попробуйте снова!")
@dp.message()
async def echo(message: Message):
    await message.answer("Я вас не понял")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")