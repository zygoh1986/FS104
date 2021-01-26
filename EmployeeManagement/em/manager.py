import requests

url = 'http://127.0.0.1:8000/api/apprisal/' 
headers = {'Authorization' : 'Token 7ec8c392e182d16fa3844f6f60fb2dbabde42b65'} 
r = requests.get(url, headers=headers)
print(r)