from aiohttp import web

from quote_generator import SHARE_SYMBOLS, QuoteGenerator
from .streamer import stream_handler, root_handler


__version__ = "1.0"


def create_app():
    app = web.Application()
    app.router.add_route("GET", "/quotes", stream_handler)
    app.router.add_route("GET", "/", root_handler)

    app['GENERATOR'] = QuoteGenerator(SHARE_SYMBOLS, seed=1)

    return app
