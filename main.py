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


class HomePage(webapp2.RequestHandler):

	def get(self):
		books = Books.query().fetch()
		if len(books) == 0:
			BookLoader()
		content = TEMPLATE.get_template('/templates/home.html')

		if self.request.cookies.get("logged_in") == "True":
			self.response.write(content.render(active = True))
		else:
			self.response.write(content.render(login = True))

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

			self.response.write(content.render(success = True, user = self.request.cookies.get("name")))
		else:
			self.response.write(content.render(failure = True))


 	def post(self):
		# logged_in = True
		content = TEMPLATE.get_template('/templates/signup.html')
	  	cssi_user = CssiUser(
	       	first_name=self.request.get('firstname'),
	       	last_name=self.request.get('lastname'),
			username = self.request.get('Username'),
		    email = self.request.get('Email'),
		    password = self.request.get('Password'),
		    location = self.request.get('location'))
		cssi_user.put()
		self.response.set_cookie("logged_in", "True")

		self.response.set_cookie("name", cssi_user.first_name)
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
				self.response.set_cookie("name", user.first_name)
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

class LordFlies(webapp2.RequestHandler):
    def get(self):
        content = JINJA_ENV.get_template('/books.html')
        params = {
            'title': "Lord of the Flies",
            'author': "William Golding",
            'synopsis': "Synopsis goes here",
            'image': "lordflies.jpeg",
        }
        self.response.write(content.render(params))

class GreatGatsby(webapp2.RequestHandler):
    def get(self):
        content = JINJA_ENV.get_template('/books.html')
        params = {
            'title': "The Great Gatsby",
            'author': "F. Scott Fitzgerald",
            'synopsis': "Synopsis goes here",
            'image' : "GreatGatsby.jpeg",
        }
        self.response.write(content.render(params))

class KillMockBird(webapp2.RequestHandler):
    def get(self):
        content = JINJA_ENV.get_template('/books.html')
        params = {
            'title': "To Kill a Mockingbird",
            'author': "Harper Lee",
            'synopsis': "Synopsis goes here",
            'image':"KillMock.jpg",
        }
        self.response.write(content.render(params))

class RomeoJuliet(webapp2.RequestHandler):
    def get(self):
        content = JINJA_ENV.get_template('/books.html')
        params = {
            'title': "Romeo & Juliet",
            'author': "William Shakespeare",
            'synopsis': "Synopsis goes here",
            'image':"RomeoJuliet.jpg",
        }
        self.response.write(content.render(params))

class Macbeth(webapp2.RequestHandler):
    def get(self):
            content = JINJA_ENV.get_template('/books.html')
            params = {
                'title': "Macbeth",
                'author': "William Shakespeare",
                'synopsis': "Synopsis goes here",
                'image':"Macbeth.jpg",
            }
            self.response.write(content.render(params))

class HuckFinn(webapp2.RequestHandler):
    def get(self):
            content = JINJA_ENV.get_template('/books.html')
            params = {
                'title': "The Adventures of Huckleberry Finn",
                'author': "Mark Twain",
                'synopsis': "Synopsis goes here",
                'images': "HuckFinn.jpg",
            }
            self.response.write(content.render(params))

class Giver(webapp2.RequestHandler):
    def get(self):
            content = JINJA_ENV.get_template('/books.html')
            params = {
                'title': "The Giver",
                'author': "Lois Lowry",
                'synopsis': "Synopsis goes here",
                'images': "Giver.jpg",
            }
            self.response.write(content.render(params))

class Hamlet(webapp2.RequestHandler):
    def get(self):
            content = JINJA_ENV.get_template('/books.html')
            params = {
                'title': "Hamlet",
                'author': "William Shakespeare",
                'synopsis': "Synopsis goes here",
                'image': "Hamlet.jpg",
            }
            self.response.write(content.render(params))

class Fahrenheit(webapp2.RequestHandler):
    def get(self):
            content = JINJA_ENV.get_template('/books.html')
            params = {
                'title': "Fahrenheit 451",
                'author': "Ray Bradbury",
                'synopsis': "Synopsis goes here",
                'image': "Fah451.jpg",
            }
            self.response.write(content.render(params))

class HarryPotter(webapp2.RequestHandler):
    def get(self):
            content = JINJA_ENV.get_template('/books.html')
            params = {
                'title': "Harry Potter and the Sorcerer's Stone",
                'author': "J.K. Rowling",
                'synopsis': "Synopsis goes here",
                'image': "HarryPot.jpg",
            }
            self.response.write(content.render(params))

class HungerGames(webapp2.RequestHandler):
    def get(self):
            content = JINJA_ENV.get_template('/books.html')
            params = {
                'title': "The Hunger Games",
                'author': "Suzanne Collins",
                'synopsis': "Synopsis goes here",
                'image': "Hunger.jpg",
            }
            self.response.write(content.render(params))

class Narnia(webapp2.RequestHandler):
    def get(self):
            content = JINJA_ENV.get_template('/books.html')
            params = {
                'title': "The Lion, the Witch, and the Wardrobe",
                'author': "C.S. Lewis",
                'synopsis': "Synopsis goes here",
                'image': "Narnia.jpg",
            }
            self.response.write(content.render(params))


app = webapp2.WSGIApplication([
  ('/', HomePage),
  ('/login', MainHandler),
  ('/signIn', LoginHandler),
  ('/input', UserInput),
      ('/lordoftheflies', LordFlies),
      ('/greatgatsby', GreatGatsby),
      ('/tokillamockingbird', KillMockBird),
      ('/romeo&juliet', RomeoJuliet),
      ('/macbeth', Macbeth),
      ('/huckleberryfinn', HuckFinn),
      ('/thegiver', Giver),
      ('/hamlet', Hamlet),
      ('/fahrenheit451', Fahrenheit),
      ('/sorcererstone', HarryPotter),
      ('/hungergames', HungerGames),
      ('/lionwitchwardrobe', Narnia),
], debug=True)
