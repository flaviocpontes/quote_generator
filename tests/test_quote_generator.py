from quote_generator import QuoteGenerator, SHARE_SYMBOLS


def test_one_symbol_generator():
    q = QuoteGenerator(["PETR4"], seed=1)
    assert next(q)["PETR4"] == 10.25


def test_two_symbols_generator():
    q = QuoteGenerator(["PETR4", "VALE3"], seed=2)
    assert next(q)["PETR4"] == 9.2
    assert next(q)["VALE3"] == 10.84


def test_many_symbols_generator():
    q = QuoteGenerator(SHARE_SYMBOLS, seed=1)
    assert next(q)['B3SA3'] == 10.25
    assert next(q)['BBDC4'] == 9.56
    assert next(q)['RADL3'] == 10.67
    assert next(q)['SUZB3'] == 10.43
    assert next(q)['BRFS3'] == 9.21
    assert next(q)['VALE3'] == 10.97
    assert next(q)['MRFG3'] == 9.95
    assert next(q)['PETR4'] == 10.53
    assert next(q)['GOLL4'] == 10.59
    assert next(q)['KROT3'] == 10.3
    assert next(q)['ABEV3'] == 10.98
    assert next(q)['VALE3'] == 9.92
