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


def click_form_submit(driver):
    element_xpath = """
    //*[contains(@class, "header-bottom")]
    //*[contains(@class, "header-bottom-in")]
    //*[contains(@class, "qsr-submit")]
    """
    element = element_xpath.strip()

    wait = random.randint(20, 30)

    try:
        search_submit_wait = WebDriverWait(driver, wait)
        search_submit = search_submit_wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    element,
                )
            )
        )
        search_submit.click()

    except (
        TimeoutException,
        NoSuchElementException,
        ElementClickInterceptedException,
    ) as e:
        logging.error(f"{e}")
