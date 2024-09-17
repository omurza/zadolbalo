from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from app.BAZA import register_user, get_user_balance, transfer_money

router = Router()
# nvtchnjm
class TransferState(StatesGroup):
    waiting_for_amount = State()
    waiting_for_receiver = State()

@router.message(Command("start"))
async def start_command(message: types.Message):
    chat_id = message.from_user.id
    full_name = message.from_user.full_name
    await message.reply(f"Привет, {full_name}! Я бот для управления вашим счётом. Используйте /create_account для создания счёта, /balance для проверки баланса и /transfer для перевода денег.")

@router.message(Command("create_account"))
async def create_account_command(message: types.Message):
    chat_id = message.from_user.id
    full_name = message.from_user.full_name
    register_user(chat_id, full_name)
    await message.reply("Счёт создан!")

@router.message(Command("balance"))
async def balance_command(message: types.Message):
    chat_id = message.from_user.id
    balance = get_user_balance(chat_id)
    if balance is not None:
        await message.reply(f"Ваш баланс: {balance} рублей.")
    else:
        await message.reply("Создайте счёт с помощью /create_account.")

@router.message(Command("transfer"))
async def transfer_command(message: types.Message, state: FSMContext):
    chat_id = message.from_user.id
    balance = get_user_balance(chat_id)
    if balance is not None:
        await message.reply("Сколько денег хотите перевести?")
        await TransferState.waiting_for_amount.set()
    else:
        await message.reply("Создайте счёт с помощью /create_account.")

@router.message(TransferState.waiting_for_amount)
async def process_amount(message: types.Message, state: FSMContext):
    amount_text = message.text
    if amount_text.isdigit():
        amount = int(amount_text)
        if amount > 0:
            chat_id = message.from_user.id
            balance = get_user_balance(chat_id)
            if balance is not None and balance >= amount:
                await state.update_data(amount=amount)
                await message.reply("Теперь введите ID пользователя, которому хотите перевести деньги:")
                await TransferState.waiting_for_receiver.set()
            else:
                await message.reply("Недостаточно денег.")
        else:
            await message.reply("Введите положительное число.")
    else:
        await message.reply("Введите сумму в виде числа.")

@router.message(TransferState.waiting_for_receiver)
async def process_receiver(message: types.Message, state: FSMContext):
    receiver_id_text = message.text
    if receiver_id_text.isdigit():
        receiver_chat_id = int(receiver_id_text)
        data = await state.get_data()
        amount = data['amount']
        sender_chat_id = message.from_user.id
        if transfer_money(sender_chat_id, receiver_chat_id, amount):
            await message.reply("Деньги переведены.")
        else:
            await message.reply("Ошибка. Проверьте ID получателя и наличие денег.")
        await state.clear()
    else:
        await message.reply("Введите ID пользователя в виде числа.")
