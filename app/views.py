from flask import request, redirect, session, url_for, make_response,jsonify,json
from flask import render_template
from flask_mysqldb import MySQL
import mysql.connector


from database import *


@app.route("/") # A decorator; when the user goes to the route `/`, exceute the function immediately below
def index():
   
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
           
        else:
            return redirect('/')
        
    elif request.method == 'GET':
        return render_template('public/register.html')
    



@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect('/')

@app.route('/movie/<id>')
def movie(id):
    session['movie_id']=id
    return render_template('/public/movie.html',id=id)

@app.route('/reviews',methods=['POST'])
def review():
    req=request.json
    review=getReviews(req['id'])
    return make_response(jsonify(review), 200)
  

@app.route('/add-review',methods=['POST'])
def add_review():
    if(session.get('user',None) is not None):
        print('etc')
        data = request.form['comment']
        userid=session['user']
        username=session['name']
        movie_id=session['movie_id']
       
        createReview(userid,username,movie_id,data)
        
        return redirect(url_for('movie',id=movie_id))
    else:
        return redirect(url_for("login"))

   


@app.route("/search", methods=['GET','POST']) # A decorator; when the user goes to the route `/`, exceute the function immediately below
def search():
   
    req = request.get_json()
   
    if session.get('user',None) is not None:
        user=session['user']
        return render_template('public/search.html',user=user)
    else:
        return render_template('public/search.html')



@app.route("/actor/<id>",methods=['GET','POST'])
def actor(id):
    return render_template('/public/actor.html',id=id)
    actor = request.json
    return render_template('/public/actor.html',actor=actor)
    

@app.route("/favorite",methods=['GET','POST'])
def favorite():
    
    favorite = request.json
    print(favorite)
    if session.get('user',None) is None:
        #no user logged in do a redirect
        response=None
    else:
        user=session['user']
        response=checkFavorite(user,favorite['id'],favorite['name'],favorite['genre'],favorite['image'])
    
   
    return make_response(jsonify(response), 200)

@app.route("/favorites")
def favorites():
    if session.get('user',None) is None:
        #no user logged in do a redirect
        return redirect(url_for("login"))
    else:
        result=getFavorite(session['user'])
        
        return render_template('public/favorites.html',result=result)

@app.route('/profile',methods=['GET','POST'])
#dynamic urls for created profiles
def profile():
    #if 'user' in session:
    
    if session.get('user',None) is not None:
        userid=session['user']
        #get user from db
        result = getUser(userid)
        favorites = getFavorite(userid)
        reviews = getReview_user(userid)
        if request.method == 'POST':
            name = request.form['name']
            email=request.form['email']
            changeAccountData(name,email,userid)
            
            result=getUser(userid)
        return render_template('/public/profile.html',user=result[1],email=result[3],favorites=favorites, reviews=reviews)
    else:
        return redirect(url_for("login"))
   

@app.route("/discover",methods=['GET','POST'])
def discover():

    return render_template('public/discover.html')

