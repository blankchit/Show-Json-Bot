#!/usr/bin/env python3
# Copyright (C) @ZauteKm
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import os
from config import Config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserIsBlocked, PeerIdInvalid

@Client.on_message(filters.command('start'))
async def start(c, m):
    owner = await c.get_users(int(Config.OWNER_ID))
    owner_username = owner.username if owner.username else 'Ns_bot_updates'

    # start text
    text = f"""Hey! {m.from_user.mention(style='md')},

💡 ** I am Telegram ShowJson Bot**

`Get the json for the text, media, etc.`

**👨‍💻 Made with by ❤️:** {owner.mention(style='md')}
"""

    # Buttons
    buttons = [
        [
            InlineKeyboardButton('👨‍💻 Developer', url=f"https://t.me/{owner_username}"),
            InlineKeyboardButton('Dev Channel 📢', url=f"https://t.me/ZauteKm")
        ],
        [
            InlineKeyboardButton('🗣️ Feedback', url=f"https://t.me/zautebot"),
            InlineKeyboardButton(' Channel 📢', url=f"https://t.me/TGBotsProJect")
        ]
    ]
    await m.reply_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )



@Client.on_message(filters.private & filters.incoming)
async def show_json(c, m):
    text = f'`{m}`'
    if len(text) <= 4096:
        await m.reply_text(text)
    else:
        with open(f'Your json file {m.from_user.first_name}.json', 'w') as f:
            f.write(text)
        await m.reply_document(f'Your json file {m.from_user.first_name}.json', True)
        os.remove(f'Your json file {m.from_user.first_name}.json')

@Client.on_inline_query()
async def inline_json(c, m):
    if m.query == "":
      await m.answer(
        results=[],
        switch_pm_text="Type something to get json",
        switch_pm_parameter="start",
        cache_time=0
    )
      return

    text = f'`{m}`'
    switch_pm_text = f"Hey i sent the json in PM 😉"
    try:
        if len(text) <= 4096:
            await c.send_message(chat_id=m.from_user.id, text=text)
        else:
            with open(f'Your json file {m.from_user.first_name}.json', 'w') as f:
                f.write(text)
            await c.send_document(chat_id=m.from_user.id, file_name=f'Your json file {m.from_user.first_name}.json')
    except UserIsBlocked:
        switch_pm_text="You have Blocked the bot,Unblock it "
        pass
    except PeerIdInvalid:
        switch_pm_text="Please start the bot once in pm and try again"
        pass
    except Exception as e:
        print(e)
        switch_pm_text="Something went wrong"
        pass

    try: # if file exist try to delete..
       os.remove(f'Your json file {m.from_user.first_name}.json')
    except: # else continue
        pass

    await m.answer(
        results=[],
        switch_pm_text=switch_pm_text,
        switch_pm_parameter="start",
        cache_time=0
    )
