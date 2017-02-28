class DifferentCurrencyCodeError(AttributeError):
    pass


class DifferentClassError(ValueError):
    pass


class Currency:
    def __init__(self, amount, code=''):
        if code == "":
            self.code = amount(0)
            self.amount = float(amount(1:))
        else:
            self.code = code
            self.amount = amount


    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.code == other.code and self.amount == other.amount
        else:
            return False


    def __ne__(self, other):
        return not self.__eq__(other)


    def __add__(self, other):
        if isinstance(other, self.__class__):
            if self.code == other.code:
                return Currency(self.code, self.amount + other.amount)
            else:
                raise DifferentCurrencyCodeError("Codes don't match in add")
        else:
            raise DifferentClassError("Cannot compare different classes in add")

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            if self.code == other.code:
                return Currency(self.code, self.amount - other.amount)
            else:
                raise DifferentCurrencyCodeError("Codes don't match in subtract")
        else:
            raise DifferentClassError("Cannot compare different classes in subtract")


    def __mul__(self, multiplier):
        if type(multiplier) == int or type(multiplier) == float:
        # test type of multiplier to be int or float
        # raise DifferentClassError
            return Currency(self.code, self.amount * multiplier)
        else:
            raise DifferentClassError("Cannot multiply by a non-number")

    def __str__(self):
        if self.code == "USD":
            print("${}".format(self.amount))
        elif self.code == "EUR":
            print("€{}".format(self.amount))
        elif self.code == "JAP":
            print("¥{}".format(self.amount))
