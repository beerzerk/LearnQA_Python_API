import requests

response = requests.post("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
count = 0
for i in response.history:
    count += 1
print(count)
print(response.url)