from aiohttp import web
from asyncio import sleep


async def stream_handler(request):
    generator = request.app['GENERATOR']
    update_interval = request.app['UPDATE_INTERVAL']

    ws = web.WebSocketResponse()
    await ws.prepare(request)
    print(f'Connection from {request.host}', flush=True)

    maintain_connection = True
    while maintain_connection:
        msg = next(generator)
        await ws.send_json(msg)
        await sleep(update_interval)

        try:
            resp = await ws.receive(timeout=update_interval / 2)
            if resp and resp.type == web.WSMsgType.CLOSE:
                maintain_connection = False
        except Exception as e:
            print(e)

    await ws.close()
