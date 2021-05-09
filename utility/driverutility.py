import platform  # To check for thhe current platform
import traceback

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options

from utility.baseutility import Baseutility


class Driverutility(Baseutility):
    def set_driver(self, browser, headless_status):
        driver = None
        try:
            if browser.lower() == "chrome":
                driver_path = None
                if platform.system().lower() == "darwin":
                    driver_path = super().parse_config("project_config", "browser_config", "driver_path_macos")
                if platform.system().lower() == "linux":
                    driver_path = super().parse_config("project_config", "browser_config", "driver_path_linux")
                if platform.system().lower() == "windows":
                    driver_path = super().parse_config("project_config", "browser_config", "driver_path_windows")
                if headless_status:
                    chrome_options = Options()
                    chrome_options.add_argument("--headless")
                    super().log_info("Set headless argument")
                    chrome_options.add_argument("--no-sandbox")
                    super().log_info("Deactivate sandbox")
                    chrome_options.add_argument('--disable-dev-shm-usage')
                    super().log_info("Deactivate shared virtual memory")
                    driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
                    driver.implicitly_wait(10)
                    super().log_info("Adding implicit wait time")
                    super().set_windowsize(driver, 1080, 1920)
                    super().log_info("Web driver initialized for " + browser)

                else:
                    super().log_info("Setting driver path to " + driver_path)
                    driver = webdriver.Chrome(executable_path=driver_path)
                    driver.implicitly_wait(10)
                    super().log_info("Adding implicit wait time")
                    driver.maximize_window()
                    super().log_info("Maximize window")
                    super().log_info("Web driver initialised for " + browser)

            if platform.system().lower() == "darwin" and browser.lower() == "safari":
                driver = webdriver.Safari()
                super().log_info("Web driver initialised for " + browser)
                driver.implicitly_wait(10)
                super().log_info("Adding implicit wait time")
                driver.maximize_window()
                super().log_info("Window maximised")

        except WebDriverException as e:
            super().log_error(e)
            traceback.print_exc()

        return driver

    def tear_down(self, driver):
        super().log_info("Tearing down web driver")
        driver.quit()
