import urllib.request as req
from bs4 import BeautifulSoup
import requests
import sys
import io
from collections import OrderedDict
from itertools import count
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

def torrent_cralwler(max_page):
    url = "http://javtorrent.me/" #torrentmap의 한국드라마
    post_dict = OrderedDict() #OrderedDict를 사용하며, key에 url을 넣겠습니다.
                              #url은 유일성이기 때문에!
    fName = 'e:/imagedown/javTorr.txt'
    if os.path.exists(fName):
        os.remove(fName)

    f = open(fName, 'wt', encoding='utf-8')
    i = 1
    for page in count(1): #1부터 무한대로 시작(break or return이 나올때까지)
        param = {
            'page': page
        }
        html = url + 'page/' + str(page)
        #print(html)
        response = requests.get(html)
        html = response.text
        #print(html)
        soup = BeautifulSoup(html, "html.parser")
        titleList = soup.select("div#masonry-container .entry-title > a")
        #print(titleList)

        for srcList in titleList:
            if max_page and (page > max_page):
                return post_dict
            if srcList['href'] in post_dict: #지금 저장할 링크(key)가 이미 post_dict에 있다면
                return post_dict #리턴해서 끝내버린다.
            print(i, srcList.text + '  -  ' + srcList['href'])
            f.write(str(i) + ' ' + srcList.text + '(' + srcList['href'] + ')\n')
            post_dict[srcList['href']] = srcList['href']
            i += 1
#
    return post_dict
    f.close()


#실행
if __name__ == '__main__':
    torrent_cralwler(4)
