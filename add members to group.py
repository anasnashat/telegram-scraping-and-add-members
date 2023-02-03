import time

try:

    from telethon import TelegramClient, events, functions
except:
    import os
    os.system('pip install telethon')
    from telethon import TelegramClient, events, functions
    import asyncio


api_id = 00
api_hash = ''
phone = ''
chat_id = input('inter chat id : ') # group chat ID
client = TelegramClient('session_name', api_id, api_hash)
client.start(phone=phone)


async def add_member():
    await client.start(phone)
    with open('users.txt', 'r') as f:
        user_ids = [line.strip() for line in f.readlines()]

    for user_name in user_ids:
        try:
            print(user_name)
            # group chat ID
            result = await client(
                functions.channels.InviteToChannelRequest(channel=chat_id,
                                                          users=[user_name]))

            time.sleep(50)  # to not get banned by telegram

            if result:
                print("User %d successfully added to the group", user_name)
            else:
                print("Failed to add user %d to the group", user_name)

        except Exception as e:
            print(e)
            continue

asyncio.get_event_loop().run_until_complete(add_member())