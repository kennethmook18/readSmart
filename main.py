
import webapp2
import jinja2
import os
from google.appengine.api import users
from google.appengine.ext import ndb

users = []
TEMPLATE = jinja2.Environment(
	loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions = ['jinja2.ext.autoescape'],
	autoescape = True
)


logged_in = False


class Books(ndb.model):
	title = ndb.StringProperty()
	author = ndb.StringProperty()
	id = ndb.StringProperty()
	persons_input = ndb.IntegerProperty()
	bookindex = ndb.IntegerProperty(repeat=True)

class HomePage(webapp2.RequestHandler):
	def get(self):
		content = TEMPLATE.get_template('/templates/home.html')
		self.response.write(content.render(active = logged_in))
		hamlet = Books(
			title = "hamlet"
			author = "shakespeare"
		)
		Macbeth = books()
		self.response.write(content.render(title= hamlet.title, author = hamlet.author))

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

    if logged_in:

		self.response.write(content.render(success = True, user = user))
    else:

		self.response.write(content.render(failure = True))


  def post(self):
	  logged_in = True
	  content = TEMPLATE.get_template('/templates/signup.html')
	  # user = users.get_current_user()
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
	  #
	  # user = cssi_user.all()
	  # print user



	  cssi_user.put()
	  users.append(cssi_user)
	  self.response.write(content.render(success = True, user = cssi_user.first_name))

class LoginHandler(webapp2.RequestHandler):
	def get(self):
	  	content = TEMPLATE.get_template('/templates/signIn.html')
		self.response.write(content.render(start = True))

	def post(self):
		username = self.request.get("Username")
		password = self.request.get("Password")
		content = TEMPLATE.get_template('/templates/signIn.html')
		self.response.write(content.render(start = False))
		# user_key =  CssiUser.all()

		q = CssiUser.query().fetch()
		for user in q:
			content = TEMPLATE.get_template('/templates/signup.html')
			if user.username == username and user.password == password:
				logged_in = True
				self.response.clear()
				self.response.write(content.render(success = logged_in, user = user.first_name))
		self.response.clear()
		content = TEMPLATE.get_template('/templates/signIn.html')
		self.response.write(content.render(start = True, error = True, Username = username, Password = password))
		# ndb.Query()
		# q.filter("username = ", self.response.get("Username"))
		# print q

# booksindex = []

def average(persons_input, title):
	b = books.query().fetch()
	for book in b:
		if b.title == title:
			book_length = persons_input
			book_length = int(book_length)
			b.bookindex.append(book_length)


app = webapp2.WSGIApplication([
  ('/', HomePage),
  ('/login', MainHandler),
  ('/signIn', LoginHandler)
], debug=True)
