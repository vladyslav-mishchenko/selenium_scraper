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


def open_search_results(driver):
    element_xpath = """
    (
    //*[contains(@class, "tab-content")]
    //*[contains(@class, "view-grid")]
    //*[contains(@class, "product-wrapper")]
    //*[contains(@class, "br-pp-desc")]
    //a
    )[1]
    """
    element = element_xpath.strip()

    wait = random.randint(17, 25)

    try:
        search_result_1_wait = WebDriverWait(driver, wait)
        search_result_1 = search_result_1_wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    element,
                )
            )
        )
        search_result_1.click()

    except (
        TimeoutException,
        NoSuchElementException,
        ElementClickInterceptedException,
    ) as e:
        logging.error(f"{e}")
