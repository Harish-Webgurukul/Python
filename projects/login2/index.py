from flask import Flask, session, render_template, redirect, request
from checker import check_logged_in
from checker import isadmin

from DBcm import UseDatabase

app= Flask(__name__)
app.config['dbconfig'] = {
							'host':'127.0.0.1',
							'user':'root',
							'password': 'password',
							'database':'proj'
							}


@app.route('/')
@app.route('/login')
def login()-> 'html':
	return render_template('login.html', title='Login Form')

@app.route('/check', methods=['POST'])
def check()-> 'html':
	email = request.form['email']
	password = request.form['password']
	query = "SELECT * FROM users WHERE email=%s AND password=%s"
	with UseDatabase(app.config['dbconfig']) as cursor:
		cursor.execute(query, (email, password))
		res = cursor.fetchone()
		try:
			if email in res:
				session['logged_in'] = True
				if 1 in res:
					session['admin'] = True
					return redirect('/dashboard')
				if 0 in res:
					return redirect('/welcome')
		except Exception as e:
			return redirect('/login')

@app.route('/welcome')
@check_logged_in
def welcome()-> 'html':
	return render_template('welcome.html', title='Welcome')

@app.route('/logout')
def logout()-> 'html':
	try:
		session.pop('logged_in')
		session.pop('admin')
		return redirect('/login')
	except Exception as e:
		return redirect('/login')

# Admin pane Code
@app.route('/dashboard')
@check_logged_in
@isadmin
def dashboard()-> 'html':
	return render_template('dashboard.html', title='Dashboard')


app.secret_key="SecretKey"

if __name__ =='__main__':
	app.run(debug=True)