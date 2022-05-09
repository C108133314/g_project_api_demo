import requests

result = requests.post("http://127.0.0.1:8000/get_aspect_api/", data = {"userInput" : "房間環境有待加強，有味道"})
print(result)