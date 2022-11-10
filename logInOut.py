from flask import Flask, render_template, redirect, url_for,request,session
from flask_mysqldb import MySQL
import MySQLdb
app = Flask(__name__)
app.secret_key = "12456789"
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"]= "root"
app.config["MYSQL_PASSWORD"] = "Ashish12345@"
app.config["MYSQL_DB"] = "loginlogout"

db = MySQL(app)
@app.route('/',methods=('GET', 'POST'))
def index():
    if request.method == "POST":
        if 'username' in request.form and 'password' in request.form:
            username = request.form["username"]
            password = request.form['password']
            cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("SELECT * FROM lgin WHERE username=%s AND password = %s",(username,password))
            info = cursor.fetchone()
            if info is not None:
                if info["username"] == username and info['password'] == password:
                    session['loginsuccess']=True
                    return redirect(url_for('profile'))
            else:
                return redirect(url_for('index'))
    return render_template("loginXS.html")

@app.route('/new',methods=['GET','POST'])
def new_user():
    if request.method == "POST":
        if "one" in request.form and "two" in request.form and "three" in request.form:
            username = request.form['one']
            email = request.form['two']
            password = request.form['three']
            id = "2"
            cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("INSERT INTO lgin(username,password) VALUES (%s,%s)",(username,password))
            db.connection.commit()
            return redirect(url_for('index'))
        return render_template('registrationXS.html')

@app.route('/new/profile')
def profile():
    if session['loginsuccess'] == True:
        return render_template("logoutXS.html")

@app.route('/new/logout')
def logout():
    session.pop('loginsuccess',None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
