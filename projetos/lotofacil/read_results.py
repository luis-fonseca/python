# -*- coding: utf-8 -*

from bs4 import BeautifulSoup
import os

url_results = os.path.join('resultados', 'lotofacil.min.html')
with open(url_results, 'r', encoding='utf8') as handler:
    soup = BeautifulSoup(handler, 'html.parser')

#html = """<table border=0 cellspacing=1 cellpadding=0 width=3080> <tr> <th width=50 height=20 bgcolor=#A55592><small><font face=Arial color=#FFFFFF>Concurso</font></small></th> <th width=130 height=20 bgcolor=#A55592><small><font face=Arial color=#FFFFFF>Data Sorteio</font></small></th> <th width=60 height=20 bgcolor=#A55592><small><font face=Arial color=#FFFFFF>Bola1</font></small></th> <th width=60 height=20 bgcolor=#A55592><small><font face=Arial color=#FFFFFF>Bola2</font></small></th> <th width=60 height=20 bgcolor=#A55592><small><font face=Arial color=#FFFFFF>Bola3</font></small></th> <th width=60 height=20 bgcolor=#A55592><small><font face=Arial color=#FFFFFF>Bola4</font></small></th> <th width=60 height=20 bgcolor=#A55592><small><font face=Arial color=#FFFFFF>Bola5</font></small></th> <th width=60 height=20 bgcolor=#A55592><small><font face=Arial color=#FFFFFF>Bola6</font></small></th> <th width=60 height=20 bgcolor=#A55592><small><font face=Arial color=#FFFFFF>Bola7</font></small></th> <th width=60 height=20 bgcolor=#A55592><small><font face=Arial color=#FFFFFF>Bola8</font></small></th> <th width=60 height=20 bgcolor=#A55592><small><font face=Arial color=#FFFFFF>Bola9</font></small></th> <th width=60 height=20 bgcolor=#A55592><small><font face=Arial color=#FFFFFF>Bola10</font></small></th> <th width=60 height=20 bgcolor=#A55592><small><font face=Arial color=#FFFFFF>Bola11</font></small></th> <th width=60 height=20 bgcolor=#A55592><small><font face=Arial color=#FFFFFF>Bola12</font></small></th> <th width=60 height=20 bgcolor=#A55592><small><font face=Arial color=#FFFFFF>Bola13</font></small></th> <th width=60 height=20 bgcolor=#A55592><small><font face=Arial color=#FFFFFF>Bola14</font></small></th> <th width=60 height=20 bgcolor=#A55592><small><font face=Arial color=#FFFFFF>Bola15</font></small></th> <th width=80 height=20 bgcolor=#A55592><small><font face=Arial color=#FFFFFF>Arrecadacao_Total</font></small></th> <th width=80 height=20 bgcolor=#A55592><small><font face=Arial color=#FFFFFF>Ganhadores_15_N�meros</font></small></th> <th width=95 height=20 bgcolor=#A55592><small><font face=Arial color=#FFFFFF>Cidade</font></small></th> <th width=95 height=20 bgcolor=#A55592><small><font face=Arial color=#FFFFFF>UF</font></small></th> <th width=80 height=20 bgcolor=#A55592><small><font face=Arial color=#FFFFFF>Ganhadores_14_N�meros</font></small></th> <th width=80 height=20 bgcolor=#A55592><small><font face=Arial color=#FFFFFF>Ganhadores_13_N�meros</font></small></th> <th width=80 height=20 bgcolor=#A55592><small><font face=Arial color=#FFFFFF>Ganhadores_12_N�meros</font></small></th> <th width=80 height=20 bgcolor=#A55592><small><font face=Arial color=#FFFFFF>Ganhadores_11_N�meros</font></small></th> <th width=80 height=20 bgcolor=#A55592><small><font face=Arial color=#FFFFFF>Valor_Rateio_15_N�meros</font></small></th> <th width=80 height=20 bgcolor=#A55592><small><font face=Arial color=#FFFFFF>Valor_Rateio_14_N�meros</font></small></th> <th width=80 height=20 bgcolor=#A55592><small><font face=Arial color=#FFFFFF>Valor_Rateio_13_N�meros</font></small></th> <th width=80 height=20 bgcolor=#A55592><small><font face=Arial color=#FFFFFF>Valor_Rateio_12_N�meros</font></small></th> <th width=80 height=20 bgcolor=#A55592><small><font face=Arial color=#FFFFFF>Valor_Rateio_11_N�meros</font></small></th> <th width=80 height=20 bgcolor=#A55592><small><font face=Arial color=#FFFFFF>Acumulado_15_N�meros</font></small></th> <th width=80 height=20 bgcolor=#A55592><small><font face=Arial color=#FFFFFF>Estimativa_Premio</font></small></th> <th width=80 height=20 bgcolor=#A55592><small><font face=Arial color=#FFFFFF>Valor_Acumulado_Especial</font></small></th> </tr><tr bgcolor=#D5BCCD> <td rowspan=5>1</td><td rowspan=5>29/09/2003</td><td rowspan=5>18</td><td rowspan=5>20</td><td rowspan=5>25</td><td rowspan=5>23</td><td rowspan=5>10</td><td rowspan=5>11</td><td rowspan=5>24</td><td rowspan=5>14</td><td rowspan=5>06</td><td rowspan=5>02</td><td rowspan=5>13</td><td rowspan=5>09</td><td rowspan=5>05</td><td rowspan=5>16</td><td rowspan=5>03</td><td rowspan=5>0,00</td><td rowspan=5>5</td><td></td><td>BA </td><td rowspan=5>154</td><td rowspan=5>4645</td><td rowspan=5>48807</td><td rowspan=5>257593</td><td rowspan=5>49.765,82</td><td rowspan=5>689,84</td><td rowspan=5>10,00</td><td rowspan=5>4,00</td><td rowspan=5>2,00</td><td rowspan=5>0,00</td><td rowspan=5>0,00</td><td rowspan=5>0,00</td></tr><tr bgcolor=#D5BCCD><td></td><td>PR </td></tr><tr bgcolor=#D5BCCD><td></td><td>SP </td></tr><tr bgcolor=#D5BCCD><td></td><td>SP </td></tr><tr bgcolor=#D5BCCD><td></td><td>SP </td></tr><tr> <td rowspan=1>2</td><td rowspan=1>06/10/2003</td><td rowspan=1>23</td><td rowspan=1>15</td><td rowspan=1>05</td><td rowspan=1>04</td><td rowspan=1>12</td><td rowspan=1>16</td><td rowspan=1>20</td><td rowspan=1>06</td><td rowspan=1>11</td><td rowspan=1>19</td><td rowspan=1>24</td><td rowspan=1>01</td><td rowspan=1>09</td><td rowspan=1>13</td><td rowspan=1>07</td><td rowspan=1>0,00</td><td rowspan=1>1</td><td></td><td>SP </td><td rowspan=1>184</td><td rowspan=1>6232</td><td rowspan=1>81252</td><td rowspan=1>478188</td><td rowspan=1>596.323,70</td><td rowspan=1>1.388,95</td><td rowspan=1>10,00</td><td rowspan=1>4,00</td><td rowspan=1>2,00</td><td rowspan=1>0,00</td><td rowspan=1>0,00</td><td rowspan=1>0,00</td></tr>"""
#soup = BeautifulSoup(html, 'html.parser')

print("Lendo o arquivo arquivo de resultados ...")

table = soup.find('table')
rows = table.find_all('tr')
results = {}

for row in rows:
    if not row.td is None:
        if 'rowspan' in row.td.attrs:
            rowspan_value = row.td.attrs['rowspan']
            cells = row.find_all('td', attrs={'rowspan':rowspan_value})

            numbers = []
            for i in range(2, 17):
                numbers.append(cells[i].text)

            results[cells[0].text] = [{"date" : cells[1].text, "numbers" : numbers}]



print(results)
