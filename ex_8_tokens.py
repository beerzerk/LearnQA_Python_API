import requests
import time
import json

url = "https://playground.learnqa.ru/ajax/api/longtime_job"

# 1) создавал задачу
response = requests.get(url)
# print(response.text)
obj = json.loads(response.text)
token = obj["token"]
seconds = obj["seconds"]
print("Token:", token, "\nSeconds:", seconds)

# 2) делал один запрос с token ДО того, как задача готова, убеждался в правильности поля status
payload = {"token": token}
response = requests.get(url, params=payload)
obj = json.loads(response.text)
status = obj["status"]
if status == "Job is NOT ready":
    print("Status:", status)


# 3) ждал нужное количество секунд с помощью функции time.sleep()
if status == "Job is NOT ready":
    time.sleep(seconds)
    response = requests.get(url, params=payload)
    obj = json.loads(response.text)
    status = obj["status"]
    print("Status:", status)


# 4) делал бы один запрос c token ПОСЛЕ того, как задача готова, убеждался в правильности поля status и наличии поля result
response = requests.get(url, params=payload)
obj = json.loads(response.text)
status = obj["status"]
if status == "Job is ready":
    result = obj["result"]
    print("Result:", result)
else:
    print("Job is NOT ready")
