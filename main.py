from flask import Flask,request, render_template, redirect

import requests
import os


app = Flask(__name__)

class Busca:
    def __init__(self, cep, logradouro, bairro, localidade,uf):
        self.cep = cep
        self.logradouro = logradouro
        self.bairro = bairro
        self.localidade = localidade
        self.uf = uf


@app.route('/', methods = ['GET', 'POST'])
def index():
    ceps = []
    if request.method == 'POST':
        cep = request.form['cep']

        requisicao = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))

        if requisicao.status_code != 200:
            return render_template('teste.html')


        endereco = requisicao.json()

        novojogo1 = Busca(endereco['cep'], endereco['logradouro'], endereco['bairro'], endereco['localidade'],
                          endereco['uf'])
        ceps.insert(0, novojogo1)
        if len(ceps) > 1:
            ceps.pop(1)
        return render_template('teste.html', ceps=ceps)
    else:
        return render_template('teste.html',ceps=ceps)



if __name__ == '__main__':

    app.run(debug=True, port = int(os.environ.get("PORT", 17995)))

