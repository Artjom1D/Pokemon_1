import telebot 
from config import token

from logic import Pokemon

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_message(message.chat.id, pokemon.type_pokemon())
        bot.send_message(message.chat.id, pokemon.rarity())
        bot.send_message(message.chat.id, "Покормить покемона - /feed\n"
                                      "Поиграть с покемоном - /play\n"
                                      "Узнать уровень покемона - /level\n")
        bot.send_photo(message.chat.id, pokemon.show_img())
        bot.send_message(message.chat.id, "Вот твой покемон!")
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=["feed"])
def feed(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        bot.send-message(message.chat.id, "Сначала создай покемона командой /go")
    else:
        pokemon = Pokemon.pokemons[message.from_user.username]
        bot.send_message(message.chat.id, pokemon.feed())

@bot.message_handler(commands=['play'])
def play(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        bot.send_message(message.chat.id, "Сначала создай покемона командой /go")
    else:
        pokemon = Pokemon.pokemons[message.from_user.username]
        bot.send_message(message.chat.id, pokemon.play())

@bot.message_handler(commands=['level'])
def lvlup(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        bot.send_message(message.chat.id, "Сначала создай покемона командой /go")
    else:
        pokemon = Pokemon.pokemons[message.from_user.username]
        bot.send_message(message.chat.id, pokemon.level_up())

bot.infinity_polling(none_stop=True)

