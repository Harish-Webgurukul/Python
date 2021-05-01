from flask import * 
import os
import mysql.connector

dbconfig = {
	'host':'127.0.0.1',
	'user':'root',
	'password': 'password',
	'database':'proj'
}
conn = mysql.connector.connect(**dbconfig)
cursor = conn.cursor()

app = Flask(__name__)  

@app.route('/')
@app.route('/home')
def upload():  
    return render_template("index.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        path = os.path.join('static/images/',f.filename)
        f.save(path)
        query = "INSERT INTO gallery VALUES(null ,%s, %s, NOW())"
        cursor.execute(query, (f.filename, path))
        conn.commit()
        return render_template("success.html", name = f.filename)  
 
@app.route('/view')
def view():
	query = "SELECT * FROM gallery"
	cursor.execute(query)
	res = cursor.fetchall()
	return render_template("view.html", data = res)



if __name__ == '__main__':  
    app.run(debug = True)  