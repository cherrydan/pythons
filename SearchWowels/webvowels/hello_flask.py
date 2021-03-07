# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

import vsearch

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return "<h1> Hello world from Flask!</h1>"


@app.route('/search4', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here is your results: '
    results = str(vsearch.search4letters(phrase, letters))

    return render_template('results.html', the_phrase=phrase,
                           the_letters=letters,
                           the_title = title,
                           the_results=results,)


@app.route('/entry')
def entry_page() -> 'html':

    return render_template('entry.html',
                           the_title='Welcome to search4letters on the Web!')


app.run(debug=True)
