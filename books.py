import webapp2
import jinja2
import os
from main import *
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
	synopsis = ndb.StringProperty()
	id = ndb.StringProperty()
	persons_input = ndb.IntegerProperty()
	bookindex = ndb.IntegerProperty(repeated = True)
	publication_date = ndb.StringProperty()

class AddBookHandler(webapp2.RequestHandler):
	def get(self):
		content = TEMPLATE.get_template('templates/UserInput.html')
		self.response.write(content.render())
	def post(self):
		book = Books(

		)
		book.put()

class BookView(webapp2.RequestHandler):
	def get(self):
		content = TEMPLATE.get_template('/templates/books.html')
		name = self.request.get("title")
		item = Books.query().filter(Books.title == name).get()
		average = 0
		Max=0
		Min=0
		counter = 0
		list = [["Person", "Time"]]
		for number in item.bookindex:
			print counter
			average = average + number
			print average
			list.append(["Person", number])
			counter +=1
		if counter != 0:
			average = average/counter
			Max = average * 2
			Min = average / 4
		self.response.write(content.render(title = item.title, id = item.id, author = item.author, synopsis = item.synopsis, average = average, list = list, Max = Max, Min = Min))








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
		self.response.write(content.render(title = item.title, id = item.id, author = item.author, synopsis = item.synopsis, average = average, averageSet = True, list=list))
		return


class BookHandler(webapp2.RequestHandler):
	def get(self):
		content = TEMPLATE.get_template('/templates/book.html')
		q = Books.query().fetch()

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

				<a href="/"> <img class= "masthead-brand" style = "width: 220px; height: 60px;" src="/img/logo.png" alt="Logo"> </a>
				<nav class="nav nav-masthead justify-content-right">
					<a class="nav-link" style = "font-size: 24px;" href="#">Home</a>
					<a class="nav-link active" style = "font-size: 24px;" href="/booklist">Books</a>
					<a class="nav-link" style = "font-size: 24px;" href = "/library">Library</a>
					<a class="nav-link" style = "font-size: 24px;" href = "/logout">Logout</a>
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
# <form action="/addBooks"> <input type = "submit" value = "Add a new Book"> </form>


def BookLoader():
	q = Books.query().fetch()

	book = Books(
		title = "Lord of the Flies",
		author = "William Golding",
		synopsis = "Lord of the Flies is a 1954 novel by Nobel Prize winning British author William Golding. The book focuses on a group of British boys stranded on an uninhabited island and their disastrous attempt to govern themselves.",
		id = "lordflies",
		persons_input = 0,
		bookindex = [180,230,120,180,210,240,240,180,240,270,240,180,270,270,240,270,210,270,300,300,180,160,330,230,120,360,140],
		publication_date = "September 17, 1954"
	)
	book.put()
	book = Books(
		title = "The Great Gatsby",
		author = "F. Scott Fitzgerald",
		synopsis = "The Great Gatsby is a 1925 novel written by American author F. Scott Fitzgerald that follows a cast of characters living in the fictional town of West and East Egg on prosperous Long Island in the summer of 1922.",
		id = "GreatGatsby",
		persons_input = 0,
		bookindex = [180,210,120,150,180,90,180,180,150,270,120,180,120,240,300,180,120,90,230,230,110,130,120,140,160,140,150,70,80,100,110,90,220,230,210,70,80,80],
		publication_date = "April 10, 1925"
	)
	book.put()

	book = Books(
		title = "To Kill a Mockingbird",
		author = "Harper Lee",
		synopsis = "The unforgettable novel of a childhood in a sleepy Southern town and the crisis of conscience that rocked it, To Kill A Mockingbird became both an instant bestseller and a critical success when it was first published in 1960. ",
		id = "KillMock",
		persons_input = 0,
		bookindex = [390,260,270,330,300,360,240,360,390,330,270,420,390,260,290,280,300,310,300,340,350,330,340,370,350,360,340,350,320,330,310,360,330,320,330],
		publication_date = "July 11, 1960"
	)
	book.put()
	book = Books(
		title = "Romeo and Juliet",
		author = "William Shakespeare",
		synopsis = "Romeo and Juliet is a tragedy written by William Shakespeare early in his career about two young star-crossed lovers whose deaths ultimately reconcile their feuding families.",
		id = "RomeoJuliet",
		persons_input = 0,
		bookindex = [360,420,240,240,300,240,270,300,300,240,330,180,300,300,300,280,370,240,300,420,270,160,150,260,270,280,290,270,260,360,350],
		publication_date = "1597"
	)
	book.put()
	book = Books(
		title = "Macbeth",
		author = "William Shakespeare",
		synopsis = "Macbeth is a tragedy by William Shakespeare; it is thought to have been first performed in 1606. It dramatises the damaging physical and psychological effects of political ambition on those who seek power for its own sake.",
		id = "Macbeth",
		persons_input = 0,
		bookindex = [300,150,210,270,150,270,240,180,210,210,240,180,270,360,200,200,200,200,120,160,170,180,190,260,270,140,130,310,320,120,120,130,90,200,190],
		publication_date = "1606"
	)
	book.put()

	book = Books(
		title = "The Adventures of Huckleberry Finn",
		author = "Mark Twain",
		synopsis = "A nineteenth-century boy from a Mississippi River town recounts his adventures as he travels down the river with a runaway slave, encountering a family involved in a feud, two scoundrels pretending to be royalty, and Tom Sawyer's aunt who mistakes him for Tom.",
		id = "HuckFinn",
		persons_input = 0,
		bookindex = [120,120,180,210,210,180,300,210,180,270,150,160,170,180,150,160,170,210,220,180,190,200,200,210,280,270,260,110,100,110,115,270,260,330,140,130],
		publication_date = "December 10, 1884"
	)
	book.put()
	book = Books(
		title = "The Giver",
		author = "Lois Lowry",
		synopsis = "The Giver is a 1993 American young adult dystopian novel by Lois Lowry. It is set in a society which at first appears to be utopian but is revealed to be dystopian as the story progresses. The novel follows a 12-year-old boy named Jonas.",
		id = "Giver",
		persons_input = 0,
		bookindex = [90,120,180,210,180,150,240,120,120,170,180,210,270,240,170,240,90,120,150,130,90,200,200,210,140,250,200,200,220,220,160,170,160,170,190,190,160,160,80],
		publication_date = "1993"
	)
	book.put()

	book = Books(
		title = "Hamlet",
		author = "William Shakespeare",
		synopsis = "The Tragedy of Hamlet, Prince of Denmark, often shortened to Hamlet, is a tragedy written by William Shakespeare at an uncertain date between 1599 and 1602.",
		id = "Hamlet",
		persons_input = 0,
		bookindex = [200, 250,260,270, 300, 210, 330, 300, 330, 300, 270, 270,330,330, 390,330,290,290,280,300,290,330,320,280,270,250,240,230,220,210,200,350,310,370,380,400,270,280,290,290,290,290,290,320,320,250,240,240,230,370,380],
		publication_date = "1603"
	)
	book.put()
	book = Books(
		title = "Fahrenheit 451",
		author = "Ray Bradbury",
		synopsis = "Fahrenheit 451 is a dystopian novel by American writer Ray Bradbury, published in 1953. It is regarded as one of his best works. The novel presents a future American society where books are outlawed and 'firemen' burn any that are found.",
		id = "Fah451",
		persons_input = 0,
		bookindex = [150,210,240,150,240,270,180,150,240,180,330,220,200,190,180,230,240,210,260,250,290,180,190,200,180,120,110,210,220,220,300],
		publication_date = "October 1953"
	)
	book.put()

	book = Books(
		title = "Harry Potter and the Sorcerer's Stone",
		author = "J.K. Rowling",
		synopsis = "The first book in the Harry Potter series.",
		id = "HarryPot",
		persons_input = 0,
		bookindex = [210,180,270,300,180,300,180,330,240,300,390,360,270,260,240,250,280,140,410,230,280,270,260,250,240,230,300],
		publication_date = "June 26, 1997"
	)
	book.put()
	book = Books(
		title = "The Hunger Games",
		author = "Suanne Collins",
		synopsis = "The Hunger Games is a trilogy of young adult dystopian novels written by American novelist Suzanne Collins. The series is set in The Hunger Games universe, and follows young characters Katniss Everdeen and Peeta Mellark.",
		id = "Hunger",
		persons_input = 0,
		bookindex = [270,270,240,330,300,300,240,360,390,300,360,310,330,330,360,360,270,360,350,340,330,320,310,290,280,400,260,350,320,330,430,330,390],
		publication_date = "September 14, 2008"
	)
	book.put()

	book = Books(
		title = "The Lion, the Witch and the Wardrobe",
		author = "C. S. Lewis",
		synopsis = "The Lion, the Witch and the Wardrobe is a fantasy novel for children by C. S. Lewis, published by Geoffrey Bles in 1950. It is the first published and best known of seven novels in The Chronicles of Narnia.",
		id = "Narnia",
		persons_input = 0,
		bookindex = [270,150,180,210,120,210,180,150,300,150,240,150,160,170,180,190,200,210,220,230,240,250,260,270,180,170,160,150,140,130,120,130,160,150,170,180,190,80,90,130,140,130,130],
		publication_date = "October 16, 1950"
	)
	book.put()
