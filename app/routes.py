from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

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

#decorator for login form
@app.route('/login', methods=['GET', 'POST'])
def login():
    #creating a new login form to be passed into the render_template()
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    #form=form meaning the LoginForm that was instantiated as form is being passed into the template's form parameter
    return render_template('login.html', title= 'Sign In', form = form)



