from Currency import Currency, DifferentCurrencyCodeError, DifferentClassError


def UnknownCurrencyCodeError(ValueError):
    pass


class CurrencyConverter:
    def __init__(self, dict_rates):  # rates is a dict
        self.rates = dict_rates


    def convert(self, currency, code):
        if isinstance(currency, Currency):
            if code in self.rates:
                if currency.code == code:
                    return Currency(currency.amount, code)
                else:
                    return Currency(currency.amount * (self.rates[code] / self.rates[currency.code]), code)
            else:
                raise UnknownCurrencyCodeError("Do not have the rate for that currency")
        else:
            raise DifferentClassError("Cannot convert something other than a Currency")
