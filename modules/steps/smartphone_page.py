from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from extractors.name import extract_name
from extractors.color import extract_color


def parsing_data(driver):
    data = {}

    try:
        WebDriverWait(driver, 10).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        print("Smartphone Page loaded")
    except TimeoutException:
        print("DOM did not load in time")

    try:
        product_container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".br-body-product"))
        )
        print("Product page container found")
    except TimeoutException:
        print("Product page did not appear")
        product_container = None

    try:
        characteristics_container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".br-pr-chr"))
        )
        print("Characteristics container found")
    except TimeoutException:
        print("Characteristics container did not appear")
        characteristics_container = None

    data["name"] = extract_name(driver, product_container)
    data["color"] = extract_color(driver, characteristics_container)

    return data
