#This script checks the API response and prints the user ID if it matches certain criteria.
import requests

api_url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(api_url)

for key, value in response.json().items():
    if key == "userID":
        print(f"User ID: {value}")
    if value in [1,100,200,300]:
        print("user found")  
        
        