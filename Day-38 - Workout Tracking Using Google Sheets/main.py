import requests

NUTRITION_API_ID = ""
NUTRITION_API_KEY = ""
NUTRITION_URL = "https://trackapi.nutritionix.com"
NUT_EXERCISE = "/v2/natural/exercise"

GENDER = ""
WEIGHT_KG = ""
HEIGHT_CM = ""
AGE = ""

nut_headers = {
    "x-app-id": NUTRITION_API_ID,
    "x-app-key": NUTRITION_API_KEY,
    "x-remote-user-id": "1"
}

exercise = {
    "query": input("What did you do today?"),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=f"{NUTRITION_URL}{NUT_EXERCISE}", json=exercise, headers=nut_headers)
data = response.json()
print(data)
