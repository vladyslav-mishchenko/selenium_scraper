from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from steps.home_page import open_home_page
from steps.search_form_input import fill_search_input
from steps.search_form_submit import click_form_submit
from steps.search_results_page import open_search_results
from steps.smartphone_page import parsing_data

url = "https://www.brain.com.ua/"

# driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# step:1 - homepage
open_home_page(driver, url)

# step:2 - search input
search_text = "Apple iPhone 15 128GB Black"
# search_text = "Мобільний телефон Xiaomi Redmi Note 14 8/256GB Midnight Black"
fill_search_input(driver, search_text)

# step:3 - submit search form
click_form_submit(driver)

# step:4 - click on first search result link
open_search_results(driver)

# step:5 - parsing data
data = parsing_data(driver)
print(data)

input("Press Enter to close the browser...")

driver.quit()
