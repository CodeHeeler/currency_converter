from Currency import Currency, DifferentCurrencyCodeError, DifferentClassError


def UnknownCurrencyCodeError(ValueError):
    pass


class CurrencyConverter:
    def __init__(self, dict_rates):  # rates is a dict
        self.rates = dict_rates


    def convert(self, currency, code):
        # code_dict = {"USD": "$", "EUR": "€", "JAP": "¥"}
        if isinstance(currency, Currency):
            if code in self.rates:
                # if code in list(code_dict.keys()):
                #     code = code_dict[code]
                abrev = ""
                if currency.code == "$":
                    abrev = "USD"
                elif currency.code == "€":
                    abrev = "EUR"
                elif currency.code == "¥":
                    abrev = "JAP"
                if abrev == code:
                    return Currency(currency.amount, code)
                else:
                    return Currency(currency.amount * (self.rates[code] / self.rates[abrev]), code)
            else:
                raise UnknownCurrencyCodeError("Do not have the rate for that currency")
        else:
            raise DifferentClassError("Cannot convert something other than a Currency")
