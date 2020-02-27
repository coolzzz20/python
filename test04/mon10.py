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
f = random.randint(1, 45)
print(len(b))
print('1-----------------------')
if len(b) == 0:
    b.append(a)
    print(b)
    print('2-----------------------') #a
    if c != b[0]:
        b.append(c)
        print(b)
        print('3---------------------------------') #a c

        if d != b[0] and d != b[1]:
            b.append(d)
            print(b)
            print('4---------------------') #a c d

            if e != b[0] and e != b[1] and e != b[2]:
                b.append(e)
                print(b)
                print('5-----------------------') #a c d e

                if g != b[0] and g != b[1] and g != b[2] and g != b[3]:
                    b.append(g)
                    print(b)
                    print('6--------------------') # a c d e g

                    if f != b[0] and f != b[1] and f != b[2] and f != b[3] and f != b[4]:
                        b.append(f)
                        print(b)
                        print('7--------------------------') #a c d e g e

                        # if f != b[0] and f != b[1] and f != b[2] and f != b[3] and f != b[4] and f != b[5]:
                        #     b.append(f)
                        #     print(b)
                        #     print('8------------------------------')




print(b)
b.sort()
print(b)

for x in b:
    print(x, end=' ')

# b = [ 2 , 3 , 5 ,7 ,9]
#
# print(b[0] , b[1] , b[2])
# print(int(b[0]))
#
# a = 5
# if a == b[0] or b[1] or b[2] or b[3] or b[4]:
#     print("성공")
