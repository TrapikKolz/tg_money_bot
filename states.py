from aiogram.dispatcher.filters.state import StatesGroup, State

class Register(StatesGroup):
    step1 = State()
    step2 = State()
    step3 = State()
    step4 = State()
    step5 = State()