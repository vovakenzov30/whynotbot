from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
import asyncio

import config


async def main_menu(user_id):
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='🔗 Создать ссылку', callback_data='catalog'),
            ],
            [
                InlineKeyboardButton(text='🗄 Мои ссылки', callback_data='profile'),
                InlineKeyboardButton(text='💬 Чаты', callback_data='profile'),
            ],
            [
                InlineKeyboardButton(text='⚙️ Настройки', callback_data='information'),
            ],
        ]
    )
    if config.admin_id in config:
        markup.add(
            InlineKeyboardButton(text='⭐️ Админка', callback_data='admin')
        )

    return markup
