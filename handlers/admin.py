from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from config import ADMIN_ID
from database import total_users, get_all_users

router = Router()

# Store broadcast mode for admins
broadcast_mode = set()


@router.message(Command("stats"))
async def stats(message: Message):
    if message.from_user.id != ADMIN_ID:
        return

    users = total_users()

    await message.answer(
        f"📊 <b>Bot Statistics</b>\n\n👥 Total Users: <b>{users}</b>"
    )


@router.message(Command("broadcast"))
async def broadcast(message: Message):
    if message.from_user.id != ADMIN_ID:
        return

    broadcast_mode.add(message.from_user.id)

    await message.answer(
        "📨 Send me the message you want to broadcast to all users."
    )


@router.message()
async def send_broadcast(message: Message):
    if message.from_user.id not in broadcast_mode:
        return

    broadcast_mode.remove(message.from_user.id)

    sent = 0
    failed = 0

    users = get_all_users()

    for user in users:
        try:
            await message.bot.send_message(
                chat_id=user[0],
                text=message.text
            )
            sent += 1
        except Exception:
            failed += 1

    await message.answer(
        f"""✅ Broadcast Finished

📤 Sent: {sent}
❌ Failed: {failed}
"""
    )
