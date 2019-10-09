from quote_generator import QuoteGenerator, SHARE_SYMBOLS


def test_one_symbol_generator():
    q = QuoteGenerator(["PETR4"], seed=1)
    assert next(q) == {"PETR4": 10.69}


def test_two_symbols_generator():
    q = QuoteGenerator(["PETR4", "VALE3"], seed=2)
    assert next(q) == {'PETR4': 5.92}
    assert next(q) == {'VALE3': 13.35}


def test_many_symbols_generator():
    q = QuoteGenerator(SHARE_SYMBOLS, seed=1)
    assert next(q) == {'B3SA3': 10.69}
    assert next(q) == {'BBDC4': 7.55}
    assert next(q) == {'RADL3': 12.61}
    assert next(q) == {'SUZB3': 11.52}
    assert next(q) == {'BRFS3': 5.94}
    assert next(q) == {'VALE3': 13.93}
    assert next(q) == {'MRFG3': 9.33}
    assert next(q) == {'PETR4': 11.96}
    assert next(q) == {'GOLL4': 12.22}
    assert next(q) == {'KROT3': 10.91}
    assert next(q) == {'ABEV3': 14.01}
    assert next(q) == {'VALE3': 7.28}
