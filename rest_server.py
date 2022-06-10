from flask import Flask, json
from flask_cors import CORS

tabela = open('results/items.json')

products = json.load(tabela)

api = Flask(__name__)
CORS(api)

@api.route('/products', methods=['GET'])
def get_companies():
  return json.dumps(products)

if __name__ == '__main__':
    api.run()
