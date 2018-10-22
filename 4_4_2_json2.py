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
    'from':'busan',
    'grade':[95,77,85,40]
})
data['people'].append({
    'name':'park',
    'website':'daum.net',
    'from':'suwon',
    'grade':[85,100,85,90]
})
data['people'].append({
    'name':'lee',
    'website':'yahoo.com',
    'from':'seoul',
    'grade':[96,97,95,80]
})
#data = {'people': [{'name': 'kim', 'website': 'naver.com', 'from': 'busan', 'grade': [95, 77, 85, 40]}, {'name': 'park', 'website': 'daum.net', 'from': 'suwon', 'grade': [85, 100, 85, 90]}, {'name': 'lee', 'website': 'yahoo.com', 'from': 'seoul', 'grade': [96, 97, 95, 80]}]}

# json 파일 쓰기(dump)
with open('e:/python_section4/member2.json', 'w') as outfile:
    json.dump(data, outfile)

with open('e:/python_section4/member2.json', 'r') as infile:
    r = json.load(infile)
    #print(type(r), r)
    for p in r['people']:
        print('=' * 20)
        print('Name : ', p['name'])
        print('Website : ', p['website'])
        print('From : ', p['from'])
        #print('Grade : ', p['grade'])
        grade = ''
        tot = 0
        for g in p['grade']:
            grade = grade + ' ' + str(g)
            tot += g
        print('Grade : ', grade.lstrip() + ' ' + str(tot)) #lstrip(좌측 공백 제거)
        #print('Total : ', str(tot))
