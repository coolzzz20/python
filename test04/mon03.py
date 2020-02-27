# 16. 리스트를 이용하여 다음과 같이 처리되록 코딩
# 학기 총점 : 100
# 학기 총점: 88
# 학기 총점: 99
# ----------------------
# 총학기 평균은 99점입니다.

lisss = []
k = 0
e = 0
while k < 3:
    jum = int(input("점수를 입력해주세요.>>> : "))
    lisss.append(int(jum))
    e = e + lisss[k]
    k = k + 1
print("총학기 평균은",str(e/k)+"입니다" )

# hab = 0
# pep = 0
# while True:
#     sco = input("학기 총점을 입력하세요. 완료시 X")
#     if sco == 'x' and 'X':
#             break
#     hab = int(sco) + hab  #합산식을 할 때는 위치 선정이 중요하다.
#     pep = pep + 1
# print("총학기 평균은", str(hab/pep)+"입니다.")