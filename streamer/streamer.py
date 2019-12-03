from aiohttp import web
from asyncio import sleep


async def stream_handler(request):
    generator = request.app['GENERATOR']
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    print(f'Connection from {request.host}', flush=True)

    maintain_connection = True
    while maintain_connection:
        msg = next(generator)
        await ws.send_json(msg)
        await sleep(.1)

        resp = await ws.receive(timeout=0.1)
        if resp and resp.type == web.WSMsgType.CLOSE:
            maintain_connection = False

    await ws.close()