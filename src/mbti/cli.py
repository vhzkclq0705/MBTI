import pandas as pd
import typer
import os

types = {
    "ISTP": "백과사전형",
    "ISFP": "성인군자형",
    "ISTJ": "소금형",
    "ISFJ": "권력형",
    "INFJ": "예언자형",
    "INTJ": "과학자형",
    "INFP": "잔다르크형",
    "INTP": "아이디어형",
    "ESTP": "활동가형",
    "ESFP": "사교형",
    "ENFP": "스파크형",
    "ENTP": "발명가형",
    "ESTJ": "사업가형",
    "ESFJ": "친선도모형",
    "ENFJ": "언변능숙형",
    "ENTJ": "지도자형"
}

# 나라 별 mbit 비율 확인
# 
# parameter
# :country: 나라 명(영문)
def check_country_mbti_ratio(country: str):
    
    # 현재 파일(cli.py)의 디렉토리 경로 (src/mbti)
    # 절대 경로로 불러오기 위해 다음과 같이 경로 설정
    cur_dir = os.path.dirname(os.path.abspath(__file__))

    # 프로젝트 루트 기준으로 data/countries.csv 찾기
    csv_path = os.path.join(cur_dir, "..", "..", "data", "countries.csv")

    # csv 파일 불러오기
    df = pd.read_csv(csv_path)

    print(df)

def check_type(mbti: str):
    return types[mbti]

def print_check_type(mbti: str):
    checked_type = check_type(mbti)
    print(checked_type)

def print_check_country_ratio(country: str):
    result = check_country_mbti_ratio(country)
    print(result)

def entry_point():
    typer.run(print_check_type)

def entry_point_country():
    typer.run(print_check_country_ratio)
