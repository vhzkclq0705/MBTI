import pandas as pd
import typer
import os

def check_country_mbti_ratio(mbti: str, asc: bool=False, rcnt: int=10) -> pd.DataFrame:
    """   
    특정 MBTI 유형을 기준으로 나라별 비율을 보여주는 함수
 
    :param mbti: 선택할 MBTI 유형 (ex: "ISFP", "ENTJ")
    :param asc: 오름차순 정렬 여부 (default: 내림차순)
    :param rcnt: 출력할 나라 개수 (default: 10)
    :return: 나라별 MBTI 비율이 정렬된 DataFrame
    """

    # 현재 파일(cli.py)의 디렉토리 경로 (src/mbti)
    # 절대 경로로 불러오기 위해 다음과 같이 경로 설정
    cur_dir = os.path.dirname(os.path.abspath(__file__))

    # 프로젝트 루트 기준으로 data/countries.csv 찾기
    csv_path = os.path.join(cur_dir, "..", "..", "data", "countries.csv")

    # csv 파일 불러오기
    df = pd.read_csv(csv_path)

    # 원하는 데이터로 변환
    converted_df = convert_dataframe(df)
    
    # 입력 받은 데이터
    filtered_df = converted_df[["Country", mbti]]
    sorted_df = filtered_df.sort_values(by=mbti, ascending=asc).reset_index(drop=True).head(rcnt)

    return sorted_df

# 기존 데이터셋에서 원하는 형태로 변환
def convert_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    
    # column 이름을 공통 MBTI 유형으로 변환
    # ISFP-A와 ISFP-T를 합쳐 동일 유형으로 변환
    df.columns = df.columns.str.replace('-A', '').str.replace('-T', '')

    # 같은 MBTI 유형을 그룹화
    # grouby에서 axis=1이 사라질 예정이라 경고문이 나와 수정
    # 기존 코드
    # gdf = df.groupby(df.columns, axis=1).sum()
    gdf = df.T.groupby(df.T.index).sum().T

    # 각 비율을 백분율로 환산
    gdf.iloc[:, 1:] *= 100

    return gdf

def print_check_country_ratio(mbti: str, asc: bool=False, rcnt: int=10):
    result = check_country_mbti_ratio(mbti, asc, rcnt)
    print(result.to_string(index=False))

def entry_point_country():
    typer.run(print_check_country_ratio)
