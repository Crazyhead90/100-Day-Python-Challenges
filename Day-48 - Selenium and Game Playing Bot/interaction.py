from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# url = "https://en.wikipedia.org/wiki/Main_Page"
url = "http://secure-retreat-92358.herokuapp.com/"

chrome_driver_path = "F:\SynologyDrive\Drive 2\Python\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url)
# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()


# all_portals = driver.find_element(By.LINK_TEXT, "View source")
# all_portals.click()

# search_bar = driver.find_element(By.NAME, "search")
# search_bar.send_keys("Python")
# search_bar.send_keys(Keys.ENTER)

# ------- Challenge ------- #

fname = driver.find_element(By.NAME, "fName")
fname.send_keys("Danny")

lname = driver.find_element(By.NAME, "lName")
lname.send_keys("Iets")

email = driver.find_element(By.NAME, "email")
email.send_keys("Dummy@dumdum.com")
email.send_keys(Keys.ENTER)