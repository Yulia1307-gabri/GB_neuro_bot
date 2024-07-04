from aiogram import Router, types, F
from aiogram.filters.command import Command
from less3.keyboards.keyboards import kb1, kb2
from less3.keyboards.randomfox import fox
from random import randint


router = Router()


@router.message(Command("start"))
async def command_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Привет, {name}! Я бот - твой друг и товарищ!', reply_markup=kb1)


@router.message(Command("fox"))
async def command_fox(message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
    await message.answer(f'Держи лису, {name}', reply_markup=kb2)
    await message.answer_photo(photo=img_fox)


@router.message(Command("info"))
async def cmd_info(message: types.Message):
    await message.reply("Отправь мне любое сообщение, и я повторю его, отправь команду /fox - получишь фото лисы, команда /num и я сгенерирую случайное число.", reply_markup=kb2)


@router.message(Command('num'))
async def send_random(message: types.Message):
    number = randint(1, 10)
    await message.answer(f'{number}')


@router.message()
async def echo(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
    if 'привет' in msg_user:
        await message.answer(f'Привет, {name}')
    elif 'покажи лису' in msg_user:
        await message.answer(f'Держи лису')
    elif 'пока' in msg_user:
        await message.answer(f'Пока, {name}')
    elif 'ты кто' in msg_user:
        await message.answer(f'Я бот')
    else:
        await message.answer(message.text)

