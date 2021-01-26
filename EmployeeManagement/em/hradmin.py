import requests

url = 'http://127.0.0.1:8000/api/employees'
urld = 'http://127.0.0.1:8000/api/departments'
headers = {'Authorization' : 'Token b6b75525a2990810574fec4144da8debffd42a66'} 
r = requests.get(url, urld, headers=headers)
print(r)