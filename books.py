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
	bookindex = ndb.IntegerProperty()

class BookHandler(webapp2.RequestHandler):
    print("this works")
