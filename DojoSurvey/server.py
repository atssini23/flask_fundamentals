from flask import Flask, render_template, request, redirect,flash
app = Flask(__name__)
app.secret_key ="shhhhh"

@app.route('/')
def route():
  return render_template('index.html')

@app.route('/result', methods = ['POST'])
def result():
    print request.form
    print "Got Post Info"
    name = request.form['name']
    is_valid = True
    if name is None or name == '':
        flash('Name is required')
        is_valid = False
    city = request.form['city']
    language = request.form['language']
    comment = request.form['comment']
    if comment is None or comment == '':
        flash('Comment is required')
        is_valid = False
    if len(comment)>120:
        flash('Less then 120 characters')
        is_valid = False
    if not is_valid:
        return render_template('index.html',name=name,city=city,language=language,comment=comment)

    return render_template('result.html',name=name,city=city,language=language,comment=comment)

app.run(debug=True)
