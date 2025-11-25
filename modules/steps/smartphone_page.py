from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from extractors.name import extract_name
from extractors.color import extract_color
from extractors.internal_memory import extract_internal_memory
from extractors.price import extract_price
from extractors.discounted_price import extract_discounted_price
from extractors.image_paths import extract_image_paths
from extractors.product_code import extract_product_code
from extractors.reviews import extract_reviews
from extractors.screen_diagonal import extract_screen_diagonal
from extractors.display_resolution import extract_display_resolution
from extractors.characteristics import extract_characteristics
from extractors.manufacturer import extract_manufacturer
from extractors.series import extract_series


def parsing_data(driver):
    data = {}

    # wait until dom loaded
    try:
        WebDriverWait(driver, 20).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        print("Smartphone Page loaded")
    except TimeoutException:
        print("DOM did not load in time")

    # product page container
    try:
        product_container = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".br-body-product"))
        )
        print("Product page container found")
    except TimeoutException:
        print("Product page did not appear")
        product_container = None

    # characteristics container
    try:
        characteristics_container = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".br-pr-chr"))
        )
        print("Characteristics container found")
    except TimeoutException:
        print("Characteristics container did not appear")
        characteristics_container = None

    # open characteristics
    try:
        open = WebDriverWait(driver, 25).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#br-characteristics .br-prs-button")
            )
        )
        open.click()

        print("Characteristics opened")
    except TimeoutException:
        print("Characteristics not open")
        characteristics_container = None

    data["name"] = extract_name(product_container)
    data["price"] = extract_price(product_container)
    data["discounted_price"] = extract_discounted_price(product_container)
    data["reviews"] = extract_reviews(product_container)
    data["image_paths"] = extract_image_paths(product_container)
    data["product_code"] = extract_product_code(product_container)
    data["characteristics"] = extract_characteristics(characteristics_container)
    data["color"] = extract_color(characteristics_container)
    data["internal_memory"] = extract_internal_memory(characteristics_container)
    data["screen_diagonal"] = extract_screen_diagonal(characteristics_container)
    data["display_resolution"] = extract_display_resolution(characteristics_container)
    data["manufacturer"] = extract_manufacturer(characteristics_container)
    data["series"] = extract_series(characteristics_container)

    return data
