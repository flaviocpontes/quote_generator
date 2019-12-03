from collections import namedtuple
from datetime import datetime
from random import Random
from typing import List

GROW_TREND = 1.12

SHRINK_TREND = .9


class Quote:
    value = None
    trend = None

    def __init__(self, value, trend):
        self.value = value
        self.trend = trend


class QuoteGenerator:
    def __init__(self, symbols: List[str], min_value: float, max_value: float, seed: int = 0, trend: float = 1.02):
        self.symbol_list = symbols
        self.randomizer = Random(seed)
        self.iterate = True
        self.min_value = min_value
        self.max_value = max_value
        self.quotes = {symbol: Quote(10.0, trend) for symbol in self.symbol_list}

    def __iter__(self):
        return self

    def __next__(self):
        while self.iterate:
            symbol = self.randomizer.choice(self.symbol_list)

            value = self.quotes[symbol].value * self.randomizer.uniform(0.9, 1.1) * self.quotes[symbol].trend
            if value >= self.max_value:
                self.quotes[symbol].trend = SHRINK_TREND
                value = self.quotes[symbol].value * self.randomizer.uniform(0.9, 1.1) * self.quotes[symbol].trend
            if value <= self.min_value:
                self.quotes[symbol].trend = GROW_TREND
                value = self.quotes[symbol].value * self.randomizer.uniform(0.9, 1.1) * self.quotes[symbol].trend

            self.quotes[symbol].value = value

            return {symbol: float(f'{self.quotes[symbol].value:.02f}'),
                    "timestamp": datetime.utcnow().timestamp()}
