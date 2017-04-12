class DifferentCurrencyCodeError(AttributeError):
    pass


class DifferentClassError(ValueError):
    pass


class Currency:
    def __init__(self, amount, code=''):
        if code == "":
            self.code = amount[0]
            if isinstance(amount[1:], int):
                self.amount = int(amount[1:])
            else:
                self.amount = float(amount[1:])
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
                return Currency(self.amount + other.amount, self.code)
            else:
                raise DifferentCurrencyCodeError("Codes don't match in add")
        else:
            raise DifferentClassError("Cannot compare different classes in add")

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            if self.code == other.code:
                return Currency(self.amount - other.amount, self.code)
            else:
                raise DifferentCurrencyCodeError("Codes don't match in subtract")
        else:
            raise DifferentClassError("Cannot compare different classes in subtract")


    def __mul__(self, multiplier):
        if type(multiplier) == int or type(multiplier) == float:
        # test type of multiplier to be int or float
        # raise DifferentClassError
            return Currency(self.amount * multiplier, self.code)
        else:
            raise DifferentClassError("Cannot multiply by a non-number")

    def __str__(self):
        if self.code == "USD" or self.code == "$":
            return ("$" + str(self.amount))
            # print("${}".format(self.amount))
        elif self.code == "EUR":
            return ("€" + str(self.amount))
            # print("€{}".format(self.amount))
        elif self.code == "JAP":
            return ("¥" + str(self.amount))
            # print("¥{}".format(self.amount))
