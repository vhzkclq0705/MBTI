import psycopg
from config.db_config import db_config
from models.mbti import Mbti

# Database
class Database:
    def __init__(self):
        self.conn = psycopg.connect(**db_config)
        self.cursor = self.conn.cursor()

    def execute_query(self, query, data=None):
        if data:
            self.cursor.execute(query, data)
        else:
            self.cursor.execute(query)
        self.conn.commit()

    def select_data(self) -> list:
        query = '''
        SELECT *
        FROM countries_mbti
        '''
        self.execute_query(query)

        return self.cursor.fetchall()

    def select_specific_data(self, country: str, mbti: str) -> list:
        query = '''
        SELECT percentage
        FROM countries_mbti cm
        WHERE cm.country = %s AND cm.mbti = %s;
        '''
        self.execute_query(query, (country, mbti))

        return self.cursor.fetchall()

    def select_mbti_list(self) -> list:
        query = '''
        SELECT DISTINCT mbti
        FROM countries_mbti
        ORDER BY mbti;
        '''
        self.execute_query(query)
        
        return self.cursor.fetchall()

    def select_countries_list(self) -> list:
        query = '''
        SELECT DISTINCT country
        FROM countries_mbti
        ORDER BY country;
        '''
        self.execute_query(query)
        
        return self.cursor.fetchall()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
