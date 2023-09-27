import asyncio
from pyrogram import Client
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime


api_id = 1
api_hash = ''



async def photo():
    while True:
        img = Image.open('12.jpg')
        I1 = ImageDraw.Draw(img)
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        meFont = ImageFont.truetype('123.ttf', 40)
        I1.text((400, 50), f'current time is: {current_time}', fill=(255, 0, 0), font=meFont)
        img.save('123.jpg')
        async with Client('myacc', api_id, api_hash) as app:

            async for ph in app.get_chat_photos("me"):
                asd = ph.file_id
            # Get the photos to be deleted



            # Delete one photo
            await app.delete_profile_photos(asd)
            await app.set_profile_photo(photo='123.jpg')
        await asyncio.sleep(60)

asyncio.get_event_loop().run_until_complete(photo())
