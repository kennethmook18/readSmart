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
		q = Books.query().fetch()
		#
		self.response.write("""
		<html lang="en" dir="ltr">
		  <head>
		    <link rel="image_src" href="back-end/faveicon.ico">
			<link href="/css/bootstrap.min.css" rel="stylesheet">
		    <link href="https://fonts.googleapis.com/css?family=Orbitron|Russo+One" rel="stylesheet">
		    <link href="https://fonts.googleapis.com/css?family=Ubuntu" rel="stylesheet">
			<link rel="stylesheet" type="text/css" href="css/main.css">



		    <link href="/css/cover.css" rel="stylesheet">
		    <title>User Input</title>
		    <link rel="shortcut icon" type="image/x-icon" href="/img/logo2.png"/>

		  </head>

		  <body>
		    <div class="cover-container d-flex w-100 h-100 p-3 mx-auto flex-column">
		      <header class="masthead mb-auto">
		        <div class="inner">

		          <h3 class="masthead-brand"> <a href="/">readSmart<a></h3>
		          <nav class="nav nav-masthead justify-content-center">
		            <a class="nav-link" href="/">Home</a>
		            <a class="nav-link active" href="/booklist">Books</a>
		            <a class="nav-link" href="#">Items</a>
					<a class="nav-link" href = "/logout">Logout</a>

		          </nav>
		        </div>
		      </header>

			  <div id = book_container">
		""")
		for item in q:
			self.response.write(content.render(title = item.title, id = item.id, author = item.author))
		self.response.write("""
			</div>
			<footer class="mastfoot mt-auto">
			<div class="inner">
	  		<p>readSmart&copy; Federick Gonzalez, Casey Mook, and Jaylen Patterson</p>

			</div>
  			</footer>
		""")

class BookView(webapp2.RequestHandler):
	def get(self):
		content = TEMPLATE.get_template('/templates/books.html')
		name = self.request.get("title")
		q = Books.query().fetch()
		for item in q:
			if name == item.title:
				self.response.write(content.render(title = item.title, id = item.id, author = item.author))
				return




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
		title = "Romeo and Juliet",
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
		id = "Hunger",
		persons_input = 0,
		bookindex = [],
		publication_date = "September 14, 2008"
	)
	book.put()

	book = Books(
		title = "The Lion, the Witch and the Wardrobe",
		author = "C. S. Lewis",
		id = "Narnia",
		persons_input = 0,
		bookindex = [],
		publication_date = "October 16, 1950"
	)
	book.put()
