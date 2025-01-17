# -*- coding: utf8 -*-
import requests
import datetime
import json
import os
import telebot
from dotenv import find_dotenv, load_dotenv

# Get variables
dotenv_file = find_dotenv()
load_dotenv(dotenv_file)
TOKEN = os.getenv('ACCESS_TOKEN')
PASSWORD = os.getenv('TEAMUP_PASSWORD')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
SUBCALENDAR = os.getenv('SUBCALENDAR')
ID = os.getenv('ID')
bot = telebot.TeleBot(token=TELEGRAM_TOKEN)

# Datetime +1 day
date_string = datetime.date.today()
date_string += datetime.timedelta(days=1)
date_string = date_string.strftime('%Y-%m-%d')

headers = {
    'Teamup-Token': TOKEN,
    'Teamup-Password': PASSWORD
}

def send_message(message):
    return bot.send_message(chat_id=CHAT_ID, text=message)

response = requests.get(f'https://api.teamup.com/{ID}/events?startDate={date_string}&endDate={date_string}&tz=Europe/Moscow', headers=headers)

if response.status_code == 200:
    obj = json.loads(response.text)
    if len(obj['events']) > 0:
        mess = 'Список встреч на завтра:\n'
        for i in obj['events']:
            if str(i['subcalendar_id']) == str(SUBCALENDAR) or str(SUBCALENDAR) == '1':
                dt = datetime.datetime.fromisoformat(i['start_dt'])
                mess += f'{i["title"]}: {str(dt.hour).zfill(2)}:{str(dt.minute).zfill(2)}\n'
        send_message(mess)
