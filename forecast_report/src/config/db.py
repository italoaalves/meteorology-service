import pymysql.cursors
import pymysql
from settings import DATABASE

class Db:
    def __init__(self):
        self.connection = pymysql.connect(host= DATABASE['HOST'],
                                            user = DATABASE['USER'],
                                            password = DATABASE['PASSWORD'],
                                            db = DATABASE['DB'],
                                            charset = 'utf8mb4',
                                            cursorclass = pymysql.cursors.DictCursor)
        self.cursor = self.connection.cursor()

    def execute(self, query, params):
       self.cursor.execute(query, params)
       return self.cursor

    def table_exists(table_name):
        self.execute(f'''SELECT EXISTS (
                            SELECT
                                `{table_name}`
                            FROM
                            information_schema.TABLES
                            WHERE
                            TABLE_SCHEMA LIKE 'music' AND
                                TABLE_TYPE LIKE 'BASE TABLE' AND
                                `{table_name}` = 'Artists'
                        );'''
                    )

    def __del__(self):
        self.connection.close()
