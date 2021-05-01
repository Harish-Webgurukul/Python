#import Flask class from flask file,render_template and request is function
from flask import Flask,render_template, request, redirect, session
import pymysql.cursors
from datetime import datetime
import os
now = datetime.now()

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='gallery',
                             cursorclass=pymysql.cursors.DictCursor)

#object of class 
app = Flask(__name__)
app.secret_key = "secret_key"

#for user registeration
@app.route('/')
@app.route('/register')
def register():
      return render_template('index.html')


#login page view
@app.route('/login')
def login():
	return render_template('login.html')

#logout
@app.route('/logout')
def logout():
	session.pop('logged_in')
	return render_template('login.html')

#this code will used for checking the login of the user
@app.route('/check_login', methods=['post'])
def check_login():
	email = request.form['email']
	password=request.form['password']
	conn = connection.cursor()
	sql = "SELECT * FROM users WHERE email=%s AND password=%s"
	conn.execute(sql, (email, password))
	result = conn.fetchone()
	if result == None:
		return "Invalid email or password"
	session['logged_in']=True
	return redirect('/view_img')

#whether the user is logged in or not
def is_login():
	try:
		if session['logged_in']==True:
			return True
	except:
		return False


#user fetching data from html and to register it in database
@app.route('/getdata', methods=['post'])
def getdata():
	fname=request.form['fname']
	lname=request.form['lname']
	email=request.form['email']
	password=request.form['password']
	mobile=request.form['mobile']
	cursor = connection.cursor()
	sql = "INSERT INTO users VALUES(NULL, %s, %s, %s, %s, %s, NOW(), NOW())"
	cursor.execute(sql, (fname, lname, email, password, mobile))
	connection.commit()
	return redirect('/view')

#this code is used to view all users data in the database
@app.route('/view')
def view():
	if is_login()==False:
		return redirect('/login')
	conn = connection.cursor()
	sql = "SELECT * FROM users"
	conn.execute(sql)
	result = conn.fetchall()
	return render_template('view.html', result=result)


@app.route('/delete', methods=['get'])
def delete():
	if is_login()==False:
		return redirect('/login')
	user_id = request.args['id']
	conn = connection.cursor()
	sql="DELETE FROM users WHERE id=%s"
	conn.execute(sql, (user_id))
	connection.commit()
	return redirect('/view')


#Image Upload Functionality
@app.route('/imgupload')
def imgupload():
	if is_login()==False:
		return redirect('/login')
	conn = connection.cursor()
	sql = "SELECT * FROM categories"
	conn.execute(sql)
	result = conn.fetchall()
	return render_template('image_upload.html', categories=result)


#uploading the image to static and in the database
@app.route('/imgetdata', methods=['post'])
def imgetdata():
	if is_login()==False:
		return redirect('/login')
	file = request.files['image']
	category_id=request.form['category_id']
	filename=file.filename
	ext = filename.split('.')
	if ext[1]=="jpg" or ext[1]=="png" or ext[1]=="gif":
		img_path = os.path.join('static/uploads/', filename)
		file.save(img_path)
		conn=connection.cursor()
		sql="INSERT INTO images VALUES(NULL, %s, %s, %s, NOW(),NOW())"
		conn.execute(sql, (filename, img_path, category_id))
		connection.commit()
		return redirect('/view_img')
	return "File format Not matched"

#image view in table format
@app.route('/view_img')
def view_img():
	if is_login()==False:
		return redirect('/login')
	conn = connection.cursor()
	sql = "SELECT images.*, categories.category_name FROM images LEFT JOIN categories ON images.category_id=categories.id"
	conn.execute(sql)
	result = conn.fetchall()
	return render_template('view_image.html', result=result)



app.run(debug=True)
