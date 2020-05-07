def hydrate(drink_string):
    # your code here
    pass


@test.describe('Example Tests')
def example_tests():
    test.assert_equals(hydrate("1 beer"), "1 glass of water")
    test.assert_equals(hydrate(
        "1 shot, 5 beers, 2 shots, 1 glass of wine, 1 beer"), "10 glasses of water")
