from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import CHANNEL_USERNAME

join_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📢 Join Channel",
                url=f"https://t.me/{CHANNEL_USERNAME.replace('@', '')}"
            )
        ],
        [
            InlineKeyboardButton(
                text="✅ I've Joined",
                callback_data="check_join"
            )
        ]
    ]
)
