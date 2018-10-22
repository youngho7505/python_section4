import sys
import io
import urllib.request as req
import simplejson as json
import os.path

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://jsonplaceholder.typicode.com/posts"

saveName = 'e:/python_section4/jsonplaceholder.json'
if not os.path.exists(saveName):
    req.urlretrieve(url, saveName)

items = json.load(open(saveName, 'r', encoding='utf-8'))

for item in items:
    print('=' * 50)
    print(str(item['userId']) + '(' + str(item['id']) + ')')
    print(item['title'])
    print(item['body'])
