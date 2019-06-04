from flask import render_template
from app import app

#decorator where user indicates what routes will lead to function
@app.route('/')
@app.route('/index')
def index():
   #going to make a mock user as a python dict, k='username' v = 'Surya'
   user = {'username' : 'Surya'}
   #going to make a fake post to learn for loops
   posts = [
      {
         'author': {'username': 'John'},
         'body': 'Beautiful day in Portland!'
      },
      {
         'author': {'username': 'Susan'},
         'body': 'The Avengers movie was so cool!'
      }
   ]
   return render_template('index.html', title = 'Hello', user=user, posts = posts)

