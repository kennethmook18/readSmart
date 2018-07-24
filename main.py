import webapp2
import jinja2
import os
from books import *
from google.appengine.api import users
from google.appengine.ext import ndb
import logging


TEMPLATE = jinja2.Environment(
	loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions = ['jinja2.ext.autoescape'],
	autoescape = True
)


# class Books(ndb.model):
# 	title = ndb.StringProperty()
# 	author = ndb.StringProperty()
# 	id = ndb.StringProperty()
# 	persons_input = ndb.IntegerProperty()
# 	bookindex = ndb.IntegerProperty()


class HomePage(webapp2.RequestHandler):

	def get(self):
		content = TEMPLATE.get_template('/templates/home.html')

		if self.request.cookies.get("logged_in") == "True":
			self.response.write(content.render(active = True))
		else:
			self.response.write(content.render(login = True))
		#
		# hamlet = Books(
		# 	title = "hamlet",
		# 	author = "shakespeare"
		# )
		# Macbeth = books()
		# self.response.write(content.render(title= hamlet.title, author = hamlet.author))

class CssiUser(ndb.Model):

  	first_name = ndb.StringProperty()
  	last_name = ndb.StringProperty()
	username = ndb.StringProperty()
	email = ndb.StringProperty()
	password = ndb.StringProperty()
	location = ndb.StringProperty()



class MainHandler(webapp2.RequestHandler):
	def get(self):
    # user = users.get_current_user()
		content = TEMPLATE.get_template('/templates/signup.html')

		if self.request.cookies.get("logged_in") == "True":

			self.response.write(content.render(success = True, user = user))
		else:
			self.response.write(content.render(failure = True))


 	def post(self):
		# logged_in = True
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
		self.response.set_cookie("logged_in", "True")
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
			if (user.username == username and user.password == password) or (user.email == username and user.password == password):
				# logged_in = True
				self.response.set_cookie("logged_in", "True")
				self.response.clear()
				self.response.write(content.render(success = True, user = user.first_name))
				return
			else:
				self.response.delete_cookie("logged_in")

		if self.request.cookies.get("logged_in") == "":
			self.response.clear()
			content = TEMPLATE.get_template('/templates/signIn.html')
			self.response.write(content.render(start = True, error = True, Username = username, Password = password))
		# ndb.Query()
		# q.filter("username = ", self.response.get("Username"))
		# print q

class BookHandler(webapp2.RequestHandler):
	def get(self):
		content = TEMPLATE.get_template('/templates/book.html')
		# create a new html class names Books
		# have a bunch of {{ placeholders }} and then do
		# self.response.write(content.render(book.value for all the placeholders))

class UserInput(webapp2.RequestHandler):
	def get(self):
		content = TEMPLATE.get_template('/templates/UserInput.html')
		self.response.write(content.render(title = "book variable"))
		# print "Class is functional"



def average(persons_input, title):
	b = Books.query().fetch()
	for book in b:
		if b.title == title:
			book_length = persons_input
			book_length = int(book_length)
			b.bookindex.append(book_length)


app = webapp2.WSGIApplication([
  ('/', HomePage),
  ('/login', MainHandler),
  ('/signIn', LoginHandler),
  ('/input', UserInput)
], debug=True)
