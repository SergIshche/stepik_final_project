from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def click_the_add_to_basket_button(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        button.click()

    def check_that_the_item_added(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == \
               self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED).text, \
            "The message about added prodcut is wrong"

    def check_that_the_price_is_correct(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text in \
               self.browser.find_element(*ProductPageLocators.TOTAL_PRICE_MESSAGE).text, \
            "The price of added product is wrong"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def check_is_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"
