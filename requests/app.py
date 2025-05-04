# import requests
import json

# GET All
# r = requests.get("https://jsonplaceholder.typicode.com/posts")
# print(r)
# data = json.loads(r.content)
# print(data[0]["title"])

# GET One
# id = int(input("please id your post :"))
# r = requests.get(f"https://jsonplaceholder.typicode.com/posts/{id}")
# print(json.loads(r.content))

# POST data
# data = {
#     "title":"this is title test for requests",
#     "body":"this is body test for requests package pypi and python",
#     "userId":1
# }
# r = requests.post("https://jsonplaceholder.typicode.com/posts",
#     data=json.dumps(data),
#     headers={
#         'Content-type': 'application/json; charset=UTF-8'
#     }
# )
# print(json.loads(r.content))

# PUT data
# id = int(input("please enter id post : "))
# data = {
#     "title":"this is title put for requests",
#     "body":"this is body put for requests package pypi and python",
#     "userId":1
# }
# r = requests.put(f"https://jsonplaceholder.typicode.com/posts/{id}",
#     data=json.dumps(data),
#     headers={
#         'Content-type': 'application/json; charset=UTF-8'
#     }
# )
# print(json.loads(r.content))

# DELETE data
# id = int(input("please enter id post : "))
# r = requests.delete(f"https://jsonplaceholder.typicode.com/posts/{id}")
# print(json.loads(r.content))
# print(r.status_code)
