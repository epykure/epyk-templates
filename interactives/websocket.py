# https://websockets.readthedocs.io/en/stable/intro.html

# WSS (WS over TLS) server example, with a self-signed certificate

import asyncio
import pathlib
import ssl
import websockets

import datetime
import random


async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")


async def time(websocket, path):
  while True:
    now = datetime.datetime.utcnow().isoformat() + "Z"
    await websocket.send(now)
    await asyncio.sleep(random.random() * 3)

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
localhost_pem = pathlib.Path(__file__).with_name("localhost.pem")


start_server = websockets.serve(
  hello, "localhost", 8765
)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()