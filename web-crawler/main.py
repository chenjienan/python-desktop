import urllib.request
import re


url = "https://book.douban.com/top250?icn=index-book250-all"

request = urllib.request.Request(url)

response = urllib.request.urlopen(request)

data = response.read()

data = data.decode('utf-8')

# print(data)

scores = re.findall(r'<span class="rating_nums">(.*)</span>', data)

print(scores)