from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def extract_screen_diagonal(container):
    element_xpath = """
    //div[@class='br-pr-chr-item'][.//h3[text()='Дисплей']]
    //div/div[span[1][text()='Діагональ екрану']]/span[2]
    """
    element = element_xpath.strip()

    if container is None:
        return None

    try:
        target = container.find_element(By.XPATH, element)
        return target.text.strip()
    except NoSuchElementException:
        print("Screen diagonal not found")
        return None
    except Exception as e:
        print(f"error: {e}")
        return None
