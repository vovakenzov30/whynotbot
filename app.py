import os

from aiogram import Bot, Dispatcher, types, executor
import config

# from aiogram.utils import executor
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


async def on_startup(dp):
    await bot.set_webhook(config.URL)


async def on_shutdown(dp):
    await bot.delete_webhook()


@dp.message_handler()
async def get_message(message: types.Message):
    chat_id = message.chat.id
    text = 'Hello'

    await bot.send_message(chat_id=chat_id, text=text)

executor.start_webhook(
    dispatcher=dp,
    webhook_path='',
    on_startup=on_startup,
    on_shutdown=on_shutdown,
    skip_updates=True,
    host="0.0.0.0",
    port=int(os.environ.get("PORT"), 5000)
)
