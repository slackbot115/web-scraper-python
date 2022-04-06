from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import pandas as pd

folder_path = "results/"

url = "https://www.cepea.esalq.usp.br/br/widgetproduto.js.php?"

params = "id_indicador%5B%5D=54&id_indicador%5B%5D=91&id_indicador%5B%5D=leitep"

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.79 Safari/537.36'}

page = requests.get(url+params, headers = headers)

soup = BeautifulSoup(page.content, "html.parser")

table_body = soup.find('tbody')
linhas = table_body.find_all('tr')

data, produto_tipo, preco = [], [], []
for i in linhas:
    children = i.findChildren("td")
    data.append(children[0].text)
    produto_tipo.append(children[1].text)
    preco.append(children[2].text)

df = pd.DataFrame({'Data': data, 'Produto': produto_tipo, 'Preço': preco})

df.head()

# df.to_json(folder_path + 'tabela.json')
# df.to_html(folder_path + 'tabela.html')
df.to_excel(folder_path + 'tabela.xlsx')
