from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest
import time

link_item = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
link_item_en = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                   marks=pytest.mark.xfail(reason="bugged")),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.click_the_add_to_basket_button()
    page.solve_quiz_and_get_code()
    page.check_that_the_item_added()
    page.check_that_the_price_is_correct()

@pytest.mark.success_message
@pytest.mark.xfail(reason="broken by design")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_item)
    page.open()
    page.click_the_add_to_basket_button()
    page.should_not_be_success_message()

@pytest.mark.success_message
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link_item)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.success_message
@pytest.mark.xfail(reason="broken by design")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link_item)
    page.open()
    page.click_the_add_to_basket_button()
    page.check_is_disappeared_success_message()

@pytest.mark.login
def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link_item_en)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
@pytest.mark.login
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link_item_en)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link_item_en)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_without_products()
    basket_page.basket_should_be_empty()

@pytest.mark.registered_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/accounts/login/")
        login_page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "Finalproject123"
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.click_the_add_to_basket_button()
        page.solve_quiz_and_get_code()
        page.check_that_the_item_added()
        page.check_that_the_price_is_correct()


    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, link_item)
        page.open()
        page.should_not_be_success_message()

