import psycopg
from config.db_config import db_config

# Database
class Database:
    def __init__(self):
        self.conn = psycopg.connect(**db_config)
        self.cursor = self.conn.cursor()

    def execute_query(self, query, data=None):
        if data:
            self.cursor.executemany(query, data)
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

    def close_connection(self):
        self.cursor.close()
        self.conn.close()
