import random
# while True:
#   print(target = random.randint(1, 100))

#뒤에 계시 선생님이 풀어주신 문제

a = []
while len(a) < 6:

    b = random.randint(1,45)
    if b in a:      # in 개념  : ~에 속한 것 [ ]
        pass
    else:
        a.append(b)  # b값이 정해져서 a값에 넣어준다.
for x in a:
    print(x, end=' ')
print()
print(a)

