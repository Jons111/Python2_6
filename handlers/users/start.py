from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery, KeyboardButton, ReplyKeyboardMarkup
from keyboards.default.menu_uchun import menu_button
from keyboards.default.taomlar_uchun import taomlar_button
from keyboards.inline.tillar_uchun import tillar_buttons
from loader import dp, base, bot
from filters.shaxsiy_uchun import Shaxsiy

@dp.message_handler(Shaxsiy(),CommandStart())
async def bot_start(message: types.Message):
    ism = message.from_user.first_name
    fam = message.from_user.last_name
    user_id = message.from_user.id
    try:
        base.user_qoshish(ism=ism,fam=fam,username=message.from_user.username,tg_id=user_id)
    except Exception:
        pass
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=tillar_buttons)

menular = base.select_all_menu()
@dp.message_handler(text=[menu[1] for menu in menular])
async def bot_start(message: types.Message):
    typee = message.text
    maxsulotlar = base.select_maxsulotlar(tur=typee)
    index = 0
    i = 0
    royxat = []
    for menu in maxsulotlar:
        # (1, 'Toamlar')
        if i % 2 == 0 and i != 0:
            index += 1
        if i % 2 == 0:
            royxat.append([KeyboardButton(text=menu[1])])
        else:
            royxat[index].append(KeyboardButton(text=menu[1]))
        i += 1
    royxat.append([KeyboardButton(text="Ortga")])
    maxsulot_button = ReplyKeyboardMarkup(keyboard=royxat, resize_keyboard=True)

    await message.answer(f"Assalomu alaykum maxsulotni tanlang",reply_markup=maxsulot_button)




menular = base.select_all_maxsulotlar()
@dp.message_handler(text=[menu[1] for menu in menular])
async def bot_start(message: types.Message):
    typee = message.text
    maxsulot = base.select_maxsulotlar(nomi=typee)[0]
    "(4, 'Cola', 10000, 'https://t.me/UstozShogird/25992', None, 'Ichimliklar')"
    max_nomi = maxsulot[1]
    max_narxi = maxsulot[2]
    max_rasmi = maxsulot[3]
    user_id = message.from_user.id
    await bot.send_photo(chat_id=user_id,photo=max_rasmi,caption=f"Nomi : {max_nomi}\n"
                                                                 f"Narxi : {max_narxi}\n"
                                                                 )














@dp.callback_query_handler(text="til1")
async def bot_start(xabar: CallbackQuery):
    await xabar.message.answer(f"Assalomu alaykum Taomlarni tanlang",reply_markup=menu_button)


@dp.message_handler(text="Ortga",)
async def bot_start(message: types.Message):
    await message.answer(text="Menu",reply_markup=menu_button)