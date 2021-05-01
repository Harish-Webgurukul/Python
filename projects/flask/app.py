from flask import *
import pymysql

#connection
conn= pymysql.connect(host="localhost", user="root", password="", db="proj")
#connection= pymysql.connect(host="localhost", user="examzest_examzest", password="XyI%?H~aDO)D", db="examzest_proj",cursorclass=pymysql.cursors.DictCursor)
#create object of the Flask File
app = Flask(__name__)



#@app is the decorator which is used to view function in url
@app.route('/')
def index():
	return render_template('register.html')


@app.route('/getdata', methods=['post'])
def getdata():
	username=request.form['username']
	email=request.form['email']
	password=request.form['password']
	city=request.form['city']
	cursor=conn.cursor()
	sql="INSERT INTO users VALUES(NULL, %s,%s,%s,%s)"
	cursor.execute(sql, (username, email, password, city))
	conn.commit()
	return redirect('/myapp/view')

@app.route('/view')
def view():
	cursor=conn.cursor()
	sql="SELECT users.*, cities.city_name FROM users INNER JOIN cities ON users.city_id=cities.id"
	cursor.execute(sql)
	results=cursor.fetchall()
	conn.commit()
	return render_template('view.html', results=results)


@app.route('/delete')
def delete(methods=['get']):
	user_id=request.args['id']
	cursor=conn.cursor()
	sql = "DELETE FROM users WHERE id=%s"
	cursor.execute(sql, (user_id))
	conn.commit()
	return redirect('/view')

@app.route('/edit')
def edit(methods=['get']):
	user_id=request.args['id']
	cursor=conn.cursor()
	sql = "SELECT * FROM users WHERE id=%s"
	cursor.execute(sql, (user_id))
	results=cursor.fetchone()
	conn.commit()
	return render_template('edit.html', data=results)

@app.route('/update')
def update(methods=['get']):
	user_id = request.args['id']
	username=request.args['username']
	email=request.args['email']
	password=request.args['password']
	city=request.args['city']
	cursor=conn.cursor()
	sql = "UPDATE users SET username=%s, email=%s, password=%s, city_id=%s WHERE id=%s"
	cursor.execute(sql, (username, email, password, city, user_id))
	conn.commit()
	return redirect('/view')



#below line is used to run the Flask Program
if __name__=='__main__':
	app.run(debug=True)
