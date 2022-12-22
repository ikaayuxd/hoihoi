from telethon import TelegramClient, events, Button, types, functions, errors

bot_token = ("5595411530:AAGFEHeg9XgmwTPaP113VDoUtN8dFeICUOo")
try:
    bot = TelegramClient(None, 6, "eb06d4abfb49dc3eeb1aeb98ae0f581e").start(
        bot_token=bot_token
    )
except Exception as e:
    log.exception(e)
    exit(1)

start_msg = """Hi {user}!
**I'm Channel Actions Bot, a bot mainly focused on working with the new [admin approval invite links](https://t.me/telegram/153).**
**__I can__**:
- __Auto approve new join requests.__
- __Auto Decline New Join Requests.__
`Click the below button to know how to use me!`"""
start_buttons = [
    [Button.inline("How to use me ❓", data="helper")],
    [Button.url("Updates", "https://t.me/BotzHub")],
]


@bot.on(events.NewMessage(incoming=True, pattern=f"^/start({bot_username})?$"))
async def starters(event):
    from_ = await bot.get_entity(event.sender_id)
    await event.reply(
        start_msg.format(user=from_.first_name),
        buttons=start_buttons,
        link_preview=False,
    )
    if not (await is_added("BOTUSERS", event.sender_id)):
        await add_to_db("BOTUSERS", event.sender_id)
