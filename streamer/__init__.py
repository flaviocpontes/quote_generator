from aiohttp import web

from quote_generator import SHARE_SYMBOLS, QuoteGenerator
from .streamer import stream_handler


__version__ = "1.1"


def create_app():
    app = web.Application()
    app.router.add_route("GET", "/quotes", stream_handler)

    app['GENERATOR'] = QuoteGenerator(SHARE_SYMBOLS, seed=1)

    return app
