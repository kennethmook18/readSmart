import webapp2
import jinja2
import os
from google.appengine.api import users
from google.appengine.ext import ndb
import logging


class Books(ndb.Model):
	title = ndb.StringProperty()
	author = ndb.StringProperty()
	id = ndb.StringProperty()
	persons_input = ndb.IntegerProperty()
	bookindex = ndb.IntegerProperty(repeated = True)
	publication_date = ndb.StringProperty()

class BookHandler(webapp2.RequestHandler):
	print ""


def BookLoader():
	book_list = []
	book = Books(
		title = "Lord of the Flies",
		author = "William Golding",
		id = "flies",
		persons_input = 0,
		bookindex = [],
		publication_date = "September 17, 1954"
	)
	book_list.append(book)
	book = Books(
		title = "The Great Gatsby",
		author = "F. Scott Fitzgerald",
		id = "gatsby",
		persons_input = 0,
		bookindex = [],
		publication_date = "April 10, 1925"
	)
	book_list.append(book)

	book = Books(
		title = "To Kill a Mockingbird",
		author = "Harper Lee",
		id = "mockingbird",
		persons_input = 0,
		bookindex = [],
		publication_date = "July 11, 1960"
	)
	book_list.append(book)
	book = Books(
		title = "Romeo & Juliet",
		author = "William Shakespeare",
		id = "romeo",
		persons_input = 0,
		bookindex = [],
		publication_date = "1597"
	)
	book_list.append(book)
	book = Books(
		title = "Macbeth",
		author = "William Shakespeare",
		id = "macbeth",
		persons_input = 0,
		bookindex = [],
		publication_date = "1606"
	)
	book_list.append(book)

	book = Books(
		title = "The Adventures of Huckleberry Finn",
		author = "Mark Twain",
		id = "HuckFinn",
		persons_input = 0,
		bookindex = [],
		publication_date = "December 10, 1884"
	)
	book_list.append(book)
	book = Books(
		title = "The Giver",
		author = "Lois Lowry",
		id = "giver",
		persons_input = 0,
		bookindex = [],
		publication_date = "1993"
	)
	book_list.append(book)

	book = Books(
		title = "Hamlet",
		author = "William Shakespeare",
		id = "hamlet",
		persons_input = 0,
		bookindex = [],
		publication_date = "1603"
	)
	book_list.append(book)
	book = Books(
		title = "Fahrenheit 451",
		author = "Ray Bradbury",
		id = "451",
		persons_input = 0,
		bookindex = [],
		publication_date = "October 1953"
	)
	book_list.append(book)

	book = Books(
		title = "Harry Potter and the Sorcerer's Stone",
		author = "J.K. Rowling",
		id = "stone",
		persons_input = 0,
		bookindex = [],
		publication_date = "June 26, 1997"
	)
	book_list.append(book)
	book = Books(
		title = "The Hunger Games",
		author = "Suanne Collins",
		id = "games",
		persons_input = 0,
		bookindex = [],
		publication_date = "September 14, 2008"
	)
	book_list.append(book)

	book = Books(
		title = "The Lion, the Witch and the Wardrobe",
		author = "C. S. Lewis",
		id = "Narnia",
		persons_input = 0,
		bookindex = [],
		publication_date = "October 16, 1950"
	)
	book_list.append(book)
	q = Books.query().fetch()

	
