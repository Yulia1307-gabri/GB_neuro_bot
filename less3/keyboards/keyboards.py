from aiogram import types


button1 = types.KeyboardButton(text='/start')
button2 = types.KeyboardButton(text='/info')
button3 = types.KeyboardButton(text='привет')
button4 = types.KeyboardButton(text='пока')
button5 = types.KeyboardButton(text='/fox')
button6 = types.KeyboardButton(text='/num')
button7 = types.KeyboardButton(text='/prof')


keyboard1 = [
    [button1, button2]
    ]

keyboard2 = [
    [button3, button4, button5, button6, button7]
    ]

kb1 = types.ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)
kb2 = types.ReplyKeyboardMarkup(keyboard=keyboard2, resize_keyboard=True)
