#커피값
coffee = 5000
#인원수를 입력
count = input("인원을 입력하세요")
#input 과 변수 값을 같이 계산 할 수 없다. count2로 변경
count2 = int(count)
#input값을 설정 후 변수 값으로 변경하여 곱으로 계산을 한다
sum = coffee*count2
#20000이상일 경우
if sum >= 20000 :
    print(str(sum) +  "값을 2000원을 할인해드립니다.")
#20000미만일 경우
else:
    print(str(sum) + "값을 다 지불하셔야합니다.")