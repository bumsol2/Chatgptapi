"""
모듈과 패키지
모듈 :하나의 파이썬 파일, 이 파일에 들어있는 다른 함수나, 클래스, 변수들을 가져와서 사용 하 수가 있습니다.
패키지: 모듈들을 묶어 놓은 폴더 
"""
# import overwatch as ow

# print(ow.get_hp_by_character("genji"))

# print(ow.hp_by_character)

# from game.user import User
# import game.user as u

# user = u.User(username="python", rank="gold")
# user.print_info()

"""
예외 처리 
"""

# try:
#     print(1/0)
# except Exception as e:
#     print(f"error occur!, {e}")

# print("here here")
"""
내장 함수 
"""
# a = [1,2,3]
# print(f"a의 길이: {len(a)}")

# print(max(a))

# print(max(5,10))

# print(min(a))
# print(min(5, 10))

# print(sum(a))

"""
표준 라이브러리
"""

import json
import glob
import datetime


# a = {"genji": 200, "doomfist": 450}

# with open("./hp_by_character", "wt") as f:
#     json.dump(a, f)

# with open("./hp_by_character", "rt") as f:
#     b= json.load(f)

# print(b)

# all_python_file_list = glob.glob("./*.py")
# print(all_python_file_list)

# print(datetime.datetime.now())

"""
외부 라이브러리

pandas, request, tqdm 
"""
import pandas as pd

# a = {"name": ["genji", "para", "doomfist"], 
#      "hp": ["200","200", "450"]}

# a_df = pd.DataFrame(a)

# print(a_df)

# a_df.to_excel("./overwatch.xlsx")

# b_df = pd.read_excel("./overwatch.xlsx")

# print(b_df)
# import requests
# response =requests.get("https://naver.com")
# print(response.text)

import tqdm
import time

i = 0
for i in tqdm.tqdm(range(10)):
    i += 1
    time.sleep(0.2)

"""
가상 환경
여러 프로젝트에 사용되는 라이브러리들이 다를 수 있고, 같더라도 그 버전이 다를 수 있습니다.
"""


