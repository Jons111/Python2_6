
from aiogram.dispatcher.filters.state import State,StatesGroup


class Forma(StatesGroup):
    ism_qabul_qilish = State()
    fam_qabul_qilish = State()
    yosh_qabul_qilish = State()
    matn_qabul_qilish = State()
    tasdiqlash = State()