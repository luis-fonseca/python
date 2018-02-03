# -*- coding: utf-8 -*

import requests
import zipfile
import htmlmin
import shutil
import os

def minifyHTML(file_to_minify):

    output_dir = 'resultados'
    output_file = os.path.join(output_dir, 'lotofacil.min.html')

    print 'Minificando arquivo html ...'
    with open(file_to_minify, 'r') as f:
        input_html = f.read();
        input_html = input_html.decode('iso-8859-1')

        # para não dar problemas com espaços no beautifulsoup
        output_html = htmlmin.minify(input_html)

        with open(output_file, 'w+') as of:
            output_html = output_html.encode('utf8')
            of.write(output_html)


def getResults():

    url_results = "http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_lotfac.zip"
    output_dir = "resultados"
    output_zip = os.path.join(output_dir, 'resultados.zip')
    output_html = os.path.join(output_dir, 'resultados.html')
    html_file = 'D_LOTFAC.HTM'

    response = requests.get(url_results)

    # remove os arquivos do diretorio
    shutil.rmtree(output_dir)
    os.mkdir(output_dir)

    if response.status_code == 200:
        print 'Salvando arquivo zip'
        with open(output_zip, 'wb') as results:
            results.write(response.content)

        print 'Extraindo arquivo de resultados'
        zip = zipfile.ZipFile(output_zip, 'r')
        zip.extract(html_file, output_dir)

        os.rename(os.path.join(output_dir, html_file), output_html)

        minifyHTML(output_html)
    else:
        print("Não foi possível localizar o arquivo de resultados")

    del response

