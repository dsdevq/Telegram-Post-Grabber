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
client = TelegramClient('bot_session_admin', config['client']['api_id'], config['client']['api_hash'])
client.start(bot_token=config['bot']['actions-token'])

@client.on(events.NewMessage)
async def handler(event):
    # Define the keyboard with GPT, GPT + DALLE, Later, and Trash buttons
    keyboard = [
        [  
            Button.inline("GPT", b"gpt"),
            Button.inline("GPT + DALLE", b"gpt_dalle")
        ],
        [
            Button.inline("Later", b"later"),
            Button.inline("Trash", b"trash")
        ]
    ]
    
    # Duplicate the message with buttons and send it
    if event.message:
        if event.message.media:
            # Send the media with the caption if it's a media message
            await client.send_file(event.chat_id, file=event.message.media, caption=event.message.text, buttons=keyboard)
        else:
            # Send just the text if it's a text message
            await client.send_message(event.chat_id, event.message.text, buttons=keyboard)
    
    # Delete the original message
    await event.message.delete()


@client.on(events.NewMessage(chats=config['settings']['my_channels']))
async def handler(event):
    # Define the keyboard with GPT, GPT + DALLE, Later, and Trash buttons
    keyboard = [
        [  
            Button.inline("GPT", b"gpt"),
            Button.inline("GPT + DALLE", b"gpt_dalle")
        ],
        [
            Button.inline("Later", b"later"),
            Button.inline("Trash", b"trash")
        ]
    ]
    
    # Send the message with the GPT, GPT + DALLE, Later, and Trash inline buttons
    for user_id in config['bot']['all_ID']:
        await client.send_message(user_id, event.message, buttons=keyboard)
        sleep(1)

# Handle the callback query when a button is clicked
@client.on(events.CallbackQuery)
async def callback_handler(event):
    data = event.data.decode('utf-8')

    if data == "gpt":
        # Edit the message to ask for confirmation with new buttons for GPT
        keyboard = [
            [Button.inline("Confirm", b"gpt_confirm")],
            [Button.inline("Back", b"back")]
        ]
        await event.edit(buttons=keyboard)

    elif data == "gpt_confirm":
        # Retrieve the original message
        original_message = await event.get_message()

        # Extract the text and media separately
        message_text = original_message.text  # This retrieves the text part
        message_media = original_message.media  # This retrieves the media part

        # Send the message without buttons
        for channel in config['bot']['gpt_channels']:
            if message_media:
                # Send media with caption if available
                await client.send_file(channel, file=message_media, caption=message_text)
            else:
                # Send just text if no media
                await client.send_message(channel, message_text)
            sleep(1)

        # Confirm the GPT choice
        await event.answer("You have chosen GPT!")

        # Update the message to reflect that GPT was chosen, hide other buttons
        keyboard = [
            [  
                Button.inline("GPT ✔️", b"gpt_chosen")
            ]
        ]
        await event.edit(buttons=keyboard)

    elif data == "gpt_dalle":
        # Edit the message to ask for confirmation with new buttons for GPT + DALLE
        keyboard = [
            [Button.inline("Confirm", b"gpt_dalle_confirm")],
            [Button.inline("Back", b"back")]
        ]
        await event.edit(buttons=keyboard)

    elif data == "gpt_dalle_confirm":

        original_message = await event.get_message()  # Correctly retrieve the original message

        for channel in config['bot']['gpt_dalle_channels']:
            await client.send_message(channel, original_message.message)
            sleep(1)

        # The user confirmed GPT + DALLE choice, perform the action
        await event.answer("You have chosen GPT + DALLE!")

        # Update the message to reflect that GPT + DALLE was chosen, hide other buttons
        keyboard = [
            [  
                Button.inline("GPT + DALLE ✔️", b"gpt_dalle_chosen")
            ]
        ]
        await event.edit(buttons=keyboard)

    elif data == "later":
        # User pressed "Later", resend the message to the bot chat
        original_message = await event.get_message()  # Correctly retrieve the original message

        # Resend the message with the original buttons
        keyboard = [
            [  
                Button.inline("GPT", b"gpt"),
                Button.inline("GPT + DALLE", b"gpt_dalle")
            ],
            [
                Button.inline("Later", b"later"),
                Button.inline("Trash", b"trash")
            ]
        ]

        for user_id in config['bot']['all_ID']:
            await client.send_message(user_id, original_message)  # Resend the message with buttons
            sleep(1)
        
        # Delete the original message
        await original_message.delete()

    elif data == "trash":
        # Edit the message to ask for confirmation with new buttons for Trash
        keyboard = [
            [Button.inline("Confirm", b"trash_confirm")],
            [Button.inline("Back", b"back")]
        ]
        await event.edit(buttons=keyboard)

    elif data == "trash_confirm":
        # The user confirmed Trash choice, perform the action
        await event.answer("Message moved to Trash!")

        # Update the message to reflect that Trash was chosen, with an option to go back
        keyboard = [
            [  
                Button.inline("Trash ✔️", b"trash_chosen")
            ],
            [  
                Button.inline("Back", b"back_to_initial")
            ]
        ]
        await event.edit(buttons=keyboard)

    elif data == "back_to_initial":
        # User pressed "Back" after confirming Trash, return to the initial button layout
        keyboard = [
            [  
                Button.inline("GPT", b"gpt"),
                Button.inline("GPT + DALLE", b"gpt_dalle")
            ],
            [
                Button.inline("Later", b"later"),
                Button.inline("Trash", b"trash")
            ]
        ]
        await event.edit(buttons=keyboard)


    elif data == "back":
        # User pressed "Back", return to the initial button layout
        keyboard = [
            [  
                Button.inline("GPT", b"gpt"),
                Button.inline("GPT + DALLE", b"gpt_dalle")
            ],
            [
                Button.inline("Later", b"later"),
                Button.inline("Trash", b"trash")
            ]
        ]
        await event.edit(buttons=keyboard)

    elif data == "gpt_chosen" or data == "gpt_dalle_chosen" or data == "trash_chosen":
        # Handle the case if the user tries to click the already chosen button
        await event.answer("This option has already been chosen.", alert=True)

client.run_until_disconnected()
