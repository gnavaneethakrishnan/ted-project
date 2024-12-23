from money import Money

class Bank:
    def __init__(self) -> None:
        self.exchange_rates = {}

    def add_exchange_rate(self, from_currency, to_currency, rate):
        key = f"{from_currency}->{to_currency}"
        self.exchange_rates[key] = rate

    def convert(self, aMoney, aCurrency):
        if aMoney.currency == aCurrency:
            return Money(aMoney.amount, aCurrency)
        
        key = f"{aMoney.currency}->{aCurrency}"
        
        if key in self.exchange_rates:
            return Money(aMoney.amount * self.exchange_rates[key], aCurrency)
        raise Exception(key)
    