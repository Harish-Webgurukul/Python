from flask import Flask, render_template, request
import pymysql.cursors
import os
# Connect to the database

app = Flask(__name__)  #object of Flask


@app.route('/')
@app.route('/home')
def home():
	return render_template('index.html')


@app.route('/getdata', methods=['post'])
def getdata():
	file = request.files['data']
	filename=file.filename
	ext = filename.split('.')
	if ext[1]=="jpg" or ext[1]=="png" or ext[1]=="gif":
		file.save(os.path.join('static/uploads/', filename))
		return "File Uploaded"
	return "File format Not matched"


@app.route('/view')
def view():
	return render_template('view.html')

app.run(debug=True) #run flask