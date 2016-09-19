from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.bot_db
stats = db.stats


def save_event(update):
    message = {"chat_id" : update.message.chat_id,
                "command" : "start"}
    stats.insert_one(message)
