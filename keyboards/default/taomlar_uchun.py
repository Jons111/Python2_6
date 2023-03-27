from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

taomlar_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Osh"),
            KeyboardButton(text="Lag'mon")
        ],
        [
            KeyboardButton(text="Sho'rva"),
            KeyboardButton(text="Kabob")
        ]
    ],
    resize_keyboard=True
)