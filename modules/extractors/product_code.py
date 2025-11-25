from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def extract_product_code(container):
    element_xpath = """
    //div[@id='br-pr-1']
    //*[contains(@class, 'br-pr-code-val')]
    """
    element = element_xpath.strip()

    if container is None:
        return None

    try:
        target = container.find_element(By.XPATH, element)
        text = target.get_attribute("textContent")

        return text.strip()

    except NoSuchElementException:
        print("Product code not found")
        return None
    except Exception as e:
        print(f"error: {e}")
        return None
