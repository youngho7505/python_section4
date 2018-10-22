import sys
import io
import simplejson as json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#Dict(json) 선언
data = {}
data['people'] = []
data['people'].append({
    'name':'kim',
    'website':'naver.com',
    'from':'busan'
})
data['people'].append({
    'name':'park',
    'website':'daum.net',
    'from':'suwon'
})
data['people'].append({
    'name':'lee',
    'website':'yahoo.com',
    'from':'seoul'
})
#data = {'people': [{'name': 'kim', 'website': 'naver.com', 'from': 'busan'}, {'name': 'park', 'website': 'daum.net', 'from': 'suwon'}, {'name': 'lee', 'website': 'yahoo.com', 'from': 'seoul'}]}

#dict(json) -> str
e = json.dumps(data, indent=2) #indent : 들여쓰기
#print(type(e), e) #str

#str -> dict(json)
d = json.loads(e)
#print(type(d), d)

with open('e:/python_section4/member.json', 'w') as outfile:
    outfile.write(e)

with open('e:/python_section4/member.json', 'r') as infile:
    r = json.loads(infile.read())
    #print('='*10)
    #print(type(r), r)
    for p in r['people']:
        print('='*20)
        print('Name : ', p['name'])
        print('Website : ', p['website'])
        print('From : ', p['from'])
