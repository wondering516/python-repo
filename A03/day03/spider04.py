from urllib.request import urlopen
from urllib.parse import urlencode


data = {
    'name': 'tom',
    'age' : 18
}

by_data = bytes(urlencode(data), encoding='utf-8')

url = 'http://httpbin.org/post'

#
response = urlopen(url, data=by_data)

print(response.read().decode())