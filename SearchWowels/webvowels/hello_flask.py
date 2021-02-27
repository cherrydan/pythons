# -*- coding: utf-8 -*-

from flask import Flask

import vsearch

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return "<h1> Hello world from Flask!</h1>"


@app.route('/search4')
def do_search() -> str:
    return str(vsearch.search4letters('life, the universe and everything', repr('eiru,!')))


app.run()
