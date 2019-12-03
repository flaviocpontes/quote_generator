from quote_generator import QuoteGenerator, SHARE_SYMBOLS


def test_one_symbol_generator():
    q = QuoteGenerator(["PETR4"], min_value=0, max_value=150, seed=1)
    assert next(q)["PETR4"] == 10.34


def test_two_symbols_generator():
    q = QuoteGenerator(["PETR4", "VALE3"], min_value=0, max_value=150, seed=2)
    assert next(q)["PETR4"] == 9.37
    assert next(q)["VALE3"] == 10.88


def test_many_symbols_generator():
    q = QuoteGenerator(SHARE_SYMBOLS, min_value=0, max_value=150, seed=1)
    assert next(q)['B3SA3'] == 10.34
    assert next(q)['BBDC4'] == 9.7
    assert next(q)['RADL3'] == 10.73
    assert next(q)['SUZB3'] == 10.51
    assert next(q)['BRFS3'] == 9.37
    assert next(q)['VALE3'] == 11.0
    assert next(q)['MRFG3'] == 10.06
    assert next(q)['PETR4'] == 10.6
    assert next(q)['GOLL4'] == 10.65
    assert next(q)['KROT3'] == 10.39
    assert next(q)['ABEV3'] == 11.02
    assert next(q)['VALE3'] == 10.15


def test_value_never_exceeds_max_value():
    MAX_VALUE = 11
    q = QuoteGenerator(SHARE_SYMBOLS, min_value=0, max_value=MAX_VALUE, seed=1)
    for i in range(10000):
        assert tuple(next(q).values())[0] <= MAX_VALUE, f'Failed in iteration {i}'


def test_value_never_exceeds_min_value():
    MIN_VALUE = 8
    q = QuoteGenerator(SHARE_SYMBOLS, min_value=MIN_VALUE, max_value=150, seed=1)
    for i in range(10000):
        assert tuple(next(q).values())[0] >= MIN_VALUE, f'Failed in iteration {i}'
