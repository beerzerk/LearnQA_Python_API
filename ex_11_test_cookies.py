import requests

def test_cookies():
    url = "https://playground.learnqa.ru/api/homework_cookie"
    response = requests.get(url)
    cookie = dict(response.cookies)
    print(cookie)
    assert cookie["HomeWork"] == 'hw_value', "There is no right cookie in response"