from aiogram import types
from app import dp
import config


@dp.message_handler(text='/start')
async def command_start(message: types.Message):
    await message.answer_photo(photo=config.photo,
                               caption=f'<b>Welcome {message.from_user.full_name} to my bot!</b>',
                               )
