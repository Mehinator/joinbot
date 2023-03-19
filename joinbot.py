import os
import logging
from telegram.ext import Updater, CommandHandler
from telegram import ChatAction, InputMediaVideo, InputMediaPhoto

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Define the function to check if the user has joined the channel
def check_join(update, context):
    # Get the user ID and channel ID
    user_id = update.message.from_user.id
    channel_id = '@kirtanha'

    # Check if the user has joined the channel
    user_in_channel = context.bot.get_chat_member(channel_id, user_id).status == 'member'

    # If the user is in the channel, send a clip or photo
    if user_in_channel:
        # Send a typing indicator while processing the request
        context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)

        # Send a clip or photo
        media_file = 'path/to/your/media/file.mp4'  # Replace with the path to your media file
        if media_file.endswith('.mp4'):
            context.bot.send_video(chat_id=update.message.chat_id, video=open(media_file, 'rb'))
        elif media_file.endswith('.jpg') or media_file.endswith('.jpeg') or media_file.endswith('.png'):
            context.bot.send_photo(chat_id=update.message.chat_id, photo=open(media_file, 'rb'))
        else:
            context.bot.send_message(chat_id=update.message.chat_id, text='Sorry, I could not send the media file.')

    # If the user is not in the channel, send a message
    else:
        context.bot.send_message(chat_id=update.message.chat_id, text='Please join our channel to access the content: ' + channel_id)

# Define the main function to start the bot
def main():
    # Set up the bot and its token
    updater = Updater(token=os.environ.get('938991477:AAGXktVkPUkCwEKTQ1PexjNN66ieEsFpuak'), use_context=True)

    # Add a command handler to the bot
    updater.dispatcher.add_handler(CommandHandler('check_join', check_join))

    # Start the bot
    updater.start_polling()
    updater.idle()

# Call the main function to start the bot
if __name__ == '__main__':
    main()
