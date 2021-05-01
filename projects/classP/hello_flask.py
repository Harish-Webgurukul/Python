from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
@app.route('/entry')
def entry_page()->'html':
	return render_template('entry.html', the_title='Welcome to search4letters on the Web!')

@app.route('/search4', methods=['POST'])
def harish()->str:
	num1 = int(request.form['num1'])
	num2 = int(request.form['num2'])
	total = num1+num2
	return render_template('output.html', total=total)

app.run(debug=True)