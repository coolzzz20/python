target = { 1, 2, 3}
print(1 in target)
#print( a in b)의 경우 b변수 안에 a라는 값이 있니 물어보는 것! 있으면 True 없으면 False이다.
print(4 in target)

num = [ 1, 2, 3, 4 ,5]
print(1 in num)
# x 는 요소를 꺼내는 임시 역할 / 전부다 값을 구하고 싶을 때
for x in num:
    print(x, end='')
print()

# x는 index / 특정 값들만 구하고 싶을 때
for x in range(0, len(num), 2):
    print(num[x])
