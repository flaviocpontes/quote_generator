from aiohttp import web

from quote_generator import SHARE_SYMBOLS, QuoteGenerator
from .streamer import stream_handler

__version__ = "1.1"


def create_app(max_value: float = 150.00, min_value: float = 5.00, update_interval: float = 0.1):
    app = web.Application()
    app.router.add_route("GET", "/quotes", stream_handler)

    app['GENERATOR'] = QuoteGenerator(SHARE_SYMBOLS, seed=1)
    app['MIN_VALUE'] = min_value
    app['MAX_VALUE'] = max_value
    app['UPDATE_INTERVAL'] = update_interval

    return app
