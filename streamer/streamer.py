from aiohttp import web
from asyncio import sleep


async def stream_handler(request):
    generator = request.app['GENERATOR']
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    print(f'Connection from {request.host}')

    while True:
        msg = next(generator)
        await ws.send_json(next(generator))
        await sleep(.1)


async def root_handler(request):
    return web.Response(text="Hello World!")