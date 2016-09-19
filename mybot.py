
def method1(bot, update):
    ## some logic goes here
    result = "The task1 is completed. Please take a look what we have."
    bot.sendMessage(chat_id=update.message.chat_id, text=result)

def method2(bot, update):
    ## some logic goes here
    result = "The task2 is completed. Please take a look what we have."
    bot.sendMessage(chat_id=update.message.chat_id, text=result)

