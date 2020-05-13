from flask import request, redirect, session, url_for
from flask import render_template
from flask_mysqldb import MySQL
import mysql.connector
# from database import suma 
# from database import hello

from database import *


@app.route("/") # A decorator; when the user goes to the route `/`, exceute the function immediately below
def index():
    #createTable()   
    #print('1',flush=True)
    #print(app.config)
    if session.get('user',None) is not None:
        user=session['user']
        return render_template('public/index.html',user=user)
    else:
        return render_template('public/index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    session.clear()

    if request.method=='GET':
        return render_template('public/login.html')
    if request.method == 'POST':
        name=request.form['login']
        password=request.form['password']
         
        # Ensure username was submitted
        if not request.form.get("login"):
            return "must provide username"

        # Ensure password was submitted
        elif not request.form.get("password"):
            return "must provide password"

        # Query database for username
        if loginUser(name,password):
            return redirect(url_for('profile'))
        else:
            return redirect('/')
    


@app.route('/register', methods=['GET','POST'])
def register():
    
    if request.method == 'POST':
        name = request.form['name']
        password=request.form['password']
        email=request.form['email']
        exists = createUser(name,password,email)
        

        if exists: 
            return redirect('/login')
            print('entered function')
        else:
            return redirect('/')
        
    elif request.method == 'GET':
        return render_template('public/register.html')
    

@app.route('/profile')
#dynamic urls for created profiles
def profile():
    #if 'user' in session:
    if session.get('user',None) is not None:
        userid=session['user']
        #get user from db
        result = getUser(userid)
        return render_template('/public/profile.html',user=result[1],email=result[3])
    else:
        return redirect(url_for("login"))
    #if username in users:
     #   print
    

@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect('/')