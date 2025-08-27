import requests

# print(dir(requests))

response = requests.get('https://api.github.com')
rjson = response.json()
print(rjson['current_user_url'])

payload = {'username': 'karthik', 'password': 'dummy'}
r = requests.post('https://httpbin.org/post', data=payload)
rjson= r.json()
print(rjson)
print(rjson['url'])
