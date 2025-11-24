import random
import logging

from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException,
)

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def fill_search_input(driver, text):
    element_xpath = """
    //*[contains(@class, "header-bottom")]
    //*[contains(@class, "header-bottom-in")]
    //*[contains(@class, "quick-search-input")]
    """
    element = element_xpath.strip()

    wait = random.randint(18, 25)

    try:
        search_input_wait = WebDriverWait(driver, wait)
        search_input = search_input_wait.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    element,
                )
            )
        )
        search_input.send_keys(text)

    except (
        TimeoutException,
        NoSuchElementException,
        ElementClickInterceptedException,
    ) as e:
        logging.error(f"{e}")
