from Currency import Currency


five_dollars = Currency("$5")
my_money = Currency("5", "USD")

def test_print():
    assert print(five_dollars) == "$5"

def test_is_equal():
    assert (my_money == five_dollars) == True


test_print()
test_is_equal()
