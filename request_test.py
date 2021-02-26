import requests
import json

url = "https://www.baidu.com"
# url = "http://fanyi.baidu.com/v2transapi"
url_myblog = "http://121.5.64.189"

# params = {
#     "from":"en",
#     "to":"zh",
#     "query": "test"
# }

r = requests.request("get",url=url)
print(r.text)
# d = json.loads(r.text)
# print(d)


# print(r.text)