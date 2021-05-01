from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import os
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='password', database=
	'bank')

app = Flask(__name__)

app.config['images']="Static/images"

@app.route('/upload')
def upload_file()->'html':
   return render_template('upload.html')



@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
   if request.method == 'POST':
      file = request.files['file']
      file.save(os.path.join(app.config['images'], secure_filename(file.filename)))
      myCursor = conn.cursor()
      sql = "INSERT INTO gallery VALUES(NULL, %s, NOW(), NOW())"
      args = (file.filename)
      myCursor.execute(sql, args)
      conn.commit()
      myCursor.close()
      return redirect('/view')

@app.route('/view')
def view()->'html':
	sql="SELECT * FROM gallery"
	myCursor = conn.myCursorr()
	myCursor.execute(sql)
	conn.commit()
	results = myCursor.fetchall()
	myCursor.close()
	return render_template('view.html', data=results)



if __name__ == '__main__':
   app.run(debug = True)