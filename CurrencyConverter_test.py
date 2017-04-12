from CurrencyConverter import CurrencyConverter
from Currency import *


rates = {'USD': 1.0, 'EUR': 0.5, 'JAP': 2}
currency_converter = CurrencyConverter(rates)


def test_converter_same():
    assert currency_converter.convert(Currency(1, 'USD'), 'USD') == Currency(1, 'USD')


def test_converter_different():
    assert currency_converter.convert(Currency(1, 'USD'), 'EUR') == Currency(2, "EUR")


test_converter_same()
test_converter_different()
