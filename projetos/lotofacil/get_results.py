import requests
import zipfile
import io

url = "http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_lotfac.zip"
output = "resultados"

response = requests.get(url)

if response.status_code == 200:
    zip_response = zipfile.ZipFile(io.BytesIO(response.content))
    zip_response.extractall(output)
else:
    print("Não foi possível localizar o arquivo de resultados")

del response
