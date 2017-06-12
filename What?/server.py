from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def route():
  return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    print "YoUr NaMe iS!"
    name = request.form['name']
    return render_template('process.html', name = name)

app.run(debug=True)
