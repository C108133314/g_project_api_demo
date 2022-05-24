import requests

result = requests.post("https://www.hoteller.online/get_aspect_api/", data = {"userInput" : "房間環境有待加強，有味道"})
print(result)
