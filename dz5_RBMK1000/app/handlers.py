from aiogram.types import Message , CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram import F, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from app.keyboards import *
from baza import  *
router=Router()
@router.message(CommandStart())
async def nurdanacapomog(message:Message):
    await message.reply(f"привет {message.from_user.full_name} этот бот преднозначен для удобного доаступа к вашему счету нужные вам команды..")
    await kudbuhon()

class Zamena(StatesGroup):
    full_name = State()
    balanse= State()



