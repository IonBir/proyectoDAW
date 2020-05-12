from app import app
from flask import Flask, session,redirect
from flask_session import Session
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from tempfile import mkdtemp
import mysql.connector

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345'
app.config['MYSQL_DB'] = 'proyecto'
#app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['MYSQL_PORT'] = 3305
mysql = MySQL(app)

#key for sessions
app.config['SECRET_KEY']='etc_sa354Aasdf23'


def createUser(name,password,email):
    #mysql = MySQL(app)
    exists=False
    cur = mysql.connection.cursor()
    #cur = mysql.connection.cursor()
    sql='SELECT * FROM usuario WHERE email = %s'
    cur.execute(sql,[email])
    msg=cur.fetchone()
    if not msg:
         hashed=generate_password_hash(password)
         sqls='INSERT INTO usuario(name,password,email) VALUES (%s,%s,%s)'
         cur.execute(sqls,(name,hashed,email))
         result = cur.fetchone()
         return False
    else:
        return True

    mysql.close()

def loginUser(name,password):
    #mysql = MySQL(app)
    #User login
    error = None
    cur = mysql.connection.cursor()
    sql='SELECT * FROM usuario WHERE name = %s'
    cur.execute(sql,[name])
    result=cur.fetchone()
    passw=result[1]
    print(passw)
    #acces tuple for password
    #print(result[3])
    #Check if user and password is correct
    if result is None:
        error= 'incorect user'
        #session is id from db
        #session['user']=result[0]
    elif check_password_hash(passw,password):
        error='incorect password'
    print (error)
    if error is None:
        session['user']=result[0]
        return True
    else:
        return False
    
    
    #this works
    #print(result[0][2])
    #print (cur[0])
def getUser(id):
    cur = mysql.connection.cursor()
    sql='SELECT * FROM usuario WHERE id = %s'
    cur.execute(sql,[id])
    result=cur.fetchone()
    if result is None:
        return 'no bueno'
    else:
        return result

    