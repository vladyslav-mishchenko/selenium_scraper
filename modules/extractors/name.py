from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def extract_name(driver, product_container):
    element_xpath = """
    //*[contains(@class, 'main-right-block')]
    //*[contains(@class, 'desktop-only-title')]
    """
    element = element_xpath.strip()

    if product_container is None:
        return None

    try:
        target = product_container.find_element(By.XPATH, element)
        return target.text.strip()
    except NoSuchElementException:
        print("Product name not found")
        return None
    except Exception as e:
        print(f"extract_name error: {e}")
        return None
