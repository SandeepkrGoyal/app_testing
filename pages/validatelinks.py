from pages.decline_cookie import DeclineCookie
from time import sleep


class Validatelinks(DeclineCookie):

    def validate_who_we_serve(self, driver):
        # To get xpath
        xpath_who_we_serve = super().parse_config("web_config", "links", "who-we-serve")
        xpath_enterprise = super().parse_config("web_config", "links", "enterprise")
        xpath_agency_partner = super().parse_config("web_config", "links", "agency_partner")
        xpath_smb = super().parse_config("web_config", "links", "smb")

        # Click element
        sleep(3)

        super().decline_cookie(driver)
        # search elements
        web_element_who_we_serve = super().search_element(driver, "xpath", xpath_who_we_serve)
        # Click element
        super().click_element(web_element_who_we_serve)

        web_element_enterprise = super().search_element(driver, "xpath", xpath_enterprise)
        super().click_element(web_element_enterprise)

        sleep(3)

        # Get actual page title
        enterprise_title = super().get_title(driver)
        # Get expected page title
        enterprise_expected_title = super().parse_config("web_data", "assert_data", "enterprise_page_title")
        super().check_equals(enterprise_title, enterprise_expected_title, "Actual and expected title did not match")
        sleep(3)

        # Validating Agency Partner
        super().click_element(web_element_who_we_serve)
        web_element_agency_partner = super().search_element(driver, "xpath", xpath_agency_partner)
        super().click_element(web_element_agency_partner)

        sleep(3)
        agency_partner_title = super().get_title(driver)
        agency_partner_expected_title = super().parse_config("web_data", "assert_data", "agency_partner_page_title")
        super().check_equals(agency_partner_title, agency_partner_expected_title, "Actual and expected title did not match")

        sleep(3)
        #Validating smb
        super().click_element(web_element_who_we_serve)
        web_element_smb = super().search_element(driver, "xpath", xpath_smb)
        super().click_element(web_element_smb)

        sleep(3)
        smb_title = super().get_title(driver)
        smb_expected_title = super().parse_config("web_data", "assert_data", "smb_page_title")
        super().check_equals(smb_title, smb_expected_title, "Actual and expected title did not match")
