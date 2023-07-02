# 자료형과 변수
# int, float, str, list tuple, set, dict
# comment, 주석

"""
#int
print(1+2+3)

# float
print(1.1)
print(3.14)

#str
print("문자를 뜻하는 str 자료형")

print("문자를 뜻하는 것이 str 자료형" + "같은 자료형끼리만 가능, 다른 자료형끼리는 연산 안됨")
"""
# print("-" * 30 )
# print("안녕" )

# #변수
# a = 1
# b = 2
# print(a+b)

# c = "문자도 변수에 저장 가능\n줄바꿈이 있는 경우\\n으로 표시"
# print(c)

# d = """ 여러줄 문장 
# 이렇게 쉽게 표현이 가능
# """
# print(d)

# formatting

# a = "오늘"
# b = input("오늘 날씨는 얼마야?")

# print(f"{a}의 날씨는 {b}도입니다.")
# print(f"{c}의 날씨는 {d}도입니다.".format(c=a, d=b))

#list
# a = [1,2,3,4]

# print(a)

# #indexing, sclicing
# print(a[1])

# # [2, 3]
# print(a[:2])

# tuple
# a = ["오늘", "내일", "모래"]
# b = ("오늘", "내일", "모래")

# print(a)
# a[1] = "XX"
# print(a)

# print(b)
# b[1] = "XX"
# print(b)

# set
# a = {1,2,3,1,2}
# a = set([1,2,3,1,2])

# print(a)
# a.add(10)
# print(a)

# a = [1,2,3,1,2]

# print(a)
# a.append(10)
# print(a)

# dict
a = {'a':1, 'b':2}
print(a)

print(a['b'])

hp_character = {'genji':200, 'doomfist': 450}

# print(hp_character)
character = 'doomfist'
print(f"{character} hp: {hp_character['doomfist']}")