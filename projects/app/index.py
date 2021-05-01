from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def hello()->'html':
	data="PHP"
	return render_template('index.html', lang=data)

@app.route('/calculate')
def calculate()->'html':
    return render_template('add.html')


@app.route('/getdata', methods=['POST'])
def getdata()->'html':
	num1 = int(request.form['num1'])
	num2 = int(request.form['num2'])
	op = int(request.form['op'])
	if op==1:
		total = num1+num2
		para="Addition"
	elif op==2:
		total = num1-num2
		para="Substraction"
	elif op==3:
		total = num1/num2
		para="Division"
	elif op==4:
		total = num1*num2
		para="Multiplication"
	else:
		total="Invalid Input"
	return render_template('getdata.html', total=total, para=para)

app.run(debug=True)	