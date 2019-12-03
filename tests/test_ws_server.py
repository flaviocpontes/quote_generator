from aiohttp import web
import pytest

from streamer import create_app


@pytest.fixture
async def test_client(aiohttp_client, loop):
    app = create_app()
    return await aiohttp_client(app)


@pytest.mark.freeze_time('2017-05-21')
async def test_get_one_quote_from_ws(test_client):
    msg_data = None
    async with test_client.ws_connect('/quotes') as ws:
        assert await ws.receive_json() == {"B3SA3": 10.25, "timestamp": 1495335600.0}
        await ws.close()


async def receive_next_quote(ws):
    data = await ws.receive_json()
    await ws.send_str("")
    return data


@pytest.mark.freeze_time('2017-05-21')
async def test_get_multiple_quotes_from_ws(test_client):
    msg_data = None
    async with test_client.ws_connect('/quotes') as ws:
        assert await receive_next_quote(ws) == {"B3SA3": 10.25, "timestamp": 1495335600.0}
        assert await receive_next_quote(ws) == {'BBDC4': 9.56, 'timestamp': 1495335600.0}
        assert await receive_next_quote(ws) == {'RADL3': 10.67, 'timestamp': 1495335600.0}
        assert await receive_next_quote(ws) == {'SUZB3': 10.43, 'timestamp': 1495335600.0}
        assert await receive_next_quote(ws) == {'BRFS3': 9.21, 'timestamp': 1495335600.0}
        assert await receive_next_quote(ws) == {'VALE3': 10.97, 'timestamp': 1495335600.0}
        assert await receive_next_quote(ws) == {'MRFG3': 9.95, 'timestamp': 1495335600.0}
        assert await receive_next_quote(ws) == {'PETR4': 10.53, 'timestamp': 1495335600.0}
        assert await receive_next_quote(ws) == {'GOLL4': 10.59, 'timestamp': 1495335600.0}
