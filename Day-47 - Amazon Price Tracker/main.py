import requests
from bs4 import BeautifulSoup
import lxml
import smtplib


URL = "https://www.amazon.nl/-/en/gp/product/B083KM6BZS/ref=ewc_pr_img_1?smid=AE9XWIQL6Y1PP"
BUY_PRICE = 100

MY_EMAIL = "@gmail.com"
MY_PASSWORD = ""

header = {
    "Accept-Language": "nl,en-US;q=0.7,en;q=0.3",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
}

response = requests.get(URL, headers=header)
website_lxml = response.text

soup = BeautifulSoup(website_lxml, "lxml")

whole_price = int(soup.find(name="span", class_="a-price-whole").getText()[:-1])

if whole_price < BUY_PRICE:
    full_price = soup.find(name="span", class_="a-offscreen").getText()[1:]
    product_title = soup.find(id="productTitle").getText().strip()
    product_url = soup.find(name="link", rel="canonical").get("href")

    message = f"{product_title}\nIs now: {full_price} euro\n{product_url}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}"
        )
