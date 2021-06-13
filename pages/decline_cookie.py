from utility.webutility import Webutility
from utility.assertutility import Assertutility
from time import sleep

class DeclineCookie(Webutility, Assertutility):

    def decline_cookie(self, driver):
        xpath_decline = super().parse_config("web_config", "links", "decline_cookie")
        web_element_decline_cookie = super().search_element(driver, "xpath", xpath_decline)
        super().click_element(web_element_decline_cookie)