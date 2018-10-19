#a = 'hello'
#print(type(a))
#print(a[0])
#print(a[0:3])
#print(a[-1])
#for t in a:
#    print(type(t),t)

#리스트 자료형(순서0, 수정0, 중복0, 삭제0)

#선언
a = []
b = list()
c = [0,0,1,2]
#for li in c:
#    print(str(li))

d = [0,1,'car','apple','apart']
##print(d)
#print(c[0] + c[3])
#for li in d:
#    print(li)
e = [0,1,['car','apple','apart']]
#print(e[2][1])
#for li in e:
#    print(li)

#슬라이싱
#print('='*20)
#print(d[0:3])
#print(d[2:])
#print(e[0:3])

#연산
#print(c + d)
#print(c * 3)
#print('hi' + str(c[0]))

#리스트 수정, 삭제
#c[0] = 4
#print(c)
#c[1:2] = ['a','b','c']
#print(c)
#c[1] = ['a','b','c']
#print(c)
#c[1:3] = []
#print(c)
#del c[3]
#print(c)

#리스트 함수
a = [5,2,3,1,4,4]
print('============')
a.append(6)
print(a)
a.sort()
print(a)
a.reverse() #역순으로 정렬
print(a)
print(a.index(3),a[3])
print(a.count(4)) #리스트 원소중 '4'의 갯수
print(a,len(a))
a.remove(2) #리스트 원소중 '2'를 지움
print(a)
print(a.pop())#마지막 자료 꺼냄
print(a)
ex = [8,9]
a.extend(ex)
print(a)

#리스트 삭제 del, remove, pop
while a:
    l = a.pop()
    if l is 8:
        break
print(a)
