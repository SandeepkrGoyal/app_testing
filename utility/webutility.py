import sys
from time import sleep

from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import InvalidElementStateException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utility.baseutility import Baseutility


class Webutility(Baseutility):
    def execute_javascript(self, driver, script):
        # Inject a javascript in the page DOM during runtime
        driver.execute_script(script)
        super().log_info("executing javascript " + script)

    def get_currenturl(self, driver):
        # Get the current url of the application where the control is present currently
        current_url = driver.current_url
        return current_url

    def get_networkrequests(self, driver):
        self.execute_javascript(driver, "return window.performance.getEntries();")
        super().log_info("collecting all network calls")

    def get_performancemetrics(self, driver):
        # Get all the performance metrics for all the requests for a particular web page within an application
        self.execute_javascript(driver, "return performance.timing")
        super().log_info("collecting performance metrics")

    def get_consolelogs(self, driver):
        # Get log will fetch all the required logs from the browser
        obj_consolelog = driver.get_log('browser')
        super().log_info("collecting console logs")
        return obj_consolelog

    def get_pagesource(self, driver):
        # Gets the page source of the html
        obj_pagesource = driver.page_source
        super().log_info("collecting page source")
        return obj_pagesource

    def get_sitecookies(self, driver):
        # This will give you all the cookies that the site is currently using
        cookies = driver.get_cookies()
        super().log_info("collecting all cookies")
        return cookies

    def set_explicitwaittime(self, sleeptime):
        # Set explicit wait time
        sleep(sleeptime)
        super().log_info("adding explicit wait time")

    def set_implicitwaittime(self, driver, sleeptime):
        # Implicit wait timing
        driver.implicitly_wait(sleeptime)
        super().log_info("adding implicit wait time")

    def get_url(self, driver, url):
        super().log_info("current url: " + url)
        driver.get(url)

    def get_title(self, driver):
        # This will get the title of the current page
        page_title = driver.title
        return page_title

    def get_text(self, element):
        # This will give me the text of a web element
        return element.text.strip()

    def search_element(self, driver, selector_type, selector):
        # Get the respective element based on the locator
        try:
            if selector_type == "xpath":
                super().log_info("Finding element with xpath: " + selector)
                return driver.find_element(By.XPATH, selector)
            if selector_type == "css":
                super().log_info("Finding element with css: " + selector)
                return driver.find_element(By.CSS_SELECTOR, selector)
            if selector_type == "id":
                super().log_info("Finding element with id: " + selector)
                return driver.find_element(By.ID, selector)
            if selector_type == "class_name":
                super().log_info("Finding element with class_name: " + selector)
                return driver.find_element(By.CLASS_NAME, selector)
            if selector_type == "link_text":
                super().log_info("Finding element with link_text: " + selector)
                return driver.find_element(By.LINK_TEXT, selector)
            if selector_type == "name":
                super().log_info("Finding element with name: " + selector)
                return driver.find_element(By.NAME, selector)
            if selector_type == "tag":
                super().log_info("Finding element with tag: " + selector)
                return driver.find_element_by_tag_name(selector)
            if selector_type not in ["xpath", "css", "id", "class_name", "link_text", "name", "tag"]:
                super().log_error("selector type not available")
        except NoSuchElementException:
            super().log_error("element not found " + selector)

    def search_elements(self, driver, selector_type, selector):
        # Get all the elements based on the locator
        try:
            if selector_type == "xpath":
                super().log_info("Finding elements with xpath: " + selector)
                return driver.find_elements(By.XPATH, selector)
            if selector_type == "css":
                super().log_info("Finding elements with css: " + selector)
                return driver.find_elements(By.CSS_SELECTOR, selector)
            if selector_type == "id":
                super().log_info("Finding element with id: " + selector)
                return driver.find_elements(By.ID, selector)
            if selector_type == "class_name":
                super().log_info("Finding element with class name: " + selector)
                return driver.find_elements(By.CLASS_NAME, selector)
            if selector_type == "link_text":
                super().log_info("Finding element with link text: " + selector)
                return driver.find_elements(By.LINK_TEXT, selector)
            if selector_type == "name":
                super().log_info("Finding element with name: " + selector)
                return driver.find_elements(By.NAME, selector)
            if selector_type == "tag":
                super().log_info("Finding element with tag: " + selector)
                return driver.find_elements_by_tag_name(selector)
            if selector_type not in ["xpath", "css", "id", "class_name", "link_text", "name", "tag"]:
                super().log_error("selector type not available")
        except NoSuchElementException:
            super().log_error("element not found " + selector)

    def input_data(self, element, input_data):
        # Enter the respective data in the input field
        # driver.find_element(By.XPATH, "xpath string").send_keys("data")
        element.send_keys(input_data)
        super().log_info("entering data for input field")

    def click_element(self, element):
        # Click on a particular element
        try:
            element.click()
            super().log_info("click on web element object")
        except ElementNotInteractableException:
            super().log_error("element is not interactable right now")
        except ElementClickInterceptedException:
            super().log_error("element is not clickable at point")

    def validate_element(self, element):
        flag = False
        if element:
            flag = True
        return flag

    def scroll_to_element(self, driver, element):
        driver.execute_script("arguments[0].scrollIntoView();", element)
        super().log_info("scrolling element into view")

    def scroll_down_to_pageend(self, driver):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        super().log_info("scrolling down to page end")

    def scroll_to_top_of_page(self, driver):
        element = driver.find_element_by_tag_name("html")
        element.send_keys(Keys.HOME)

    def wait_until_clickable(self, driver, selector_type, selector):
        try:
            if selector_type == "xpath":
                element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, selector)))
                super().log_info("clicking on element: " + selector)
                element.click()
            if selector_type == "css":
                element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
                super().log_info("clicking on element: " + selector)
                element.click()
            if selector_type == "id":
                element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, selector)))
                super().log_info("clicking on element: " + selector)
                element.click()
            if selector_type == "class_name":
                element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, selector)))
                super().log_info("clicking on element: " + selector)
                element.click()
            if selector_type == "link_text":
                element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, selector)))
                super().log_info("clicking on element: " + selector)
                element.click()
            if selector_type == "name":
                element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, selector)))
                super().log_info("clicking on element: " + selector)
                element.click()
            if selector_type not in ["xpath", "css", "id", "class_name", "link_text", "name", "tag"]:
                super().log_error("selector type not available")
        except NoSuchElementException:
            super().log_error("element not found for " + selector)
        except ElementClickInterceptedException:
            super().log_error("element is not clickable at point for " + selector)
        except InvalidElementStateException:
            super().log_error("invalid element state exception for " + selector)

    def get_url_definition(self, url):
        return url.rsplit("/", 1)[-1]

    def check_element_present(self, driver, selector_type, selector):
        try:
            if selector_type == "xpath":
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, selector)))
                super().log_info("element " + selector + " is found")
            if selector_type == "css":
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
                super().log_info("element " + selector + " is found")
            if selector_type == "id":
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, selector)))
                super().log_info("element " + selector + " is clickable")
            if selector_type == "class_name":
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, selector)))
                super().log_info("element " + selector + " is clickable")
            if selector_type == "link_text":
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, selector)))
                super().log_info("element " + selector + " is clickable")
            if selector_type == "name":
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, selector)))
                super().log_info("element " + selector + " is clickable")
        except WebDriverException:
            super().log_error("web driver exception for web element: " + selector)

    def clear_input(self, element):
        if sys.platform == "darwin":
            element.send_keys(Keys.COMMAND, 'a')
        else:
            element.send_keys(Keys.CONTROL, 'a')

        element.send_keys(Keys.BACKSPACE)

    def accept_alert(self, driver):
        try:
            # Wait condition to check for alert
            WebDriverWait(driver, 5).until(
                EC.alert_is_present(), 'Timed out waiting for PA creation ' + 'confirmation popup to appear.'
            )

            # Switch to alert context
            alert = driver.switch_to.alert
            super().log_info("Alert mesage: " + alert.text)
            # Accept alert
            alert.accept()
            super().log_info("Alert accepted")
        except TimeoutException:
            super().log_error("No alert present")