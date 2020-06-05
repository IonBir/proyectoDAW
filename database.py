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
    exists=False
    cur = mysql.connection.cursor()
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
    
    error = None
    cur = mysql.connection.cursor()
    sql='SELECT * FROM usuario WHERE name = %s'
    cur.execute(sql,[name])
    result=cur.fetchone()
   
    #Check if user and password is correct
    if result is None:
        error= 'incorect user'
        
    elif check_password_hash(result[2],password):
        error = None
    else:
        error='incorect password'
    if error is None:
        session['user']=result[0]
        session['name']=result[1]
        return True
    else:
        print (error)
        return False
    
    

def getUser(id):
    cur = mysql.connection.cursor()
    sql='SELECT * FROM usuario WHERE id = %s'
    cur.execute(sql,[id])
    result=cur.fetchone()
    if result is None:
        return 'no bueno'
    else:
        return result



def getReviews(movie_id):
    cur = mysql.connection.cursor()
    sql='Select * FROM review WHERE movie_id = %s'
    cur.execute(sql,[movie_id])
    result=cur.fetchall()
    print(result)
    return result

def getReview_user(user_id):
    cur = mysql.connection.cursor()
    sql='Select * FROM review WHERE user_id = %s'
    cur.execute(sql,[user_id])
    result=cur.fetchall()
    print(result)
    return result

def createReview(user_id,user_name,movie_id,data):
    cur = mysql.connection.cursor()
    sql='SELECT * FROM review WHERE movie_id=%s AND user_id=%s'
    cur.execute(sql,(movie_id,user_id))
    if (cur.fetchone() is None):
        sql='INSERT INTO review(user_id,user_name,movie_id,review_text) VALUES (%s,%s,%s,%s)'
        cur.execute(sql,(user_id,user_name,movie_id,data))
    else:
        return 'false'

def checkFavorite(user_id,movie_id,movie_name,genre_id,image_id):
    cur=mysql.connection.cursor()
    sql='SELECT * FROM favoritos WHERE user_id=%s AND movie_id=%s'
    cur.execute(sql,(user_id,movie_id))
    if (cur.fetchone() is None):
        sql='INSERT INTO favoritos(user_id,movie_id,movie_name,genre_id,movie_poster) VALUES (%s,%s,%s,%s,%s)'
        cur.execute(sql,(user_id,movie_id,movie_name,genre_id,image_id))
        return True
    else:
        sql='DELETE FROM favoritos WHERE user_id=%s AND movie_id=%s'
        cur.execute(sql,(user_id,movie_id))
        return False

def getFavorite(user_id):
    cur=mysql.connection.cursor()
    sql='SELECT * FROM favoritos WHERE user_id=%s'
    cur.execute(sql,[user_id])
    result=cur.fetchall()
    return result

def changeAccountData(name,email,userid):
    cur=mysql.connection.cursor()
    sql='UPDATE usuario SET name = %s, email = %s WHERE id = %s;'
    cur.execute(sql,[name,email,userid])
    result=cur.fetchone()

    return result
