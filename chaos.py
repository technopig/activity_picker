import requests
import time

# while True:
for a in range(0,1000000):
    result = requests.get("http://localhost:5016/")
    time.sleep(0.03)
# print(result.text)
