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


class PersonalLibrary(webapp2.RequestHandler):
	def get(self):
		content = TEMPLATE.get_template('/tempates/library.html')

class BookView(webapp2.RequestHandler):
	def get(self):
		content = TEMPLATE.get_template('/templates/books.html')
		name = self.request.get("title")
		item = Books.query().filter(Books.title == name).get()
		average = 0
		counter = 0
		list = [["Person", "Time"]]
		for number in item.bookindex:
			print counter
			average = average + number
			print average
			list.append(["Person", number])
			counter +=1
			if counter == 0:
				average = 0

			else:
				average = average/counter
		self.response.write(content.render(title = item.title, id = item.id, author = item.author, average = average, list = list))


	def post(self):
		content = TEMPLATE.get_template('/templates/books.html')
		name = self.request.get("title")
		item = Books.query().filter(Books.title == name).get()

		item.bookindex.append(int(self.request.get("time")))
		average = 0
		counter = 0
		list = [["Person", "Time"]]
		for number in item.bookindex:
			print counter
			average += number
			list.append(["Person", item.bookindex[counter]])

			counter +=1
		average = average/counter
		item.put()
		self.response.write(content.render(title = item.title, id = item.id, author = item.author, average = average, averageSet = True, list=list))
		return


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
		    <title>readSmart</title>
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



def BookLoader():
	q = Books.query().fetch()

	book = Books(
		title = "Lord of the Flies",
		author = "William Golding",
		id = "lordflies",
		persons_input = 0,
		bookindex = [180,180,120,180,210,240,240,180,240,270,240,180,270,270,240,270,210,270,300,300,180],
		publication_date = "September 17, 1954"
	)
	book.put()
	book = Books(
		title = "The Great Gatsby",
		author = "F. Scott Fitzgerald",
		id = "GreatGatsby",
		persons_input = 0,
		bookindex = [180,210,120,150,180,90,180,180,150,270,120,180,120,240,300,180,120],
		publication_date = "April 10, 1925"
	)
	book.put()

	book = Books(
		title = "To Kill a Mockingbird",
		author = "Harper Lee",
		id = "KillMock",
		persons_input = 0,
		bookindex = [390,240,240,330,300,360,240,360,390,330,270,420,240,390],
		publication_date = "July 11, 1960"
	)
	book.put()
	book = Books(
		title = "Romeo and Juliet",
		author = "William Shakespeare",
		id = "RomeoJuliet",
		persons_input = 0,
		bookindex = [390,420,240,240,300,240,330,300,300,240,330,180,300,300,300,300,420,240,300,420,270],
		publication_date = "1597"
	)
	book.put()
	book = Books(
		title = "Macbeth",
		author = "William Shakespeare",
		id = "Macbeth",
		persons_input = 0,
		bookindex = [300,150,210,270,150,270,240,180,210,210,240,180,270,360],
		publication_date = "1606"
	)
	book.put()

	book = Books(
		title = "The Adventures of Huckleberry Finn",
		author = "Mark Twain",
		id = "HuckFinn",
		persons_input = 0,
		bookindex = [120,120,180,210,150,210,180,300,150,210,180,330,270,150],
		publication_date = "December 10, 1884"
	)
	book.put()
	book = Books(
		title = "The Giver",
		author = "Lois Lowry",
		id = "Giver",
		persons_input = 0,
		bookindex = [90,120,180,210,180,150,240,120,120,270,250,250,180,210,270,240,270,240],
		publication_date = "1993"
	)
	book.put()

	book = Books(
		title = "Hamlet",
		author = "William Shakespeare",
		id = "Hamlet",
		persons_input = 0,
		bookindex = [210 ,240, 300, 210, 330, 300, 330, 300, 270, 270,330,330, 390,330],
		publication_date = "1603"
	)
	book.put()
	book = Books(
		title = "Fahrenheit 451",
		author = "Ray Bradbury",
		id = "Fah451",
		persons_input = 0,
		bookindex = [150,210,240,150,280,240,270,180,150,240,600,180],
		publication_date = "October 1953"
	)
	book.put()

	book = Books(
		title = "Harry Potter and the Sorcerer's Stone",
		author = "J.K. Rowling",
		id = "HarryPot",
		persons_input = 0,
		bookindex = [210,180,270,300,180,300,180,330,240,300,390,360,270],
		publication_date = "June 26, 1997"
	)
	book.put()
	book = Books(
		title = "The Hunger Games",
		author = "Suanne Collins",
		id = "Hunger",
		persons_input = 0,
		bookindex = [270,270,240,330,300,300,240,360,390,300,300,360,300,300,330,330,360,360,270],
		publication_date = "September 14, 2008"
	)
	book.put()

	book = Books(
		title = "The Lion, the Witch and the Wardrobe",
		author = "C. S. Lewis",
		id = "Narnia",
		persons_input = 0,
		bookindex = [270,150,180,210,120,210,180,150,300,150,240,300],
		publication_date = "October 16, 1950"
	)
	book.put()
