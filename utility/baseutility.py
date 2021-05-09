import json
import logging


class Baseutility:
    # To display log information
    def log_info(self, informationmesssage):
        logging.info(informationmesssage)

    # To display log error
    def log_error(self, errormessage):
        logging.error(errormessage)

    # Logging for debugging
    def log_debug(self, debugmessage):
        logging.debug(debugmessage)

    # Logging for waring
    def log_warning(self, warningmessage):
        logging.warning(warningmessage)

    # Logging for critical
    def log_critical(self, criticalmessage):
        logging.critical(criticalmessage)

    # To set window size
    def set_windowsize(self, driver, height, width):
        window_height = int(height)
        window_width = int(width)
        self.log_info("Setting window size to " + str(window_width) + "*" + str(window_height))
        driver.set_window_size(window_height, window_width)

    def parse_config(self, config_type, parent_datatype, child_datatype):
        try:
            json_obj = ""
            config_path = "configurations/"
            if config_type == "project_config":
                json_config_path = config_path + "projectconfig.json"
                with open(json_config_path, "r") as jsonobj:
                    jsondata = json.load(jsonobj)
                    json_obj = jsondata.get(parent_datatype).get(child_datatype)
            return json_obj
        except KeyError as e:
            self.log_error(e)
