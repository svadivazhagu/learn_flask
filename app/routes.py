from app import app

#decorator where user indicates what routes will lead to function
@app.route('/')
@app.route('/index')
def index():
   #going to make a mock user as a python dict, k='username' v = 'Surya'
   user = {'username' : 'Surya'}
   return '''
   
<html> 
   <head>
      <title>Blog Homepage </title>
      
   </head>
   <body>
      <h1> Hello, ''' + user['username'] + ''' ! </h1>
   </body>
   
</html>

'''

