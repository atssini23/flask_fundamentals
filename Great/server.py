from flask import Flask, render_template, redirect, request, session, url_for
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def route():
    return render_template('index.html', is_correct=None)

@app.route('/', methods=['POST'])
def submit_route():
    str_num = request.form['num']

    if str_num is None or str_num == '':
        return render_template('index.html', is_correct=None)

    num = int(str_num)

    if 'answer' not in session:
        session['answer'] = random.randint(1, 100)

    if num == session['answer']:
        session.pop('answer')
        return render_template('index.html', is_correct=True, num=num)

    return render_template('index.html', is_correct=False, num=session['answer'])

app.run(debug=True)
