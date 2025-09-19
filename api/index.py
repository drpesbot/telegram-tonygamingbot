import os
from typing import Optional

from fastapi import FastAPI, Request
from pydantic import BaseModel

from telegram import Update, Bot

TOKEN = os.environ.get("TOKEN")

app = FastAPI()


@app.post("/webhook")
async def webhook(request: Request):
    bot = Bot(token=TOKEN)
    update = Update.de_json(await request.json(), bot)

    if update.message:
        chat_id = update.message.chat_id
        text = update.message.text

        if text == "/start":
            await bot.send_message(
                chat_id=chat_id,
                text="❤️ اضغط على الرابط الذى بالاسفل للوصول إلى ستور تونى جمينج 👇👇\n❤️ هذا هو الرابط تفضل بالضغط عليه 👇👇\nhttps://t.me/pes224\n👆👆👆👆👆👆👆"
            )
        else:
            await bot.send_message(
                chat_id=chat_id,
                text="❤️ اضغط على الرابط الذى بالاسفل للوصول إلى ستور تونى جمينج 👇👇\n❤️ هذا هو الرابط تفضل بالضغط عليه 👇👇\nhttps://t.me/pes224\n👆👆👆👆👆👆👆"
            )

    return {"message": "ok"}

