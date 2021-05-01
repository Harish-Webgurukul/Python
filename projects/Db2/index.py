#import Flask class from flask file,render_template and request is function
from flask import Flask,render_template, request, redirect
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='proj',
                             cursorclass=pymysql.cursors.DictCursor)

#object of class 
app = Flask(__name__)

@app.route('/')
def index():
      return 'welcome to Home page'

@app.route('/register')
def register():
      return render_template('index.html')

@app.route('/getdata', methods=['post'])
def getdata():
	email=request.form['email']
	password=request.form['password']
	city=request.form['city']
	mobile=request.form['mobile']
	with connection.cursor() as cursor:
		sql = "INSERT INTO users VALUES(NULL, %s, %s, %s, %s)"
		cursor.execute(sql, (email, password, city, mobile))
		connection.commit()
	return redirect('/view')

@app.route('/view')
def view():
	with connection.cursor() as cursor:
		sql = "SELECT * FROM users"
		cursor.execute(sql)
		result = cursor.fetchall()
	return render_template('view.html', result=result)

@app.route('/edit', methods=['get'])
def edit():
	user_id = request.args['id']
	with connection.cursor() as cursor:
		sql = "SELECT * FROM users WHERE id=%s"
		cursor.execute(sql, (user_id))
		result = cursor.fetchone()
	return render_template('edit.html', result=result)

@app.route('/delete', methods=['get'])
def delete():
	user_id = request.args['id']
	with connection.cursor() as cursor:
		sql="DELETE FROM users WHERE id=%s"
		cursor.execute(sql, (user_id))
		connection.commit()
	return redirect('/view')




app.run(debug=True)
