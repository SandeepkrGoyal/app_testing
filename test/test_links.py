from pages.validatelinks import Validatelinks
from utility.driverutility import Driverutility


class Testlinks(Validatelinks, Driverutility):
    def test_link1(self):
        url = super().parse_config("project_config", "site", "site_data2")
        headless_status = super().parse_config("project_config", "browser_config", "headless_status")

        driver = super().set_driver("chrome", headless_status)
        super().get_url(driver, url)

        super().validate_who_we_serve(driver)

        super().tear_down(driver)