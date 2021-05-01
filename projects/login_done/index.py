from flask import Flask, session, render_template, redirect, request

from checker import check_logged_in

app = Flask(__name__)

@app.route('/')
def hello()->str:
	return 'Hello from simple webapp'

@app.route('/page1')
@check_logged_in
def page1()->str:
	return 'this is page1'

@app.route('/login')
def do_login()->'html':
	session['logged_in'] = True
	return render_template('login.html')


@app.route('/logout')
def do_logout()->str:
	session.pop('logged_in')
	return redirect('/login')

app.secret_key = "SecretKey"


if __name__ == '__main__':
	app.run(debug=True)

