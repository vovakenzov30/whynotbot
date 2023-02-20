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
                                         InlineKeyboardButton(text='⚙️ Настройки', callback_data='заглушка4'),
                                     ],

                                 ])