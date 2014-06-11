from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers

class Tweet(db.Model):
	content = db.StringProperty(multiline=False)
	date = db.DateTimeProperty(auto_now_add=True)
	image = db.BlobProperty(default=None)
	
	
	