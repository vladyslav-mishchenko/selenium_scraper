from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def extract_discounted_price(driver, container):
    element_xpath = """
    //div[contains(@class, 'main-price-block')]
    //div[contains(@class, 'br-pr-op')]
    """
    element = element_xpath.strip()

    if container is None:
        return None

    try:
        target = container.find_element(By.XPATH, element)
        value = target.text.strip()
        return value
    except NoSuchElementException:
        print("Discounted price not found")
        return None
    except Exception as e:
        print(f"error: {e}")
        return None
