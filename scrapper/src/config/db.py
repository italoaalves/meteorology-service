from os import getenv
import pymysql.cursors
import pymysql

class Db:
    def __init__(self):
        self.connection = pymysql.connect(host= getenv('HOST'),
                                            user = getenv('USER'),
                                            password = getenv('PASSWORD'),
                                            db = getenv('DB'),
                                            charset = 'utf8mb4',
                                            cursorclass = pymysql.cursors.DictCursor)
        self.cursor = self.connection.cursor()

    def execute(self, query, params):
       self.cursor.execute(query, params)
       return self.cursor

    def __del__(self):
        self.connection.close()
