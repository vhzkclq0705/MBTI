import pandas as pd

# Data_manager
class Data_manager:
    def __init__(self, db):
        self.db = db

    def get_table(self) -> pd.DataFrame:
        data = self.db.select_data()

        df = (
            pd.DataFrame(data, columns=['country', 'mbti', 'percentage'])
            .pivot_table(index='country', columns='mbti', values='percentage')
            .reset_index()
            .sort_values(by='country')
            .reset_index(drop=True)
        )
        
        return df
