def encyrpted(pw):
  import hashlib
  return hashlib.md5(pw).hexdigest()
  
def signup():
   # db.user.truncate()
   # global left_sidebar_enabled
   # left_sidebar_enabled = False
   '''
   print("in signup", globals()['left_sidebar_enabled'])
   globals()['left_sidebar_enabled'] = False
   print("in signup", globals()['left_sidebar_enabled'])'
   '''
   import time
   form = FORM(
     'Username', INPUT(_name='username', requires=[IS_NOT_EMPTY(), IS_NOT_IN_DB(db,db.users.username)]), BR(),
     'Password', INPUT(_name='pw1', _type='password', label='Password'), BR(),
     'Paswword2', INPUT(_name='pw2', _type='password', label='Confirm password',
            requires=IS_EQUAL_TO(request.vars.pw1, "don't match")), BR(),
     'Email', INPUT(_name='email', requires=IS_EMAIL()), BR(),
     INPUT(_type='submit'),
     _id="loginform", _class="bootstrapform"
   )
   if form.process().accepted:
     db.users.insert(username=form.vars.username, 
                    password=encyrpted(form.vars.pw1),
                    email = form.vars.email
                    )
     #TODO: return user to the new account page               
     return redirect(request.env.http_referer)
   return dict(form = form)
def signin():
   global userid
   username = request.vars.username
   pw = encyrpted(request.vars.pw)
   rows = db( (db.users.username == username) & (db.users.password==pw)).select()   
   if len(rows) == 0:
		response.flash = "Wrong username or password"
		session.error='Wrong username or password'
		return redirect(request.env.http_referer)
   else:
     session.user = rows[0]
     return redirect(request.env.http_referer)
   return BEAUTIFY(request.vars)
   
def logout():
	session.user=None
	return redirect(request.env.http_referer)
