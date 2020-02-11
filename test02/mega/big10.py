from tkinter import messagebox

messagebox.showinfo("안녕하세요.", "홍길동이요")
#두가지 밖에 나타내지 못한다 (A, B) 나타난다. (A, B, C) 나타나지 않음 <--오류
messagebox.showwarning("지금은 오후예요", "졸음주의!!!")
result = messagebox.askquestion("시간체크" ,"지금은 오후인가요?")
print(result)

