#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

DEVELOPMENT_ENV = True

app = Flask(__name__)

app_data = {
    "name":         "Ukrainian Transliteration",
    "description":  "This is a simple algorithm that transliterates your name using dictionary provided by Ukrainian Goverment",
    "author":       "Bob Volskiy",
    "html_title":   "Ukrainian Transliteration",
    "keywords":     "flask, webapp, transliteration, ukraine"
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('Convert') == 'Convert':
            print(request.form.get('name'),request.form.get('surname'))
    return render_template('index.html', app_data=app_data)

if __name__ == '__main__':
    app.run(debug=DEVELOPMENT_ENV)