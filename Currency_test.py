from Currency import Currency


five_dollars = Currency("$5")
my_money = Currency("5", "USD")

def test_print():
    assert str(five_dollars) == "$5.0"

def test_is_equal():
    assert my_money == five_dollars


test_print()
test_is_equal()
