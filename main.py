import telebot 
from config import token
from random import randint
from logic import Pokemon, Warrior, Wizard

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
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

@bot.message_handler(commands=['hospital'])
def hospital(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        bot.send_message(message.chat.id, "Сначала создай покемона командой /go")
    else:
        pokemon = Pokemon.pokemons[message.from_user.username]
        bot.send_message(message.chat.id, pokemon.hospital())

@bot.message_handler(commands=['attack'])
def attack_pok(message):
    if message.reply_to_message:
        if message.reply_to_message.from_user.username in Pokemon.pokemons.keys() and message.from_user.username in Pokemon.pokemons.keys():
            enemy = Pokemon.pokemons[message.reply_to_message.from_user.username]
            pok = Pokemon.pokemons[message.from_user.username]
            res = pok.attack(enemy)
            bot.send_message(message.chat.id, res)
        else:
            bot.send_message(message.chat.id, "Сражаться можно только с покемонами")
    else:
            bot.send_message(message.chat.id, "Чтобы атаковать, нужно ответить на сообщения того, кого хочешь атаковать")

bot.infinity_polling(none_stop=True)

