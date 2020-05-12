#punto entrada de la aplicacion
#import busca el fichero __init__ que crea la app
from app import app
from tempfile import mkdtemp

from flask import request, redirect, session, url_for
from flask import render_template
from flask_mysqldb import MySQL
import mysql.connector
app.secret_key = 'hello'

if __name__ == 'main':
    app.run()


