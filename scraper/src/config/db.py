from os import getenv
import mysql.connector

# import config.settings

class Db:
    def __init__(self):
        self.connection = mysql.connector.connect(host=getenv('HOST'),
                                            user=getenv('USER'),
                                            password=getenv('PASSWORD'),
                                            database=getenv('DATABASE'),
                                            autocommit=True
                                        )

        self.cursor = self.connection.cursor()

    def execute(self, query, params=None):
       self.cursor.execute(query, params)
       return self.cursor
