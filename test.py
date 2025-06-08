import requests
proxies = {"http": "http://10.10.0.10:28888", "https": "http://10.10.0.10:28888"}
r = requests.get("https://www.youtube.com", proxies=proxies)
print(r.status_code)
