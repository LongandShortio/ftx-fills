#! /usr/bin/python3
import os
os.chdir("") # Put your working directory
from tgFills import *

if __name__ == '__main__':
    ws= websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message)
    ws.run_forever()
