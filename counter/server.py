from flask import Flask, render_template, redirect, request, session, url_for
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

def sumSessionsCounter():
    try:
        session['counter']+=1
    except KeyError:
        session['counter'] = 1

@app.route('/')
def index():
    sumSessionsCounter()
    return render_template('index.html')

@app.route('/button_plus2', methods=['POST'])
def return_to_index():
    print request.form
    session['counter'] += 2
    return render_template('index.html')


@app.route('/button_reset', methods=['POST'])
def reset_button():
    print request.form
    session['counter'] = 0
    return redirect('/')



app.run(debug=True)
