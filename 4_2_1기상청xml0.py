from bs4 import BeautifulSoup
import urllib.request as req
import os.path
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
savename = "e:/python_section4/forecast.xml"
fileName = 'e:/python_section4/forecast.txt'
if not os.path.exists(savename):
    req.urlretrieve(url, savename)

# BeautifulSoup로 분석하기
xml = open(savename, "r", encoding="utf-8").read()
soup = BeautifulSoup(xml, 'html.parser')

f = open(fileName, 'wt', encoding='utf-8')
# 지역 확인
for location in soup.find_all("location"):
    loc = location.find('city').string
    print(loc)
    print('=' * 30)
    f.write(loc + '\n')
    f.write('=' * 30 + '\n')
    for weather in location.find_all("data"):
        print("시간 : ", weather.tmef.string)
        print("날씨 : ", weather.wf.string)
        print("최저 : ", weather.tmn.string)
        print("최고 : ", weather.tmx.string)
        print("신뢰도 : ", weather.reliability.string)
        print()

        f.write("시간 : " + weather.tmef.string + '\n')
        f.write("날씨 : " + weather.wf.string + '\n')
        f.write("최저 : " + weather.tmn.string + '\n')
        f.write("최고 : " + weather.tmx.string + '\n')
        f.write("신뢰도 : " + weather.reliability.string + '\n')
        f.write('\n')

f.close()
