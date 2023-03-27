from aiogram import types
from aiogram.types import ContentTypes

from loader import dp,bot
from filters.guruh_uchun import Guruh

# Echo bot
@dp.message_handler(Guruh(),commands="start",)
async def bot_echo(message: types.Message):
    await message.answer(text="Guruhga hush kelibsiz")


@dp.message_handler(Guruh(),content_types=ContentTypes.NEW_CHAT_MEMBERS)
async def bot_echo(message: types.Message):
    ism = message.new_chat_members[0].full_name
    chat_id = message.chat.id
    await bot.send_message(chat_id=chat_id,text=f"Guruhga hush kelibsiz {ism}")

@dp.message_handler(Guruh(),content_types=ContentTypes.LEFT_CHAT_MEMBER)
async def bot_echo(message: types.Message):
    ism = message.left_chat_member.full_name
    chat_id = message.chat.id
    msg_id = message.message_id
    await bot.send_message(chat_id=chat_id,text=f"Guruhni tark etdi {ism}")
    await bot.delete_message(chat_id=chat_id,message_id=msg_id)

@dp.message_handler(Guruh(),content_types=ContentTypes.STICKER)
async def bot_echo(message: types.Message):

    chat_id = message.chat.id
    msg_id = message.message_id
    user_id = message.from_user.id
    await bot.kick_chat_member(chat_id=chat_id,user_id=user_id,until_date='15:36')
    await bot.delete_message(chat_id=chat_id,message_id=msg_id)


@dp.message_handler(Guruh(),commands='unban')
async def bot_echo(message: types.Message):

    chat_id = message.chat.id
    msg_id = message.message_id
    user_id = message.from_user.id
    await bot.unban_chat_member(chat_id=chat_id,user_id=user_id,only_if_banned=True)
    await bot.kick_chat_member(chat_id=chat_id,user_id=user_id,until_date=1)
















