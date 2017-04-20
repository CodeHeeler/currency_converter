class DifferentCurrencyCodeError(AttributeError):
    pass


class DifferentClassError(ValueError):
    pass


class Currency:
    def __init__(self, amount, code=''):
        if code == "":
            self.code = amount[0]
            self.amount = float(amount[1:])
        else:
            self.amount = float(amount)

            if code == "USD" or code == "$":
                self.code = "$"
            elif code == "EUR" or code == "€":
                self.code = "€"
            elif code == "JAP" or code == "¥":
                self.code = "¥"




    def __eq__(self, other):
        return self.code == other.code and self.amount == other.amount


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

    def __repr__(self):
        return "{}{}".format(self.code, self.amount)

    def __str__(self):
        return "{}{}".format(self.code, self.amount)
        
