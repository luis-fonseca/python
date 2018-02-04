# -*- coding: utf-8 -*

import requests
import zipfile
import htmlmin
import shutil
import os

url_draws = "http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_lotfac.zip"
draws_dir = "resultados"
filename_zip  = os.path.join(draws_dir, 'resultados.zip')
filename_html = os.path.join(draws_dir, 'resultados.html')
filename_min_html = os.path.join(draws_dir, 'lotofacil.min.html')
extract_html  = 'D_LOTFAC.HTM'

def minifyHTML(file_to_minify):
    """Minifica o arquivo html extraído do arquivo compactado"""

    print 'Minificando arquivo html ...'
    with open(filename_html, 'r') as f:
        input_html = f.read();
        input_html = input_html.decode('iso-8859-1')

        # para não dar problemas com espaços no beautifulsoup
        input_html = htmlmin.minify(input_html)

        with open(filename_min_html, 'w+') as of:
            input_html = input_html.encode('utf8')
            of.write(input_html)


def getResults():

    response = requests.get(url_draws)

    shutil.rmtree(draws_dir)
    os.mkdir(draws_dir)

    if response.status_code == 200:
        print 'Salvando arquivo zip ...'
        with open(filename_zip, 'wb') as results:
            results.write(response.content)

        print 'Extraindo arquivo de resultados ...'
        zip = zipfile.ZipFile(filename_zip, 'r')
        zip.extract(extract_html, draws_dir)

        os.rename(os.path.join(draws_dir, extract_html), filename_html)

        minifyHTML(filename_html)
    else:
        print("Não foi possível localizar o arquivo de resultados")

    del response


def extract_results(filename_draws):
    pass
