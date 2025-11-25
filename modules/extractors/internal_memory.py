from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def extract_internal_memory(container):
    element_xpath = """
    //div[@class='br-pr-chr-item'][.//h3[text()="Функції пам'яті"]]
    //div/div[span[1][text()="Вбудована пам'ять"]]/span[2]
    """
    element = element_xpath.strip()

    if container is None:
        return None

    try:
        target = container.find_element(By.XPATH, element)
        return target.text.strip()
    except NoSuchElementException:
        print("Internal memory not found")
        return None
    except Exception as e:
        print(f"error: {e}")
        return None
