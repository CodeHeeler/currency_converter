import Currency from Currency
import DifferentCurrencyCodeError from Currency
import DifferentClassError from Currency


def UnknownCurrencyCodeError(ValueError):
    pass


class CurrencyConverter:
    def __init__(self, rates):
        self.rates = rates


    def convert(currency, code):
        if isinstance(currency, Currency):
            if code in self.rates:
                if currency.code == code:
                    return Currency(currency.amount, code)
                else:
                    return Currency(currency.__mul__(currency, 1 / rates(code)))
            else:
                raise UnknownCurrencyCodeError("Do not have the rate for that currency")
        else:
            raise DifferentClassError("Cannot convert something other than a Currency")
