import requests

url="https://playground.learnqa.ru/ajax/api/compare_query_type"

#1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.
response = requests.get(url)
print("Case 1")
print("Not enough parameters in request:", response.text)
print("Server response:", response.status_code)

#2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.
response = requests.head(url, data={"method": "HEAD"})
print("Case 2")
print("Wrong type of request:", response.text)
print("Server response:", response.status_code)

#3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.
response = requests.post(url, data={"method": "POST"})
print("Case 3")
print("Response:", response.text)
print("Server response:", response.status_code)

#4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method.
# Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ и так далее.
# И так для всех типов запроса. Найти такое сочетание, когда реальный тип запроса не совпадает со значением параметра, но сервер отвечает так, словно все ок.
print("Case 4")
methods = ["GET", "POST", "PUT", "DELETE"]
for api_method in methods:
    for params_method in methods:
        response = requests.request(api_method, url, params={"method": params_method}, data={"method": params_method})
        print("Method:", api_method, "Params:", params_method)
        print("Response:", response.text)
        print("Server response:", response.status_code)


