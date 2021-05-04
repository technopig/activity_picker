import requests
import time

# while True:
for a in range(0,100000):
    result = requests.get("http://localhost:5016/")
    time.sleep(0.1)
# print(result.text)
