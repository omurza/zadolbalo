import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import Command, CommandStart

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

buttons = [
    [KeyboardButton(text="билеты на оффлайн концерт /konc"), KeyboardButton(text="кино /kino")],
    [KeyboardButton(text="помощь /help")]
]
keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)


@dp.message(CommandStart())
async def nerd(message: Message):
    await message.reply(
        f"Здравствуйте, {message.from_user.full_name}! Я умный бот, созданный для покупки билетов. Вот нужные вам команды: /help, /kino, /konc", 
        reply_markup=keyboard  
    )


@dp.message(Command("help"))
async def nerd1(message: Message):
    await message.reply("Помощь: Для покупки билетов используйте команды.")

@dp.message(Command("konc"))
async def nerd1(message: Message):
    await message.reply("сейчас доступны Концерт A, Концерт B, Концерт C.")
@dp.message(Command("kino"))
async def nerd2(message: Message):
    await message.reply("Сейчас в прокате доступны: Биртуганчик, Планб, Ванчопа")

@dp.message(F.text.in_({'Биртуганчик', 'Планб', 'Ванчопа'}))
async def guess_number(message: Message):
    user_guess = message.text
    if user_guess == "Биртуганчик":
        await message.reply(
            "Ваш фильм: Биртуганчик\nhttps://youtu.be/M4ArOescLg0"
        )
    elif user_guess == "Планб":
        await message.reply(
            "Ваш фильм: Планб\nhttps://www.youtube.com/watch?v=PgLHt72CzzA"
        )
    elif user_guess == "Ванчопа":
        await message.reply(
            "Ваш фильм: Ванчопа\nhttps://www.youtube.com/watch?v=jAJRNmJLB0Q"
        )
    else:
        await message.reply("Такого выбора не было.")

@dp.message(F.text.in_({'Концерт A', 'Концерт B', 'Концерт C'}))
async def concert_selection(message: Message):
    user_choice = message.text

    if user_choice == "Концерт A":
        await message.reply(
            "Ваш концерт: Концерт A\nСсылка на покупку билетов: https://www.concerts.com/concert-a"
        )
    elif user_choice == "Концерт B":
        await message.reply(
            "Ваш концерт: Концерт B\nСсылка на покупку билетов: https://www.concerts.com/concert-b"
        )
    elif user_choice == "Концерт C":
        await message.reply(
            "Ваш концерт: Концерт C\nСсылка на покупку билетов: https://www.concerts.com/concert-c"
        )
    else:
        await message.reply("Такого концерта нет в списке.")
        
@dp.message()
async def echo(message: Message):
    await message.answer("Я вас не понял")
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(dp.start_polling(bot))
