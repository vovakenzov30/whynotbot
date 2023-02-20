# from aiogram import types
#
# from app import dp
#
#
# @dp.message_handler(text='Создать ссылку')
# async def show_inline_menu(message: types.Message):
#     await message.answer('aaa', reply_markup=ikb_menu)

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🔗 Создать ссылку', callback_data='заглушка')
        ],
        [
            InlineKeyboardButton(text='🗄 Мои ссылки', callback_data='заглушка2'),
            InlineKeyboardButton(text='💬 Чаты', callback_data='заглушка3'),
        ],
        [
            InlineKeyboardButton(text='⚙️ Настройки', callback_data='настройки'),
        ],
    ]
),

settings_menu = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text='✅ Скрыть ник', callback_data='заглушка5'),
        InlineKeyboardButton(text='✅ Скрыть страну', callback_data='заглушка6'),
    ],
    [
        InlineKeyboardButton(text='🔤 Изменить Paytag', callback_data='заглушка7'),
        InlineKeyboardButton(text='💳 Изменить USDT кошелёк', callback_data='заглушка8'),
    ],

    [
        InlineKeyboardButton(text='🗂 Мои профили', callback_data='заглушка9'),
        InlineKeyboardButton(text='📌 Шаблоны ТП', callback_data='заглушка10'),
    ],
    [
        InlineKeyboardButton(text='👨‍🏫 Наставники', callback_data='заглушка11'),
    ],
])


