import logging

from aiogram import Dispatcher

from config import admin_id


async def on_startup_notify(dp: Dispatcher):
    for admin in admin_id:
        try:
            text = 'START'
            await  dp.bot.send_message(chat_id=admin, text=text)
        except Exception as err:
            logging.exception(err)
