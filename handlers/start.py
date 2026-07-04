from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from keyboards.buttons import join_keyboard
from utils.forcejoin import is_user_joined
from database import add_user

router = Router()


@router.message(CommandStart())
async def start_command(message: Message):

    add_user(
        message.from_user.id,
        message.from_user.first_name,
        message.from_user.username or ""
    )

    joined = await is_user_joined(
        message.bot,
        message.from_user.id
    )

    if joined:
        await message.answer(
            f"""
👋 <b>Welcome {message.from_user.first_name}!</b>

✅ Your membership has been verified.

Welcome to Jordan's Trades.
            """
        )

    else:
        await message.answer(
            """
🔒 <b>You must join our official channel first.</b>

1️⃣ Click <b>Join Channel</b>

2️⃣ Join the channel

3️⃣ Return and press <b>I've Joined</b>
            """,
            reply_markup=join_keyboard
        )


@router.callback_query(F.data == "check_join")
async def check_join(callback: CallbackQuery):

    joined = await is_user_joined(
        callback.bot,
        callback.from_user.id
    )

    if joined:

        await callback.message.edit_text(
            f"""
🎉 Welcome <b>{callback.from_user.first_name}</b>!

Your membership has been verified successfully.

Enjoy using Jordan's Trades Bot.
            """
        )

    else:

        await callback.answer(
            "❌ You haven't joined the channel yet.",
            show_alert=True
        )
