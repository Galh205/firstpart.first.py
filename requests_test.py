import requests

url = "https://api.apilayer.com/exchangerates_data/convert?to=ILS&from=USD&amount=1"

payload = {}
headers= {
  "apikey": "wfag4zceVvR5Wsmg56SeMc8J3lVKUHWc"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text