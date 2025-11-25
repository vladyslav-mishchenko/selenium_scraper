from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def extract_characteristics(container):
    characteristics = {}

    if container is None:
        return None

    try:
        items = container.find_elements(By.XPATH, ".//div[@class='br-pr-chr-item']")

        for item in items:
            category = item.find_element(By.XPATH, ".//h3")
            category_title = category.text.strip()

            characteristic = {}

            rows = category.find_elements(By.XPATH, "./following-sibling::div/div")
            for row in rows:
                title = row.find_element(By.XPATH, ".//span[1]").text.strip()
                value = row.find_element(By.XPATH, ".//span[2]").text.strip()
                characteristic[title] = value

            characteristics[category_title] = characteristic

        return characteristics
    except NoSuchElementException:
        print("Product name not found")
        return None
    except Exception as e:
        print(f"extract_name error: {e}")
        return None
