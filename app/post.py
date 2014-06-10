from app import app
from tweetings import Tweet
from forms import TweetForm
from flask import request
import datetime

class Post():
	def execute(form):
		form = TweetForm()
		t = Tweet()
		t.content = request.form['tweet']
		t.date = datetime.datetime.now()
		t.put()
		