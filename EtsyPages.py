import time

from selenium.webdriver.common.keys import Keys

from BaseApp import BasePage
from selenium.webdriver.common.by import By


class HomePage:
    Search_field = (By.ID, 'global-enhancements-search-query')
    Context_menu_Home_and_Living = (By.ID, 'catnav-primary-link-891')
    Pet_Supplies = (By.ID, 'side-nav-category-link-4440')
    Pet_Hats_and_Wigs = (By.ID, 'catnav-l4-12065')


class SearchPage:
    Filters_button = (By.ID, 'search-filter-button')
    Price_button = (By.CLASS_NAME, 'wt-menu wt-display-block wt-action-group__item-container')
    Price_checkbox_75_150 = (
        By.XPATH, "//body/div[@id='wt-modal-container']/div[@id='search-filters-overlay']/div[1]/div[3]/form[1]/div[4]/fieldset[1]/div[1]/div[1]/div[3]/a[1]/span[1]")
    Color_Pink_button = (By.XPATH, "//span[contains(text(),'Pink')]")
    Shipping_Method_Free = (By.XPATH, "//body/div[@id='wt-modal-container']/div[@id='search-filters-overlay']/div[1]/div[3]/form[1]/div[2]/fieldset[1]/div[1]/div[1]/div[1]/div[1]/a[1]/span[1]")
    Bar_with_filters = (By.XPATH, "//body/div[@id='content']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/ul[1]")
    Created_filter_FREE_shipping = (By.PARTIAL_LINK_TEXT, "FREE shippi")
    Button_with_price = (By.XPATH, "//span[contains(text(),'₪75 – ₪150')]")


class SearchHelper(BasePage):

    def find_something(self, word):
        search_field = self.find_element(HomePage.Search_field)
        search_field.click()
        search_field.send_keys(word)
        search_field.send_keys(Keys.ENTER)
        time.sleep(2)
        return search_field

    def open_filters(self):
        open_filters = self.find_element(SearchPage.Filters_button)
        open_filters.click()

    def use_price_change(self, word):
        self.open_filters()
        if word == "75-150":
            price = self.find_element(SearchPage.Price_checkbox_75_150)
            price.click()
        time.sleep(2)

    def use_color_change(self, word):
        self.open_filters()
        if word == "Pink":
            color = self.find_element(SearchPage.Color_Pink_button)
            color.click()
        time.sleep(2)

    def use_shipping_methods(self, word):
        self.open_filters()
        if word == "FREE shipping":
            method = self.find_element(SearchPage.Shipping_Method_Free)
            method.click()
        time.sleep(2)

    def verifi_price(self):
        return self.find_element(SearchPage.Button_with_price)

    def verifi_new_filter_FREE_shiping(self):
        return self.find_element(SearchPage.Created_filter_FREE_shipping)

    def verifi_saved_request(self):
        return self.find_element(HomePage.Search_field).get_attribute('value')