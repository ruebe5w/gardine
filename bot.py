#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Basic example for a bot that uses inline keyboards.
# This program is dedicated to the public domain under the CC0 license.
"""
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from gardineclass import Gardine

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(bot, update):
    keyboard = [[InlineKeyboardButton("Auf", callback_data='1'),
                 InlineKeyboardButton("Zu", callback_data='2')],

                [InlineKeyboardButton("Stop", callback_data='3')],
                [InlineKeyboardButton("Aktueller Zustand", callback_data='4')]
                ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Gardinensteuerung', reply_markup=reply_markup)


def button(bot, update):
    query = update.callback_query

    if query.data == '1':
        print("Auf")
        Gardine.f_auf()
        text = "Wird geöffnet!"
    if query.data == '2':
        print("Zu")
        Gardine.f_zu()
        text = "Wird geschlossen!"
    if query.data == '3':
        print("Stop")
        Gardine.f_stop()
        text = "Wird gestoppt!"
    if query.data == '4':
        print("Zustand")

        text = "Die Gardine ist aktuell " + Gardine.get_zustand() + "."
    bot.edit_message_text(text=text,
                          chat_id=query.message.chat_id,
                          message_id=query.message.message_id)
    keyboard = [[InlineKeyboardButton("Auf", callback_data='1'),
                 InlineKeyboardButton("Zu", callback_data='2')],

                [InlineKeyboardButton("Stop", callback_data='3')],
                [InlineKeyboardButton("Aktueller Zustand", callback_data='4')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    query.message.reply_text('Gardinensteuerung', reply_markup=reply_markup)


def help(bot, update):
    update.message.reply_text("Use /start to test this bot.")


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater('630231596:AAFe4YLV9MDeEnY-eCGfTNWLyXAhaj4_XVY')

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


main()