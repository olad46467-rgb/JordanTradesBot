from aiogram.exceptions import TelegramBadRequest
from config import CHANNEL_USERNAME

async def is_user_joined(bot, user_id):
    try:
        member = await bot.get_chat_member(CHANNEL_USERNAME, user_id)
        return member.status in ("member", "administrator", "creator")
    except TelegramBadRequest:
        return False
