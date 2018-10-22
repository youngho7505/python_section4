import sys
import io
import urllib.request as req
import simplejson as json
import os.path

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "https://api.github.com/repositories"

#경로, 파일명
saveName = 'e:/python_section4/repo.json'

if not os.path.exists(saveName):
    req.urlretrieve(url, saveName)

items = json.load(open(saveName, 'r', encoding='utf-8'))
#items = json.loads(open(saveName, 'r', encoding='utf-8').read())
for item in items:
    print(item["full_name"] + ' - ' + item["owner"]["url"])
