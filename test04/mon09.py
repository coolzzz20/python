import random

#로또 문제 set으로 하는 경우

result = set()
while True:
    choice = random.randint(1, 45)
    result.add(choice)
    if len(result) ==6:
        break

print(result)
