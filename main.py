import json
import urllib.request

api_git_request = urllib.request.urlopen("http://api.github.com")
dict_api = json.loads(api_git_request.read())

for key, el in dict_api.items():
    print(key, "=====>", el)
