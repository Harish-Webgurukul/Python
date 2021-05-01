from flask import Flask, render_template

app = Flask(__name__)  #object of Flask


@app.route('/')
@app.route('/home')
def home():
	return render_template('index.html')


@app.route('/view')
def view():
	return render_template('view.html')

app.run(debug=True) #run flask