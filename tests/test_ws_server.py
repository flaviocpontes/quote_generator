import pytest

from streamer import create_app


@pytest.fixture
def app(loop, aiohttp_client):
    app = create_app()
    return loop.run_until_complete(aiohttp_client(app))


async def test_can_connect_to_server(app):
    resp = await app.get("/")
    assert resp.status == 200
    assert await resp.text() == "Hello World!"



