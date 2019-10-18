from datetime import datetime
from random import Random
from typing import List


class QuoteGenerator:
    def __init__(self, symbols: List[str], seed: int = 0):
        self.symbol_list = symbols
        self.randomizer = Random(seed)
        self.iterate = True
        self.quotes = {symbol: 10.0 for symbol in self.symbol_list}

    def __iter__(self):
        return self

    def __next__(self):
        while self.iterate:
            symbol = self.randomizer.choice(self.symbol_list)
            self.quotes[symbol] *= self.randomizer.uniform(0.5, 1.5)
            return {symbol: float(f'{self.quotes[symbol]:.02f}'),
                    "timestamp": datetime.utcnow().timestamp()}