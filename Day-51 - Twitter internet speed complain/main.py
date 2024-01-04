from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time

PROMISED_DOWN = 400
PROMISED_UP = 20
CHROME_DRIVER_PATH = "chromedriver.exe"
TWITTER_EMAIL = "@gmail.com"
TWITTER_PASSWORD = "PASSWORD"

class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 180)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        self.driver.implicitly_wait(10)
        cookies = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        cookies.click()

        start_test = self.driver.find_element(By.CSS_SELECTOR, ".start-text")
        start_test.click()

        while self.driver.current_url == "https://www.speedtest.net/":
            pass
        self.driver.implicitly_wait(10)
        time.sleep(2)
        close = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/div[2]/a')
        close.click()

        self.down = float(self.driver.find_element(By.CSS_SELECTOR, ".download-speed").text)
        self.up = float(self.driver.find_element(By.CSS_SELECTOR, ".upload-speed").text)

    def tweet_at_provider(self):
        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:
            self.driver.implicitly_wait(10)
            self.driver.get("https://twitter.com/i/flow/login")

            self.driver.implicitly_wait(10)
            email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
            email.send_keys(TWITTER_EMAIL)
            email.send_keys(Keys.ENTER)

            try:
                self.driver.implicitly_wait(10)
                bot_check = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
                bot_check.send_keys("Coinwatch3")
                bot_check.send_keys(Keys.ENTER)
            except:
                pass

            self.driver.implicitly_wait(10)
            password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password.send_keys(TWITTER_PASSWORD)
            password.send_keys(Keys.ENTER)

            tweet_message = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
            tweet_message.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for Gigabit with a promise of {PROMISED_DOWN}down/{PROMISED_UP}up?")
            self.driver.implicitly_wait(10)
            tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
            tweet_button.click()

        else:
            pass


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
