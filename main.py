@Client.on_message(filters.text & filters.private & filters.incoming & filters.user(AUTH_USERS) if AUTH_USERS else filters.text & filters.private & filters.incoming)
async def filter(client, message):
    if message.text.startswith("/"):
        return
    if AUTH_CHANNEL:
        invite_link = await client.create_chat_invite_link(int(AUTH_CHANNEL))
        try:
            user = await client.get_chat_member(int(AUTH_CHANNEL), message.from_user.id)
            if user.status == "kicked":
                await client.send_message(
                    chat_id=message.from_user.id,
                    text="Sorry Sir, You are Banned to use me.",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await client.send_message(
                chat_id=message.from_user.id,
                text = "**Hey! 😃\n\nYou Have To Join Our Update Channel To Use Me ✅\n\nClick Bellow Button To Join Now.👇🏻**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🍿 Join Our Channel 🍿", url=invite_link.invite_link)
                        ],
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await client.send_message(
                chat_id=message.from_user.id,
                text="Something went Wrong.",
                parse_mode="markdown",
                disable_web_page_preview=True
            )
            return
    if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", message.text):
        return
    if 2 < len(message.text) < 100:    
        # search_msg = await message.reply_sticker(sticker='CAACAgIAAxkBAAEE-d1ipaeEBQABkYqzvvZYJL56zS218NcAAuUAA1advQoICxZklQXRiiQE')
        btn = []
        search = message.text

        mo_tech_yt = f"**🗂️ Title:** {search}\n**⭐ Rating:** {random.choice(RATING)}\n**🎭 Genre:** {random.choice(GENRES)}\n**"

        search = await validate_query(search)
        search = urllib.parse.quote(search)
        btn.append([InlineKeyboardButton(text="👉 Click Here To Download 👈", url=f"https://{MOVIE_WEBSITE}/q?search={search}")])
