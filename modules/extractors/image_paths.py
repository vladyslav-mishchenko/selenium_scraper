from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def extract_image_paths(container):
    element_xpath = """
    //div[@class='slick-track']
    //img[@class='br-main-img']
    """
    element = element_xpath.strip()

    if container is None:
        return None

    image_paths = []

    try:
        images = container.find_elements(By.XPATH, element)
        image_urls = [img.get_attribute("src") for img in images]

        for url in image_urls:
            image_paths.append(url)

        return image_paths
    except NoSuchElementException:
        print("Images not found")
        return None
    except Exception as e:
        print(f"error: {e}")
        return None
