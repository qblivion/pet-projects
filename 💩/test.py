from pyrogram import Client
import asyncio

api_id = 19890531
api_hash = "7ec8158285a1d583eaea1d881c70ca2e"
app = Client("my_account", api_id=api_id, api_hash=api_hash)


async def react_to_messages(chat_id, emoji):
    async with Client("my_account", api_id, api_hash) as app:
        async for message in app.get_chat_history(chat_id, limit=100):
            await app.send_reaction(chat_id, message.id, emoji)
            # await asyncio.sleep(1)


asyncio.run(react_to_messages("@anonimus2004", "💩"))
