from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, PollAnswerHandler, CallbackContext
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


# Replace 'YOUR_TOKEN' with the actual token obtained from BotFather
TOKEN = '6956518827:AAHE5UYhV9tTkH5gJtbTV8ZBxSql-ivMHUs'

def poll_answer(update: Update, context: CallbackContext) -> None:
    user = update.poll_answer.user
    poll_id = update.poll_answer.poll_id
    option_ids = update.poll_answer.option_ids

    context.bot.send_message(update.effective_chat.id,
                             f"User {user.username} selected options: {option_ids} in poll ID: {poll_id}")

async def gpt_create_poll(update: Update, context: CallbackContext) -> None:
    # Define poll options
    options = ["Option 1", "Option 2", "Option 3"]

    # Create a poll
    poll_message = update.message.reply_poll(
        question="Choose an option:",
        options=options,
        is_anonymous=False,
        allows_multiple_answers=True
    )

    # Save the poll ID for later reference if needed
    context.user_data['poll_id'] = poll_message.poll.id

async def publish_poll(update: Update, context: CallbackContext)->None:
    pass

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

def main() -> None:
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    # app.add_handler(CommandHandler("createpoll", create_poll))
    app.run_polling()
    # updater = Updater(TOKEN)
    # dp = updater.dispatcher
    # dp.add_handler(CommandHandler("start", start))
    # dp.add_handler(CommandHandler("createpoll", create_poll))
    #
    # # Add poll answer handler
    # dp.add_handler(PollAnswerHandler(poll_answer))
    # updater.start_polling()
    # updater.idle()


if __name__ == '__main__':
    main()
