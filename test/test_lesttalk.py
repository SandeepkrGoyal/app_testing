from pages.letstalk import Letstalk
from utility.driverutility import Driverutility
import pytest


class Testtalk(Letstalk, Driverutility):
    @pytest.mark.debug
    def test_talk(self):
        url = super().parse_config("project_config", "site", "site_data2")
        headless_status = super().parse_config("project_config", "browser_config", "headless_status")

        driver = super().set_driver("chrome", headless_status)
        super().get_url(driver, url)

        super().validate_letstalk_button(driver)

        super().tear_down(driver)