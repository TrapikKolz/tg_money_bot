import asyncio
import time

from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.dispatcher.filters import Text, Command
from aiogram.dispatcher import FSMContext

from keyboards import register_keyboard, start_register_keyboard
from main import bot, dp
from states import Register
from sql import register_sql, check_chat_id_regester

@dp.message_handler(Command('start'))
async def expenses_start(message: Message):
    await message.answer('Здравствуйте, выберите действие\n'
                         '/register чтобы зарегистрироваться\n'
                         '/money чтобы ввести траты')

@dp.message_handler(Command('register'), state=None)
async def register(message: Message):
    """
    ПРОВЕРКА НА НАЛИЧИЕ АККАУНТА
    :param message:
    :return:
    """
    if check_chat_id_regester(message.chat.id)[0]:
        await message.answer('Для эффективного менеджмента бюджета, рекомендуется\n '
                             'разбивать траты на несколько категорий,'
                             ' таких как:\n✅ Основные траты, '
                             'например еда, сотовая связь или квартира\n'
                             '✅ Дополнительные траты, например одежда или развлечения\n '
                             '✅ Откладываемые деньги, '
                             'например на отпуск\n ✅ Инвестиции\n '
                             'Выберите какой процент каждому из этих '
                             'ответвлений вы бы хотели задать.\n '
                             'Выберите процент из предложенного списка или задайте '
                             'свое значение. Выберите 0 чтобы убрать данный пункт. '
                             'Помните что в сумме должно получиться 100 процентов.',
                             reply_markup=start_register_keyboard)
        await Register.step1.set()
    else:
        await message.answer('Вы уже зарегестрировались, ' + check_chat_id_regester(message.chat.id)[1])

@dp.message_handler(state=Register.step1)
async def register(message: Message, state: FSMContext):
    await message.answer('Начнем с основных трат, выберите процент для них:',
                         reply_markup=register_keyboard)

    await Register.next()

@dp.message_handler(state=Register.step2)
async def register(message: Message, state: FSMContext):
    chat_id = message.chat.id
    username = message.chat.username
    first_name = message.chat.first_name
    last_name = message.chat.last_name
    try:
        OSN_percent = int(message.text)
    except:
        await message.answer('Введите корректный процент!'
                             'Для повторной регистрации нажмите /register')
        OSN_percent = False
        await state.finish()

    if OSN_percent:
        await state.update_data(
            {
                'chat_id': chat_id,
                'username': username,
                'first_name': first_name,
                'last_name': last_name,
                'OSN_percent': OSN_percent
            }
        )
        text = f'(осталось {100 - OSN_percent} процентов)'
        await message.answer('Выберите процент для дополнительных трат:' + text,
                             reply_markup=register_keyboard)
        await Register.next()

@dp.message_handler(state=Register.step3)
async def register(message: Message, state: FSMContext):
    DOP_percent = int(message.text)
    await state.update_data(
        {
            'DOP_percent': DOP_percent
        }
    )

    data = await state.get_data()
    OSN_percent = data.get('OSN_percent')
    text = f'(осталось {100 - OSN_percent - DOP_percent} процентов)'

    await message.answer('Выберите процент денег, которые вы будете откладывать с каждой зарплаты:' + text,
                         reply_markup=register_keyboard)
    await Register.next()

@dp.message_handler(state=Register.step4)
async def register(message: Message, state: FSMContext):
    OTK_percent = int(message.text)
    await state.update_data(
        {
            'OTK_percent': OTK_percent
        }
    )
    await message.answer('Какой процент вы будете тратить на инвестиции?',
                         reply_markup=register_keyboard)
    await Register.next()

@dp.message_handler(state=Register.step5)
async def register(message: Message, state: FSMContext):
    INV_percent = int(message.text)
    await state.update_data(
        {
            'INV_percent': INV_percent
        }
    )

    data = await state.get_data()
    chat_id = data.get('chat_id')
    username = data.get('username')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    OSN_percent = data.get('OSN_percent')
    DOP_percent = data.get('DOP_percent')
    OTK_percent = data.get('OTK_percent')
    INV_percent = data.get('INV_percent')

    register_sql(chat_id, username, first_name, last_name, OSN_percent, DOP_percent, OTK_percent, INV_percent)
    await state.finish()
