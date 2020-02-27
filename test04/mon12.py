import random

# random.randint(1, 45) 이용
# 6번 실행
# 중복된 값이 없어야함
# 리스트 값 처럼 나열할 수 있어야함.

a = random.randint(1, 45)
c = random.randint(1, 45)
d = random.randint(1, 45)
e = random.randint(1, 45)
f = random.randint(1, 45)
g = random.randint(1, 45)
b = []

if a != b:
    b.append(a)

    if c != b[0]  :
        b.append(c)

        if d != b[0] and c != b[1]  :
                b.append(d)

                if e != b[0] and c != b[1] and c != b[2] :
                    b.append(e)

print(b)
b.sort()
print(b)