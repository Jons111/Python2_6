from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from loader import base

menular = base.select_all_menu()
print(menular)
index  =0
i = 0
royxat = []

for menu in menular:
    # (1, 'Toamlar')
    if i%2==0 and i !=0:
        index+=1
    if i%2==0:
        royxat.append([KeyboardButton(text=menu[1])])

    else:
        royxat[index].append(KeyboardButton(text=menu[1]))
    i+=1

menu_button = ReplyKeyboardMarkup(keyboard=royxat,resize_keyboard=True)


tasdiqlash_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Tasdiqlash"),
            KeyboardButton(text="Bekor qilish"),

        ],

    ],
    resize_keyboard=True
)