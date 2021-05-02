import requests
import time

while True:
    result = requests.get("http://localhost:5016/")
    time.sleep(0.05)
# print(result.text)
