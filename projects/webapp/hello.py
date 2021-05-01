from flask import Flask, render_template, request, redirect
from DBcm import UseDatabase

app = Flask(__name__)
app.config['dbconfig'] = {
							'host':'127.0.0.1',
							'user':'root',
							'password': 'password',
							'database':'proj'
							}

@app.route('/home')
@app.route('/')
def hello()->'html':
	return  render_template('index.html', the_title='Python')

@app.route('/login')
def login()->'html':
	return  render_template('login.html', the_title='Python | Login')

@app.route('/register')
def register()->'html':
	return  render_template('register.html', the_title='Python | Register')

@app.route('/getdata', methods=['POST'])
def getdata()->'html':
	username = request.form['username']
	email = request.form['email']
	password = request.form['password']
	city = request.form['city']
	query = "INSERT INTO users VALUES(null ,%s, %s, %s, %s)"
	with UseDatabase(app.config['dbconfig']) as cursor:
		cursor.execute(query, (username, email, password, city))
	return  redirect('/view')

# Code to delete row of a table
@app.route('/delete', methods=['POST'])
def delete()->'html':
	rowid = request.form['id']
	# concatenation
	query = "DELETE FROM users WHERE id="+rowid
	with UseDatabase(app.config['dbconfig']) as cursor:
		cursor.execute(query)
	return  redirect('/view')

@app.route('/view')
def view()->'html':
	query = "select * from users"
	with UseDatabase(app.config['dbconfig']) as cursor:
		cursor.execute(query)
		res = cursor.fetchall()
	return  render_template('view.html', the_title='Python | View', data=res)


@app.route('/edit', methods=['POST'])
def edit()->'html':
	rowid = request.form['id']
	query = "select * from users where id ="+rowid
	with UseDatabase(app.config['dbconfig']) as cursor:
		cursor.execute(query)
		res = cursor.fetchone()
	return  render_template('edit.html', the_title='Python | View', data=res)

@app.route('/update', methods=['POST'])
def update()->'html':
	rowid = request.form['id']
	username = request.form['username']
	email = request.form['email']
	password = request.form['password']
	city = request.form['city']
	query = "UPDATE users SET username= %s, email=%s, password=%s, city=%s WHERE id=%s"
	with UseDatabase(app.config['dbconfig']) as cursor:
		cursor.execute(query, (username, email, password, city, rowid))
	return  redirect('/view')


app.run(debug=True)
