import psycopg2


class PostgreSQL_Database():
    def __init__(self):
        self.db = psycopg2.connect(host='localhost', dbname='se_db', user='se_project', password='se_project', port=5432)
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()
        self.cursor.close()

    def execute(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row

    def commit(self):
        self.cursor.commit()
