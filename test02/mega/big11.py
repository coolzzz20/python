#콘솔에서 당신의 짝이름을 입력받으세요.
#콘솔에서 당신의 짝관심사를 입력받으세요.
#메세지 박스로 당신의 짝이름과 관심사를 확인하여 출력
#관심사가 파이썬이라고 한다면, "프로그래머가 되실 거군요."
#           아니라면, "데이터 분석가가 되실 거군요." 출력

#name = input("이름을 입력해주세요>>>")
#inte = input("관심사를 입력해주세요")

#from tkinter import messagebox

#messagebox.showinfo("안녕하세요", name)
#messagebox.showinfo("당신의 관심사는", inte)

from tkinter import messagebox
#콘솔에서 당신의 짝이름을 입력받으세요
name = input("짝이름은?")
#콘솔에서 당신의 짝관심사를 입력받으세요
good = input("짝관심사는?")
#메세지 박스로 당신의 짝이름과 관심사를 확인하여 출력
messagebox.showinfo('확인' , name + ','+ good)
#관심사가 파이썬이라면 한다면," 프로그래머가 되실거군요"
#아니라면, "데이터 분석가가 되실거군요" 출력
if good == '파이썬':
    messagebox.showinfo('결과', "프로그래머가 되실거군요.")
else:
    messagebox.showinfo('결과',"데이터 분석가가 되실거군요.")

#내가 문제를 보고 푼 것
# 메세지 박스로 파이썬이 확실한가요?
#dad = input("파이썬이 확실한가요?>>")
#messagebox.showinfo("결과", dad)
# 맞다라고 하면, 열심히 하세요!
#if result == "yes":
    #messagebox.showinfo('결과', '열심히하세요!')
# 아니라고 하면, 그럼 생각중이시군요!
#else:
   # messagebox.showinfo('결과','그럼 생각중이시군요!')

# 메세지 박스로 파이썬이 확실한가요?
result = messagebox.askquestion('질문', '파이썬이 확실한가요?')

# 맞다라고 하면, 열심히 하세요!
if result == "yes":
    messagebox.showinfo('결과', '열심히하세요!')
# 아니라고 하면, 그럼 생각중이시군요!
else:
    messagebox.showinfo('결과','그럼 생각중이시군요!')