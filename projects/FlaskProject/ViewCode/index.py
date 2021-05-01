from flask import Flask, render_template
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='proj'
                             )



app = Flask(__name__)  #object of Flask


@app.route('/')
@app.route('/home')
def home():
	return render_template('index.html')


@app.route('/view')
def view():
	conn = connection.cursor()
	sql="SELECT users.*, cities.city_name FROM users INNER JOIN cities ON users.city_id = cities.id"
	conn.execute(sql)
	results = conn.fetchall()
	connection.commit()
	return render_template('view.html', results=results)





app.run(debug=True) #run flask