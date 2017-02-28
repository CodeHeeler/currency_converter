import Currency from Currency
import DifferentCurrencyCodeError from Currency
import DifferentClassError from Currency


def UnknownCurrencyCodeError(ValueError):
    pass


class CurrencyConverter:
    def __init__(self, dict_rates):  # rates is a dict
        self.rates = dict_rates


    def convert(currency, code):
        if isinstance(currency, Currency):
            if code in self.rates:
                if currency.code == code:
                    return Currency(currency.amount, code)
                else:
                    return Currency(currency * (1 / self.rates[code]), code)
            else:
                raise UnknownCurrencyCodeError("Do not have the rate for that currency")
        else:
            raise DifferentClassError("Cannot convert something other than a Currency")
