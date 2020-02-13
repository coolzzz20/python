list2 = [100, 200, 300, 400, 500, 600, 700, 800, 900]

#for문을 사용하세요.
# 1.전체 목록을 프린트
for x in list2:
    print(x)
print()
print()
# 2.홀수 번째 있는 요소들을 프린트
for x in range(0,len(list2),2):
     print(list2[x], end='  ')
print()
print()
print('=================')
# 3. 홀수 번째 있는 요소들을 다 더해서 프린트
print()
print()
sum = 0
for x in range(0, len(list2), 2):
    #print(list[x])
    sum = list2[x] + sum
print(sum)
print()
print('====================')
# 4.짝수 번쨰 있는 요소들을 프린트
print()
print()
for x in range(1,len(list2), 2):
    print(list2[x], end='  ')

print()
print()
print('================')
print()
print()
# for문을 이용해서 풀어보세요. list2랑 별개 문제.
# 1부터 1000까지 더해보세요.
sum2 = 0
for x in range (1, 1001):
    sum2 = sum2 + x
print(sum2)
