import os
# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.response_selection import get_most_frequent_response
from chatterbot import trainers as ts
from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement , Response

# Create a new instance of a ChatBot
bot = ChatBot(
    "Swiggy",
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'What is the order status?',
            'output_text': 'It will reach within 5 minutes'
        },

        "chatterbot.logic.BestMatch",
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.4,
            'default_response': 'I am sorry, but I do not understand.'
        }

        # ,
        # {
        #     'import_path': 'functionBot.MyLogicAdapter'
        # }

    ],
    response_selection_method=get_most_frequent_response,
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    database="swiggyDB1.db"

)

# First, lets train our bot with some data
bot.train('chatterbot.corpus.english.greetings')

print("Type something to begin...")

# The following loop will execute each time the user enters input
while True:
    try:
        # We pass None to this method because the parameter
        # is not used by the TerminalAdapter
        bot_input = bot.get_response(None)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
