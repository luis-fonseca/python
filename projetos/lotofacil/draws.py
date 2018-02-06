# -*- coding: utf-8 -*

import sqlite3
import requests
import zipfile
import htmlmin
import shutil
import os
import database
from bs4 import BeautifulSoup

url_draws = "http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_lotfac.zip"
draws_dir = "draws"
filename_zip  = os.path.join(draws_dir, 'resultados.zip')
filename_html = os.path.join(draws_dir, 'resultados.html')
filename_min_html = os.path.join(draws_dir, 'lotofacil.min.html')
extract_html  = 'D_LOTFAC.HTM'

def minifyHTML(file_to_minify):
    """Minifica o arquivo html extraído do arquivo compactado"""

    print('Minificando arquivo html ...')
    with open(filename_html, 'r') as f:
        input_html = f.read();
        #input_html = input_html.decode('iso-8859-1')

        # para não dar problemas com espaços no beautifulsoup
        input_html = htmlmin.minify(input_html)

        with open(filename_min_html, 'w+') as of:
            #input_html = input_html.encode('utf8')
            of.write(input_html)


def getDraws():

    response = requests.get(url_draws)

    if response.status_code == 200:
        print("Preparando diretório ...")

        if os.path.exists(draws_dir):
            shutil.rmtree(draws_dir)

        os.mkdir(draws_dir)

        print('Salvando arquivo zip ...')
        with open(filename_zip, 'wb') as draws:
            draws.write(response.content)

        extract_file(filename_zip)
        minifyHTML(filename_html)
    else:
        print("Não foi possível localizar o arquivo de resultados")

    del response


def extract_file(filename_draws):

    print('Extraindo arquivo de resultados ...')

    zip = zipfile.ZipFile(filename_draws, 'r')
    zip.extract(extract_html, draws_dir)

    os.rename(os.path.join(draws_dir, extract_html), filename_html)


def extract_draws_from_file(filename_html):

    print("Extraindo os resultados do arquivo HTML. Talvez demore um pouco ...")

    with open(filename_min_html, 'r') as handler:
        soup = BeautifulSoup(handler, 'html.parser')

    table = soup.find('table')
    rows = table.find_all('tr')
    draws = {}

    for row in rows:
        if not row.td is None:
            if 'rowspan' in row.td.attrs:
                rowspan_value = row.td.attrs['rowspan']
                cells = row.find_all('td', attrs={'rowspan':rowspan_value})

                numbers = []

                for i in range(2, 17):
                    numbers.append(int(cells[i].text))

                draws[int(cells[0].text)] = [{"date" : cells[1].text, "numbers" : numbers}]


    return draws


def prepare_to_save_the_drawings(draws):
    """Prepara a consulta, antes de salvar os resultados extraídos do arquivo html em um banco de dados."""

    total_de_sorteios = max(draws.keys())

    values = ""
    for i in range(1, total_de_sorteios + 1):
        date = draws[i][0]['date']

        # converte a lista em uma string para salvar no campo numbers da tabela
        numbers = ""
        for j in draws[i][0]['numbers']:
            numbers += str(j) + ","
        numbers = numbers[:-1]

        # valores a serem salvos no banco de dados
        values += "({0}, '{1}', '{2}'), ".format(i, date, numbers)

    sql = "INSERT INTO draws (draw, draw_date, draw_numbers) VALUES {0}".format(values[:-2])

    return sql


#extract_draws_from_file(filename_min_html)
r = extract_draws_from_file(filename_min_html)
s = prepare_to_save_the_drawings(r)
database.insert_rows_in_table(s)
