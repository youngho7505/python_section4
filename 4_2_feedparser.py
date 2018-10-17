import sys
import io
import feedparser

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#urls = (
#    "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=159",
url = "http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=2641063500"

#def crawl_rss(url):
d = feedparser.parse(url)
print(type(d))
print(d.feed['title'])
for e in d.entries:
    print("hour : " + e.hour)
    
