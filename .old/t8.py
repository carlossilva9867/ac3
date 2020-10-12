import os
from flask import Flask, jsonify,request
from math import sqrt

app = Flask(__name__)

@app.route('/ac3')
#programacao em python 
def nao_entre_em_panico():

    primos = "Tudo vai dar certo"
    return primos 

if __name__== "__main__":
    port = int(os.environ.get("PORT",500))
    app.run(host='0.0.0.0', port=port)

