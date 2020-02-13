#target = {1,2,3} #집합기호 "{ }" => 중복X
#target.add(4)
#print(target)
#target.add(2)
#print(target)

##dic = {'apple' : '사과', 'banana' : '바나나', 'melon' : '멜론'}
##print(dic)
# A : B 라고 있을 때 A만 찾을 수있고 B는 못찾는다?
##print(dic.get('apple'))

# 리스트, 집합, 사전, 튜플 => 모음(collection)
#팀원(1번)
team = { '디자이너' , '프로그래머' , 'DB관리자'}
print(team)
team.add('디자이너')
print(team)

#스키대회(3번)
ski = ['박스키', '송스키', '김스키', '정스키']
print(ski)
del ski[1]
print(ski)

#휴대폰(4번) 숫자 : 문자 해도 상관없다. 양쪽 다 타입은 상관없다.
num = { 1 : '엄마', 2 :'아빠', 3 : '친구', 4 : '동생'}
print(num)
print(num.get(2))
print(len(num))