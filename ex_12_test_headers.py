import requests

def test_headers():
    url = "https://playground.learnqa.ru/api/homework_header"
    response = requests.get(url)
    header = response.headers
    print(header)
    assert header["x-secret-homework-header"] == 'Some secret value', "There is no right header in response"