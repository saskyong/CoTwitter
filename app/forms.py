from wtforms import Form, TextAreaField, SubmitField, FileField, validators
from flask import request
from google.appengine.ext import blobstore

class TweetForm(Form):
	tweet = TextAreaField("Tweet something", [validators.Required(), validators.Length(max=140)])
	file = FileField()
	submit = SubmitField("Tweet")
	
