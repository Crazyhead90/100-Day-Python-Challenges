from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "F:\SynologyDrive\Drive 2\Python\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.amazon.nl/-/en/gp/product/B083KM6BZS/ref=ewc_pr_img_1?smid=AE9XWIQL6Y1PP")
# price = driver.find_element(by=By.CLASS_NAME, value="a-offscreen").get_attribute("textContent")
# print(price)

driver.get("https://www.python.org/")
event_date = driver.find_elements(by=By.CSS_SELECTOR, value='.event-widget time')
event_title = driver.find_elements(by=By.CSS_SELECTOR, value='.event-widget li a')
events = {}

for n in range(len(event_date)):
    events[n] = {
        "time": event_date[n].text,
        "name": event_title[n].text,
    }

print(events)

driver.quit()
