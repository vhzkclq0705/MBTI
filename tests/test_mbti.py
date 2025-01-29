from mbti.cli import check_country_mbti_ratio
import pandas as pd
import pytest

def test_check_country_mbti_ratio():
    mbti = "ISFP"
    rcnt = 10
    df = check_country_mbti_ratio(mbti=mbti, rcnt=rcnt)

    assert isinstance(df, pd.DataFrame)
    assert mbti in df.columns
