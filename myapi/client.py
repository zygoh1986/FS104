import requests

url = 'http://127.0.0.1:8000' 
headers = {'Authorization': 'Token 900a0f6860ba65e7d9011ec50ef2edb535300b86'} 
r = requests.get(url, headers=headers)
print(r)