import requests
from datetime import datetime

USERNAME = ""
TOKEN = "alskdjlsafjsaldfjal;sdf"
pixela_endpoint = "https://pixe.la/v1/users"

headers = {
    "X-USER-TOKEN": TOKEN
}

# Create Pixela account
'''

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "alskdjlsafjsaldfjal;sdf",
    "username": "",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

'''

# Create Graph
''' 
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Study Graph",
    "unit": "Hours",
    "type": "float",
    "color": "ajisai"
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

'''

# Add a pixel to the graph
'''

graph_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

today = datetime.now()

graph_content = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hour(s) did you study today? ")
}

response = requests.post(url=graph_post_endpoint, json=graph_content, headers=headers)
print(response.text)

'''

# Update pixel value
'''
graph_put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20220713"

graph_update = {
    "quantity": "1"
}

response = requests.put(url=graph_put_endpoint, json=graph_update, headers=headers)
print(response.text)
'''
