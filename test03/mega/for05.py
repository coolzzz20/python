list2 = [100, 200, 300, 400, 500, 600, 700, 800, 900]

#for문을 사용하세요.
# 1.전체 목록을 프린트
for x in list2:
    print(x)
print()
# 2.홀수 번째 있는 요소들을 프린트
for x in range(0,len(list2),2):
    print(list2[x], end='')
print()
# 3. 홀수 번째 있는 요소들을 다 더해서 프린트
sum = 0
for x in range(0, len(list2), 2):
    #print(list[x])
    sum = list2[x] + sum
print(sum)
# 4.짝수 번쨰 있는 요소들을 프린트
for x in range(0, len(list2)):