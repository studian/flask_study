# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_root():
    return "<h1>hellow world!</h1>"

@app.route("/sub01")
def hello_sub01():
    return "<h2>sub01: hellow world!</h2>"

@app.route("/sub02")
def hello_sub02():
    return "<h3>sub02: hellow world!</h3>"

if __name__ == '__main__':
    app.run()

