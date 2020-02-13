import turtle

pen = turtle.Pen()
pen.color('skyblue')  # 색상입력
pen.shape('turtle')  # 모양입력
# pen.left(90)
# pen.forward(100)


while True:
    choice = input('왼쪽: left, 오른쪽: right, 종료:x >>>>')
    if choice == 'x':
        print('종료합니다')
        break
    if choice == 'left':
        pen.left(75)
        pen.forward(100)
    if choice == 'right':
        pen.right(75)
        pen.forward(100)

# 정사각형을 그리는 코드.

# 들여쓰기: indent(인덴트)
# 코드 자동 정리=> ctrl + shift + f
