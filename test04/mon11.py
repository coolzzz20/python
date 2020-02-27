import random

#가위바위보 9가지
nam = [ '가위', '바위', '보']
a = random.randint(0, 2)

print(nam[a])
b = random.randint(0, 2)
num = ['가위', '바위', '보']
print(num[b])

if a == b:
        print("나는" ,num[a], "당신은", num[b], "비겼습니다")
elif a > b:
    if a == (b + 1): # 0 1 /1 2 /2 3
        print("나는" ,num[a], "당신은", num[b],"당신이 이겼습니다")
    elif a == 2 and b == 0:
        print("나는" ,num[a], "당신은", num[b],"당신이 이겼습니다")
elif a < b:
    if (a+1) == b:
        print("나는", num[a], "당신은", num[b], "내가 이겼습니다")
    elif a == 0 and b == 2:
        print("나는", num[a], "당신은", num[b], "내가 이겼습니다")






# 판별 결과 프린트: 컴퓨터가 승, 내가 승, 비김


# while True:
#     me = input('가위바위보>>') #내가 냄
#     com = random.choice(['가위','바위','보']) # 컴퓨터가 냄
#     print('컴퓨터가', com , '냄')
#     if me == '가위':
#         print('내가 가위 냄')
#         if com =='가위': print('비김')
#         elif com == '바위' : print('짐')
#         else: print('내가 이김')
#     elif me == '바위':
#         print('내가 바위 냄')
#         if com =='가위': print('내가 이김')
#         elif com == '바위' : print('비김')
#         else: print('내가 졌다')
#     elif me == '보':
#         print('내가 보 냄')
#         if com =='가위': print('내가 짐')
#         elif com == '바위' : print('내가 이겼다')
#         else: print('비김')
#     else:
#         print('잘못 내셨습니다.')

