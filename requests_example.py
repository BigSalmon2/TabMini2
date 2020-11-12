import requests

url = "https://main-gpt2-large-jeong-hyun-su.endpoint.ainize.ai/gpt2-large/long"
data = {
    "text": "Hi my name is hyeonwoong and", 
    "num_samples": 5,
    "length": 20
}

response = requests.post(url, data=data)

if response.status_code == 200:
    res = response.json() 
    print(res)

else:
    print("Failed requests")