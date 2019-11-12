
import pytest

from streamer import create_app


@pytest.fixture
def app(loop, aiohttp_client):
    app = create_app()
    return loop.run_until_complete(aiohttp_client(app))
