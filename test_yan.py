from EtsyPages import SearchHelper


def test_etsy_TC1(browser):
    user = SearchHelper(browser)
    user.go_to_site()
    user.find_something("Candy")
    user.use_color_change("Pink")
    user.use_price_change("75-150")
    user.use_shipping_methods("FREE shipping")
    assert user.verifi_price()
    assert user.verifi_new_filter_FREE_shiping()
    assert user.verifi_saved_request() == "Candy"


