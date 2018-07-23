
import webapp2
import jinja2
import os
from google.appengine.api import users
from google.appengine.ext import ndb


TEMPLATE = jinja2.Environment(
	loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions = ['jinja2.ext.autoescape'],
	autoescape = True
)


logged_in = False

class CssiUser(ndb.Model):

  	first_name = ndb.StringProperty()
  	last_name = ndb.StringProperty()
	username = ndb.StringProperty()
	email = ndb.StringProperty()
	password = ndb.StringProperty()
	location = ndb.StringProperty()

class HomePage(webapp2.RequestHandler):
	def get(self):
		content = TEMPLATE.get_template('/templates/home.html')
		self.response.write(content.render())


class MainHandler(webapp2.RequestHandler):
  def get(self):
    # user = users.get_current_user()

    content = TEMPLATE.get_template('/templates/signup.html')
	# params = {
	# 	'success' : False
	# 	'failure' : False
	# 	'user' : user
	# }
    # If the user is logged in...
    if logged_in:
		# params['success'] = True
		signout_link_html = users.create_logout_url('/')
		self.response.write(content.render(success = True, user = user, logout = signout_link_html))
      # email_address = user.nickname()
      # cssi_user = CssiUser.get_by_id(user.user_id())
      # # If the user has previously been to our site, we greet them!
      # if cssi_user:
      #   self.response.write('''
      #       Welcome %s %s (%s)! <br> %s <br>''' % (
      #         cssi_user.first_name,
      #         cssi_user.last_name,
      #         email_address,
      #         signout_link_html))
      ## If the user hasn't been to our site, we ask them to sign up
      # else:
      #   self.response.write(content.render() % (email_address, signout_link_html))
    # Otherwise, the user isn't logged in!
    else:

		self.response.write(content.render(failure = True))
      # self.response.write('''
      #   Please log in to use our site! <br>
      #   <a href="%s">Sign in</a>''' % (
      #     users.create_login_url('/')))

  def post(self):
	  logged_in = True
	  content = TEMPLATE.get_template('/templates/signup.html')
	  user = users.get_current_user()
	    # if not user:
	    #   # You shouldn't be able to get here without being logged in
	    #   self.error(500)
	    #   return
	  cssi_user = CssiUser(
	        first_name=self.request.get('firstname'),
	        last_name=self.request.get('lastname'),
			username = self.request.get('Username'),
		    email = self.request.get('Email'),
		    password = self.request.get('Password'),
		    location = self.request.get('location'))
	  cssi_user.put()
	  signout_link_html = users.create_logout_url('/')
	  self.response.write(content.render(success = True, user = cssi_user.first_name, logout = signout_link_html))

class LoginHandler(webapp2.RequestHandler):
	def get(self):
		print ("Login handler works")

app = webapp2.WSGIApplication([
  ('/', HomePage),
  ('/login', MainHandler),
  ('/signIn', LoginHandler)
], debug=True)
