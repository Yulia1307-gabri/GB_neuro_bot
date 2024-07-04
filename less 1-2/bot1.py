import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import config
from keyboards import kb1, kb2
from randomfox import fox
from random import randint

API_TOKEN = config.token

# Включаем логирование, чтобы видеть сообщения в консоли
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def command_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Привет, {name}! Я бот - твой друг и товарищ!', reply_markup=kb1)


@dp.message(Command("fox"))
async def command_fox(message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
    await message.answer(f'Держи лису, {name}', reply_markup=kb2)
    await message.answer_photo(photo=img_fox)


@dp.message(Command("info"))
async def cmd_info(message: types.Message):
    await message.reply("Отправь мне любое сообщение, и я повторю его, отправь команду /fox - получишь фото лисы, команда /num и я сгенерирую случайное число.", reply_markup=kb2)


@dp.message(Command('num'))
async def send_random(message: types.Message):
    number = randint(1, 10)
    await message.answer(f'{number}')


@dp.message()
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


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())