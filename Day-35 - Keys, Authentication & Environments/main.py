import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.getenv("API_KEY")
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")

weather_paramters = {
    "lat": 0,
    "lon": 0,
    # "q": "",
    "units": "metric",
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get(url=OWM_Endpoint, params=weather_paramters)
response.raise_for_status()
weather_data = response.json()

will_rain = False

weather_slice = weather_data["hourly"][:11]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    # client = Client(account_sid, auth_token)
    # message = client.messages.create(
    #     body="It's going to rain today. Remember to bring an umbrella☂️.",
    #     from_="+12393606925",
    #     to="+31640936031"
    # )
    #
    # print(message.status)

    print("It's going to rain today. Remember to bring an umbrella☂️.")