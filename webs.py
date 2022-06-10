from urllib.request import urlopen
from bs4 import BeautifulSoup
from numpy import product
import requests
import pandas as pd
import json

folder_path = "results/"

url = "https://www.cepea.esalq.usp.br/br/widgetproduto.js.php?"

params = "id_indicador%5B%5D=54&id_indicador%5B%5D=91&id_indicador%5B%5D=leitep&id_indicador%5B%5D=159"

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.79 Safari/537.36'}

page = requests.get(url+params, headers = headers)

soup = BeautifulSoup(page.content, "html.parser")

table_body = soup.find('tbody')
linhas = table_body.find_all('tr')

items = []
for i in linhas:
    children = i.findChildren("td")
    date = children[0].text
    product_type = children[1].text
    price = children[2].text
    new_item = {"date": date, "product": product_type, "price": price}
    items.append(new_item)

json_file = json.dumps(items, indent=2)

new_file = open("results/items.json", "w")
new_file.write(json_file)

# df = pd.DataFrame(items)

# df.head()

#df.to_json(folder_path + 'tabela.json', indent=2)
#df.to_html(folder_path + 'tabela.html')
#df.to_excel(folder_path + 'tabela.xlsx')
