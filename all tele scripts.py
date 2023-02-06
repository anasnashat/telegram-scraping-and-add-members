import time
import asyncio

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
chat_id =00   # group chat ID

client = TelegramClient('session_name22', api_id, api_hash)
client.start(phone=phone)


async def scrap_members():
    dilogs = await client.get_dialogs()
    for dilog in dilogs:
        print(f'name = {dilog.name},  id = {dilog.id}')
    groub = input('inter group id : ')
    users = await client.get_participants(int(groub))
    for user in users:
        user_id = user.username  # if you need to scrap id repace username with id
        if user_id is not None:
            print(user_id)
            # save user
            open('users.txt', 'a').write(f'{user_id}\n')


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

            # to not get banned by telegram

            if result:
                print("User %d successfully added to the group", user_name)
                time.sleep(50)
            else:
                print("Failed to add user %d to the group", user_name)
                time.sleep(50)

        except Exception as e:
            print(e)
            time.sleep(50)
            continue


print('for scrap members from group enter 1')
print('for add members to group enter 2')
need = int(input('what you need : '))
if need == 1:
    asyncio.get_event_loop().run_until_complete(scrap_members())
if need == 2:
    asyncio.get_event_loop().run_until_complete(add_member())