import requests

def api_check():
  try:
    url = "https://reqres.in/api/users"
    response = requests.get(url, timeout=5)
    return response.status_code == 200
  except requests.RequestException:
    return False


print(api_check())