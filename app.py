from flask import Flask, render_template, request, flash, redirect, url_for, session
import requests
import os

app = Flask(__name__)

@app.route('/')
def lista_cocktails():
    response = requests.get('https://www.thecocktaildb.com/api/json/v1/1/search.php?f=a')
    cocktails = response.json()['drinks']
    return render_template('lista_cocktails.html', cocktails=cocktails)

@app.route('/cocktail/<id>')
def cocktail_detalle(id):
    response = requests.get(f'https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={id}')
    cocktail = response.json()['drinks'][0]
    return render_template('cocktail_detalle.html', cocktail=cocktail)
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7000)
