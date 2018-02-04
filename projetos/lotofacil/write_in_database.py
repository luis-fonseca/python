import sqlite3
import os

# http://www.carlissongaldino.com.br/post/um-tutorial-passo-passo-para-sqlite-em-python

def create_database():

    database_dir  = "database"
    database_file = os.path.join(database_dir, "results.db")

    if not os.path.exists(database_dir):
        os.mkdir(database_dir)
        conn = sqlite3.connect(database_file)

        cursor = conn.cursor()
        sql = "CREATE TABLE results (draw_number text, draw_date text, numbers text)"

        cursor.execute(sql)


create_database()
