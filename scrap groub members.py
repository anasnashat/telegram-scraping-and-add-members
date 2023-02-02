try:

    from telethon import TelegramClient, events
    import asyncio
except:
    import os
    os.system('pip install telethon')
    from telethon import TelegramClient, events
    import asyncio


api_id = ''
api_hash = ''
phone = ''

client = TelegramClient('session_name', api_id, api_hash)
client.start(phone=phone)

async def main():
    dilogs = await client.get_dialogs()
    for dilog in dilogs:
        print(f'name = {dilog.name},  id = {dilog.id}')
        groub= input('enter groub id : ')
        if dilog.id == groub:  # group ID if u need name use dilog.name
            users = await client.get_participants(dilog.id)
            for user in users:
                user_id = user.username # if you need to scrap id repace username with id
                if user_id != None:
                    print(user_id)
                    # save user
                    open('users.txt','a').write(f'{user_id}\n')