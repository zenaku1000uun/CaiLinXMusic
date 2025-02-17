from pyrogram import client, filters
from pyrogram.types import Message
import random
from CaiLinXMusic import app

EMOJIS = ["😍", "👍", "❤️", "💯", "💋", "🤣", "🥰", "😭", "🍌", "🎃", "🫡", "😘", "🥴", "😐", "😢", "😁", "👀", "🌚", "🍓", "🗿", "💔", "❤️‍🔥"]

@app.on_message(filters.incoming, group=-1)
async def react_to_messages(client, message: Message):
    try:
        random_emoji = random.choice(EMOJIS)
        await message.react(random_emoji)
    except Exception as e:
        print(f"Failed to react to message: {e}")
