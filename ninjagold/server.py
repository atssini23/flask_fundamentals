from flask import Flask, render_template, redirect, request, session, url_for
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def route():
    if 'gold' not in session:
        session['gold'] = 0
    if 'message' not in session:
        session['message'] = ''
    return render_template('index.html', gold=session['gold'])

@app.route('/process_money', methods=['POST'])
def submit_route():
    message = session['message']
    gold = session['gold']
    earn = 0

    if gold is None:
        gold = 0
    else:
        gold = int(gold)

    building = request.form['building']

    if building == 'farm':
        earn = random.randint(10,20)
        gold += earn
    elif building == 'cave':
        earn = random.randint(5,10)
        gold += earn
    elif building  == 'house':
        earn = random.randint(2,5)
        gold += earn
    elif building == 'casino':
        earn = random.randint(-50,50)
        gold += earn

    session['gold'] = gold
    message = message + "\nEarns " + str(earn) + " gold from the " + building

    session['message'] = message

    return render_template('index.html', gold=gold,activities=message)



app.run(debug=True)
