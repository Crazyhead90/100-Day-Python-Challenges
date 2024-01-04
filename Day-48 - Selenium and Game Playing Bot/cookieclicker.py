from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url = "http://orteil.dashnet.org/experiments/cookie/"

chrome_driver_path = "F:\SynologyDrive\Drive 2\Python\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url)

cookie = driver.find_element(By.ID, "cookie")

start_time = time.time()
click_count = 0

while True:
    current_time = time.time()
    elapsed_time = current_time - start_time

    cookie.click()
    click_count += 1

    if click_count % 5:
        cookies_ps = driver.find_element(By.ID, "money")
        cookies_count = int(cookies_ps.text.split()[-1].replace(",", ""))

        time_machine = driver.find_element(By.CSS_SELECTOR, "#buyTime\ machine b")
        time_machine_price = int(time_machine.text.split()[-1].replace(",", ""))

        portal = driver.find_element(By.CSS_SELECTOR, "#buyPortal b")
        portal_price = int(portal.text.split()[-1].replace(",", ""))

        alchemy_lab = driver.find_element(By.CSS_SELECTOR, "#buyAlchemy\ lab b")
        alchemy_lab_price = int(alchemy_lab.text.split()[-1].replace(",", ""))

        shipment = driver.find_element(By.CSS_SELECTOR, "#buyShipment b")
        shipment_price = int(shipment.text.split()[-1].replace(",", ""))

        mine = driver.find_element(By.CSS_SELECTOR, "#buyMine b")
        mine_price = int(mine.text.split()[-1].replace(",", ""))

        factory = driver.find_element(By.CSS_SELECTOR, "#buyFactory b")
        factory_price = int(factory.text.split()[-1].replace(",", ""))

        grandma = driver.find_element(By.CSS_SELECTOR, "#buyGrandma b")
        grandma_price = int(grandma.text.split()[-1].replace(",", ""))

        cursor = driver.find_element(By.CSS_SELECTOR, "#buyCursor b")
        cursor_price = int(cursor.text.split()[-1].replace(",", ""))

        if cookies_count > time_machine_price:
            time_machine.click()
        elif cookies_count > portal_price:
            portal.click()
        elif cookies_count > alchemy_lab_price:
            alchemy_lab.click()
        elif cookies_count > shipment_price:
            shipment.click()
        elif cookies_count > mine_price:
            mine.click()
        elif cookies_count > factory_price:
            factory.click()
        elif cookies_count > grandma_price:
            grandma.click()
        elif cookies_count > cursor_price:
            cursor.click()

    if elapsed_time > 300:
        break
