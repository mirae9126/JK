#교재 7장 6절 리스트, 튜플, 딕셔너리의 심화 내용 (p.214)
#세트:키만 모아 놓은 딕셔너리의 특수한 형태
#컴프리헨션: 값이 순차적인 리스트를 한 줄로 만드는 간단 방법

#변수선언
a,b,c,d,e,f,g,h = {0,1,2,3,4,5,6,7} 
mySet1 = {1, 2, 3, 4, 5}
mySet1
print(mySet1)

##셋트함수

salesList = {'삼각김밥', '바나나', '도시락', '도시락'}

set(salesList)

print(salesList)

mySet1 = {1,2,3,4,5}
mySet2 = {4,5,6,7}
a = mySet1 & mySet2  ##교집합
b = mySet1 | mySet2  ##합집합
c = mySet1 - mySet2  ##차집합
d = mySet1 ^ mySet2  ##대칭차집합
print(a, b, c, d)

#집합함수사용

e = mySet1.intersection(mySet2) #교집합
f = mySet1.union(mySet2) #합집합
g = mySet1.difference(mySet2) #차집합
h = mySet1.symmetric_difference(mySet2) #대칭차집합
print(e, f, g, h)
