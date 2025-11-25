from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def extract_name(container):
    element_xpath = """
    //*[contains(@class, 'main-right-block')]
    //*[contains(@class, 'desktop-only-title')]
    """
    element = element_xpath.strip()

    if container is None:
        return None

    try:
        target = container.find_element(By.XPATH, element)
        value = target.text.strip()
        return value
    except NoSuchElementException:
        print("Product name not found")
        return None
    except Exception as e:
        print(f"error: {e}")
        return None
