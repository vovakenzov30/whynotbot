from aiogram import Bot, types, utils
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import keyboards.inline_menu
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
import config
import os
from keyboards.inline_menu import *
# from aiogram.utils import executor
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


async def on_startup(dp):
    await bot.set_webhook(config.URL_APP)


async def on_shutdown(dp):
    await bot.delete_webhook()

@dp.message_handler(text='/start')
async def command_start(message: types.Message):
    user_id = message.from_user.id
    await message.answer_photo(photo=config.photo,
                               caption=f'<b>Welcome {message.from_user.full_name} to my bot!</b>'
                               )

@dp.message_handler()
async def get_message(message: types.Message):
    chat_id = message.chat.id
    text = 'Hello'
    await  on_startup_notify(dp)
    await  set_default_commands(dp)
    await bot.send_message(chat_id=chat_id, text=text)


executor.start_webhook(
    dispatcher=dp,
    on_startup=on_startup,
    on_shutdown=on_shutdown,
    skip_updates=True,
    webhook_path='',
    host="0.0.0.0",
    port=int(os.environ.get('PORT', 5000))
)
