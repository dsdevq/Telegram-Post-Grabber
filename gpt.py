# Bot 2: Admin Bot
import json
from os.path import abspath
from time import sleep
from telethon import TelegramClient, Button, events
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Read config file
with open(abspath('grabber-config.json'), encoding='utf-8') as f:
    config = json.load(f)

# Ensure this session name is unique for the admin bot
client = TelegramClient('bot_gpt_session_admin', config['client']['api_id'], config['client']['api_hash'])
client.start(bot_token=config['bot']['gpt-token'])

@client.on(events.NewMessage(chats=config['bot']['gpt_channels']))
async def handler(event):
    # Send the message with the GPT, GPT + DALLE, Later, and Trash inline buttons
    for user_id in config['bot']['all_ID']:
        await client.send_message(user_id, event.message)
        sleep(1)

client.run_until_disconnected()
