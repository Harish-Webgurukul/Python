from flask import Flask, session, render_template, redirect, request
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='password', database=
	'bank')


app = Flask(__name__)

app.secret_key = "Secret"

@app.route('/')
@app.route('/login')
def login()->'str':
	return render_template('index.html')


@app.route('/check', methods=['POST'])
def check()->'str':
	email=request.form['email']
	password=request.form['pass']
	myCursor = conn.cursor()
	sql = "SELECT * FROM customers WHERE email=%s AND password=%s"
	args=(email, password)
	myCursor.execute(sql, args)
	conn.commit()
	results = myCursor.fetchone()
	myCursor.close()
	try:
		if email==results[3]:
			session['logged_in']=True
			return redirect('/welcome')
	except:
		return redirect('/login')
	


@app.route('/welcome')
def welcome()->'str':
	if 'logged_in' in session:
		return render_template('welcome.html')
	else:
		return redirect('/login')

@app.route('/logout')
def logout()->'str':
	session.pop('logged_in')
	return redirect('/login')


if __name__ == '__main__':
	app.run(debug=True)