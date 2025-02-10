# Specific_manager
class Specific_manager:
    def __init__(self, db):
        self.db = db

    def get_mbti(self) -> list:
        data = self.db.select_mbti_list()
        data_list = [row[0] for row in data]
    
        return data_list

    def get_countries(self) -> list:
        data = self.db.select_countries_list()
        data_list = [row[0] for row in data]

        return data_list

    def get_specific_data(self, country: str, mbti: str) -> str:
        data = self.db.select_specific_data(country=country, mbti=mbti)
        percentage = data[0][0]

        return f'{country}의 {mbti} 비율은 {percentage}% 입니다.'
    
