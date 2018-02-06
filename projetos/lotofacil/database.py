# -*- coding: utf-8 -*-

import sqlite3
import os
#import results

database_dir = "db"
database_name = "draws.db"
relative_path = os.path.join(database_dir, database_name)

def prepare_environment():
    """Prepara o banco de dados, salva os resultados e realiza
    as estatísticas iniciais. Usado na primeira que vez que o
    programa é iniciado."""

    print("Criando a base de dados ...")
    conn = create_database()

    print("Criando as tabelas ...")
    create_tables(conn)


def create_database():
    """Cria o banco de dados se não existir"""

    if not os.path.exists(database_dir):
        os.mkdir(database_dir)
    else:
        try:
            os.remove(relative_path)
        except PermissionError as permission:
            msg = "Não foi possível remover o arquivo de banco de dados. "
            msg += "Arquivo em uso."

            print(msg)
            exit()

    return connect_in_database(relative_path)


def create_tables(conn):
    """Cria as tabelas de sorteios e estatísticas."""

    sql_draws = """CREATE TABLE IF NOT EXISTS draws (draw integer, draw_date varchar(10),
            draw_numbers varchar(50))"""

    sql_statistics = """CREATE TABLE IF NOT EXISTS statistics (
        total_even_numbers INTEGER,
        total_odd_numbers INTEGER,
        most_drawn_number INTEGER,
        less_drawn_number INTEGER,
        most_drawn_numbers VARCHAR(25),
        less_drawn_numbers VARCHAR(25))"""

    cursor = conn.execute(sql_draws)
    cursor = conn.execute(sql_statistics)


def database_exists(name):
    """Verifica se o banco de dados foi criado."""

    return os.path.isfile(name)


def table_exists(name):
    """Verifica se uma determinada tabela existe."""

    sql = "SELECT name FROM sqlite_master WHERE type='table' "
    sql += "and name='{0}'".format(name)

    if database_exists(relative_path):
        conn = sqlite3.connect(relative_path)
        cursor = conn.execute(sql)

        if not cursor.fetchone() is None:
            return True

    return False


def connect_in_database(path):
    """Se conecta ao um banco de dados"""

    print("Conectando ao banco de dados ...")
    conn = sqlite3.connect(path)
    return conn


def insert_rows_in_table(sql):
    """Insere os registros em uma tabela."""

    try:
        conn = connect_in_database(relative_path)

        print("Salvando os resultados no banco de dados. Talvez demore um pouco ...")
        cursor = conn.cursor()
        cursor.execute(sql)

        print("Dados salvos ...")
        conn.commit()
    except sqlite3.OperationalError as error:
        msg = "Não foi possível inserir os registros. Banco de dados bloqueado por outro processo. \n"
        msg += "Nada feito."
        print(msg)
