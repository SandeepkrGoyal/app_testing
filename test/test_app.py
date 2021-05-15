from utility.driverutility import Driverutility
import pytest


class Testapp(Driverutility):
    @pytest.mark.regression
    def test_amazon(self):
        headless_status = super().parse_config("project_config", "browser_config", "headless_status")
        driver = super().set_driver("chrome", headless_status)
        driver.get("https://www.amazon.in/")
        get_title = driver.title
        print(get_title)
        assert get_title == "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in", "Title does not match"
        super().tear_down(driver)

    @pytest.mark.regression
    def test_youtube(self):
        headless_status = super().parse_config("project_config", "browser_config", "headless_status")
        driver = super().set_driver("chrome", headless_status)
        driver.get("https://www.youtube.com/")
        get_title = driver.title
        print(get_title)
        assert get_title == "YouTube", "Title does not match"
        super().tear_down(driver)

    @pytest.mark.debug
    def test_google(self):
        headless_status = super().parse_config("project_config", "browser_config", "headless_status")
        driver = super().set_driver("chrome", headless_status)
        driver.get("https://www.google.com/")
        get_title = driver.title
        print(get_title)
        assert get_title == "Google"
        super().tear_down(driver)

    @pytest.mark.sanity
    def test_facebook(self):
        headless_status = super().parse_config("project_config", "browser_config", "headless_status")
        driver = super().set_driver("chrome", headless_status)
        driver.get("https://www.facebook.com/")
        get_title = driver.title
        print(get_title)
        assert get_title == "Facebook – log in or sign up"
        super().tear_down(driver)

    # def test_safari(self):
    #     headless_status = super().parse_config("project_config", "browser_config", "headless_status")
    #     driver = super().set_driver("safari", headless_status)
    #     driver.get("https://www.amazon.in/")
    #     get_title = driver.title
    #     print(get_title)
    #     assert get_title == "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in", "Title does not match"
    #     super().tear_down(driver)
    #
    # def test_chrome_headless(self):
    #     headless_status = super().parse_config("project_config", "browser_config", "headless_status")
    #     driver = super().set_driver("chrome", headless_status)
    #     driver.get("https://www.amazon.in/")
    #     get_title = driver.title
    #     print(get_title)
    #     assert get_title == "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in", "Title does not match"
    #     super().tear_down(driver)