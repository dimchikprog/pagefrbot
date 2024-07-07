import telebot
import sqlite3
import eel
def getUserBirth(id):
    c.execute("SELECT id FROM users")
    for i in c.fetchall():
        if i == id:
            c.execute("SELECT dates FROM users")
            birthday = c.fetchone()
    return birthday

def createBirthDate(tableName, newDate):
    c.execute("INSERT INTO " +  tableName + " VALUES ('" + newDate + "')")
    c.execute("SELECT * FROM " + tableName)
    print("Successfully did - now you have: " + str(c.fetchall()))
#creating telegram bot
bot = telebot.TeleBot("7468997329:AAEOHqlGFZQEgi1wXCM70SHsKNZm-lGpP6M")

@bot.message_handler(content_types="text")
def get_mess(message):
    bot.send_message(message.from_user.id, "hello")
    id = message.from_user.id
    print(getUserBirth(id))
    eel.init("web")

    eel.get_user_id('5186301276')


    eel.start("index.html")













db = sqlite3.connect('users.db')
c = db.cursor()
#creating table
#c.execute("""CREATE TABLE users (
#        date text,
#        id text
#          )""")
#
#inserting date
#c.execute("INSERT INTO users VALUES ('26.05.2011', '5186301276')")
#c.execute("UPDATE dates SET date = '26.05.2011'")




















bot.infinity_polling()