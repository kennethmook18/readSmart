import webapp2
import jinja2
import os
from google.appengine.api import users
from google.appengine.ext import ndb
import logging


TEMPLATE = jinja2.Environment(
	loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions = ['jinja2.ext.autoescape'],
	autoescape = True
)



class Books(ndb.Model):
	title = ndb.StringProperty()
	author = ndb.StringProperty()
	id = ndb.StringProperty()
	persons_input = ndb.IntegerProperty()
	bookindex = ndb.IntegerProperty(repeated = True)
	publication_date = ndb.StringProperty()

class BookHandler(webapp2.RequestHandler):
	def get(self):
		content = TEMPLATE.get_template('/templates/book.html')





def BookLoader():
	q = Books.query().fetch()


	book = Books(
		title = "Lord of the Flies",
		author = "William Golding",
		id = "lordflies",
		persons_input = 0,
		bookindex = [],
		publication_date = "September 17, 1954"
	)
	book.put()
	book = Books(
		title = "The Great Gatsby",
		author = "F. Scott Fitzgerald",
		id = "GreatGatsby",
		persons_input = 0,
		bookindex = [],
		publication_date = "April 10, 1925"
	)
	book.put()

	book = Books(
		title = "To Kill a Mockingbird",
		author = "Harper Lee",
		id = "KillMock",
		persons_input = 0,
		bookindex = [],
		publication_date = "July 11, 1960"
	)
	book.put()
	book = Books(
		title = "Romeo & Juliet",
		author = "William Shakespeare",
		id = "RomeoJuliet",
		persons_input = 0,
		bookindex = [],
		publication_date = "1597"
	)
	book.put()
	book = Books(
		title = "Macbeth",
		author = "William Shakespeare",
		id = "Macbeth",
		persons_input = 0,
		bookindex = [],
		publication_date = "1606"
	)
	book.put()

	book = Books(
		title = "The Adventures of Huckleberry Finn",
		author = "Mark Twain",
		id = "HuckFinn",
		persons_input = 0,
		bookindex = [],
		publication_date = "December 10, 1884"
	)
	book.put()
	book = Books(
		title = "The Giver",
		author = "Lois Lowry",
		id = "Giver",
		persons_input = 0,
		bookindex = [],
		publication_date = "1993"
	)
	book.put()

	book = Books(
		title = "Hamlet",
		author = "William Shakespeare",
		id = "Hamlet",
		persons_input = 0,
		bookindex = [],
		publication_date = "1603"
	)
	book.put()
	book = Books(
		title = "Fahrenheit 451",
		author = "Ray Bradbury",
		id = "Fah451",
		persons_input = 0,
		bookindex = [],
		publication_date = "October 1953"
	)
	book.put()

	book = Books(
		title = "Harry Potter and the Sorcerer's Stone",
		author = "J.K. Rowling",
		id = "HarryPot",
		persons_input = 0,
		bookindex = [],
		publication_date = "June 26, 1997"
	)
	book.put()
	book = Books(
		title = "The Hunger Games",
		author = "Suanne Collins",
		id = "games",
		persons_input = 0,
		bookindex = [],
		publication_date = "September 14, 2008"
	)
	for item in q:
 		if item.title == book.title:
			print "Already included"
		else:
			book.put()

	book = Books(
		title = "The Lion, the Witch and the Wardrobe",
		author = "C. S. Lewis",
		id = "Narnia",
		persons_input = 0,
		bookindex = [],
		publication_date = "October 16, 1950"
	)
	for item in q:
 		if item.title == book.title:
			print "Already included"
		else:
			book.put()
