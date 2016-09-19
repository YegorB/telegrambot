from statistic import *

def log(func):
    def determine_args(bot, update):
        save_event(update)
        func(bot, update)
    return determine_args
