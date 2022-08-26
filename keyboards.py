from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


register_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='0'),
            KeyboardButton(text='10'),
            KeyboardButton(text='20')
        ],
        [
            KeyboardButton(text='30'),
            KeyboardButton(text='40'),
            KeyboardButton(text='50')
        ],
        [
            KeyboardButton(text='60'),
            KeyboardButton(text='70'),
            KeyboardButton(text='80')
        ],
    ],
    resize_keyboard=True
)

start_register_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Начать регистрацию')
        ],
    ],
    resize_keyboard=True
)
