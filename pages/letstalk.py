from utility.webutility import Webutility
from utility.assertutility import Assertutility


class Letstalk(Webutility, Assertutility):
    def validate_letstalk_button(self, driver):
        # Get xpath for button
        xpath_button = super().parse_config("web_config", "buttons", "letstalk")

        # Search element
        web_element_button = super().search_element(driver, "xpath", xpath_button)

        # CLick on the button
        super().click_element(web_element_button)

        # Get expected title
        expected_title = super().parse_config("web_data", "assert_data", "bookademo")
        actual_title = super().get_title(driver)

        # Put assertion to check for title of the page
        super().check_equals(actual_title, expected_title, "Actual and expected title did not match")