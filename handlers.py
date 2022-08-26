from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.dispatcher.filters import Text, Command
from aiogram.dispatcher import FSMContext

#from keyboards import keyboard, keyboard1, kotik_key, cb, key_change_goods
from main import bot, dp

@dp.message_handler(Command('start'))
async def show_shop(message: Message):
    await message.answer('Здравствуйте, выберите действие\n'
                         '/register чтобы зарегистрироваться\n'
                         '/money чтобы ввести траты')

@dp.message_handler(Command('register'))
async def show_shop(message: Message):
    await message.answer('Для эффективного менеджмента бюджета, рекомендуется\n разбивать траты на несколько категорий,'
                         ' таких как:\n✅ Основные траты, например еда, сотовая связь или квартира\n'
                         '✅ Дополнительные траты, например одежда или развлечения\n ✅ Откладываемые деньги, '
                         'например на отпуск\n ✅ Инвестиции\n Выберите какой процент каждому из этих '
                         'ответвлений вы бы хотели задать.')

