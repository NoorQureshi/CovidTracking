from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", total=load['cases'], recover=load['recovered'], deaths=load['deaths'], countries=l)

# Scrap Data

source = requests.get('https://corona.lmao.ninja/v2/all')
load = json.loads(source.text)

s = requests.get('https://disease.sh/v2/countries')
l = json.loads(s.text)

if __name__ == "__main__":
    app.run(debug=True)