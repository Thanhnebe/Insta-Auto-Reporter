#The Code was made by ridha for purposes educational only don't use it for other ilegal purposes

from instabot import Bot
import os

bot = Bot()

attackeruser = input("Enter your username: ")
attackerpassword = input("Enter your account password: ")
bot.login(username= attackeruser, password= attackerpassword)

uname = input("Enter username of target: ")
uid = bot.get_userid_from_username(uname)


Realy = input("Are sure wanted to report? (1 to yes and 0 to no)")

while Realy ==1:
    bot.report_user(user_id= uid)

else:
    print("The user has canceled proccess")
    
