# if, for, while
# import random

# raw_input = input("숫자를 입력하세요")
# # print(f"{type(raw_input)}, {raw_input}")

# guess = int(raw_input)

# target = random.randint(1,5)

# for문
# for i in range(10):
#     print("i")

# print(list(range(10)))

# a = 0
# for i in range(10):
#    a += i 
# print(a)

# a = 0
# while True:
#     a += 1
#     print(a)
#     if a > 10:
#         break

import random

target = random.randint(1, 10)

# for i in range(10):
while True:
    guess = int(input("숫자를 입력하세요"))
    if guess == target:
        print("정답 입니다.")
        break
    elif guess < target:
        print("target은 좀 더 큰 숫자입니다.")
    elif guess > target:
        print("target은 좀더 작은 숫자입니다.")

