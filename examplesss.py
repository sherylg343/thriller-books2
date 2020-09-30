import requests

response = requests.get("https://www.googleapis.com/books/v1/volumes/?q=Harry%20potter")
jitem = response.json()
# print(jitem.keys())
for x in range(5):
    author = jitem["items"][x]["volumeInfo"]["authors"][0]
    title = jitem["items"][x]["volumeInfo"]["title"]
    print(author + " - " + title)
