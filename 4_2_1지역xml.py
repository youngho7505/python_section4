from bs4 import BeautifulSoup
import urllib.request as req
import os.path
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=2641063500"
savename = "e:/python_section4/forecast2.xml"
fileName = 'e:/python_section4/forecast_두구동.txt'

if os.path.exists(savename):
    os.remove(savename)

if not os.path.exists(savename):
    req.urlretrieve(url, savename)

# BeautifulSoup로 분석하기
xml = open(savename, "r", encoding="utf-8").read()
soup = BeautifulSoup(xml, 'html.parser')

f = open(fileName, 'wt', encoding='utf-8')
# 지역 확인
loc = soup.find('category').string
tm = soup.find('tm').string
print(loc)
print('발표시각 : ' + tm)
print('=' * 25)
f.write(loc + '\n')
f.write('발표시각 : ' + tm + '\n')
f.write('=' * 25 + '\n')

for weather in soup.find_all("data"):
    if weather.day.string == '0':
        print("날자 : " + '오늘')
    elif weather.day.string == '1':
        print("날자 : " + '내일')
    elif weather.day.string == '2':
        print("날자 : " + '모레')

    print("시간 : ", weather.hour.string)
    print()
# 이런식으로 코딩하면 된다. ^^^^
    f.write("시간 : " + weather.hour.string + '\n')
    f.write("날씨 : " + weather.day.string + '\n')
    f.write('\n')

f.close()
