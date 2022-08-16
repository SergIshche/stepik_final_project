from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def basket_without_products(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), \
            "Basket should be without items"

    def basket_should_be_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_CONTENT), \
            "Should be a message about empty basket"


