#! /usr/bin/python3
import os, logging, time, websocket, json, hmac
from parameters import *
os.chdir('') # Put your working directory
from telegram import Bot # pip install python-telegram-bot --upgrade
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


bot=Bot(botToken)

def on_open(ws):
    ts = int(time.time() * 1000)
    login={'op': 'login', 'args': {
        'key': api,
        'sign': hmac.new(
            secret.encode(), f'{ts}websocket_login'.encode(), 'sha256').hexdigest(),
        'time': ts,
    }}

    ws.send(json.dumps(login))

    channel_data = {'op': 'subscribe', 'channel': 'fills'}
    ws.send(json.dumps(channel_data))


def on_message(ws,message):

    json_message=json.loads(message)
    try:

        data=json_message['data']

        price=data['price']
        size=data['size']
        side=data['side']
        market=data['market']
        fee=data['fee']
        liquidity=data['liquidity']
        bot.sendMessage(chatId, f"A {market} order got filled")
        bot.sendMessage(chatId,f"Market = {market} | Price = {price} | Size = {size} | Side = {side} | Liquidity = {liquidity} | Fee = {fee}")

    except:
        pass
