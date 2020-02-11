#1
price = input("1년 만기 정기 예금을 얼마나 예치하시겠습니까?>>>")
print("원금이 "+str(price)+"이시군요")
price1 = int(price)
bonus = price1/10
print("이자는"+str(bonus)+"입니다")
print("원리합계는" + str(price1+bonus)+"입니다")
#2
eng = input("영어점수 입력")
mat = input("수학점수 입력")
kor = input("국어점수 입력")
print("-----------------------------")
eng1 = int(eng)
mat1 = int(mat)
kor1 = int(kor)
print("세 과목의 합은"+str(eng1+mat1+kor1)+"입니다")
print("세 과목의 평균은"+str((eng1+mat1+kor1)/3)+"입니다")
#3
time = input("지금은 몇 시 입니까? >>>")
time1 = int(time)
if time1 < 12 :
    print("점심 전입니다. 맛있게 드세요.!")
else:
    print("점심 후입니다. 맛있게 드세요.!")
#4
id = input("로그인할 id를 입력>>")
tid = "root"

if id == tid :
    print("로그인이 되셨습니다.")
else  :
    print("로그인에 실패하셨습니다.")

#5
sti = 1000 #스티커
book = 2500 #책갈피
num1 = input("스티커 구매 수량>>>>")
num2 = input("책갈피 구매 수량>>>>")
nums1 = int(num1)
nums2 = int(num2)

print(str((sti*nums1) + (book*nums2))+"입니다.")

mem = input("우수회원 체크해주세요.")
vip = "Y"

dis = ((sti*nums1) + (book*nums2))/10
tal = (sti*nums1) + (book*nums2)

dis1 = int(dis)
tal1 = int(tal)

if mem == vip:
    print("우수회원입니다. 10%할인 가능합니다.",tal1-dis1, "입니다")
else:
    print("우수회원아니십니다." + "할인받으실수없스비다.", tal1, "입니다.")