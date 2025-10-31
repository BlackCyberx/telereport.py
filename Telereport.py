import os
import sys
import time
import requests
from telegram import Bot

#Function to install dependencies
def install_dependencies():
    os.system('pip install telegram requests')

#Function to read proxies from a file
def read_proxies(file_path):
    with open(file_path, 'r') as file:
        proxies = file.readlines()
    return [proxy.strip() for proxy in proxies]

#Function to send a message to a Telegram channel or group
def send_telegram_message(bot_token, chat_id, message):
    bot = Bot(token=bot_token)
    bot.send_message(chat_id=chat_id, text=message)

#Main function
def main():
    #Install dependencies
    install_dependencies()

    #Prompt user for Telegram channel or group link
    channel_link = input("Enter the Telegram channel or group link: ")

    #Extract chat ID from the link
    chat_id = channel_link.split('/')[-1]

    #Prompt user for proxies file directory
    proxies_file_path = input("Enter the directory of the proxies file: ")

    #Read proxies from the file
    proxies = read_proxies(proxies_file_path)

    #Your Telegram bot token
    bot_token = 8384464770:AAH0X5iFufQd7ooT5cAVQgUKaGr76WvRAUw

    #Message to send
    message = "Proxies report:"

    #Send the message to the specified Telegram channel or group
    send_telegram_message(bot_token, chat_id, message)

    #Report each proxy
    for proxy in proxies:
        proxy_report = f"Proxy: {proxy}"
        send_telegram_message(bot_token, chat_id, proxy_report)
        time.sleep(1)  # Add a delay to avoid spamming

if __name__ == "__main__":
    main()
