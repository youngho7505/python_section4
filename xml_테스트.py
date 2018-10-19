from bs4 import BeautifulSoup
import urllib.request as req
import os.path
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://thestar.chosun.com/site/data/rss/rss.xml"
savename = "e:/python_section4/joins2.xml"
fileName = 'e:/python_section4/joins2.txt'
if not os.path.exists(savename):
    req.urlretrieve(url, savename)

# BeautifulSoup로 분석하기
xml = open(savename, "r", encoding="utf-8").read()
soup = BeautifulSoup(xml, 'html.parser')

f = open(fileName, 'wt', encoding='utf-8')
# 지역 확인
for news in soup.find_all("item"):
    for li in news.children:
        print(li.string, end='')
        f.write(str(li.string))
    print()
    f.write('\n')

f.close()
