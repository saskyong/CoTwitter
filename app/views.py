from flask import render_template, request, redirect, url_for, current_app, Response
from app import app
from forms import TweetForm
from tweetings import Tweet
from retrieve import Retrieve
from google.appengine.ext import db
from google.appengine.api import images
import datetime
from tweetdisplay import TweetDisplay

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	form = TweetForm(request.form)
	tweetmaster = Tweet(key_name='tm')
	t = Tweet(parent=tweetmaster)
	
	if request.method=='POST' and form.validate():
		t.content = request.form['tweet']
		t.date = datetime.datetime.now()
		file = request.files['file']
		filedata=file.read()
		
		if file:
			t.image=db.Blob(filedata)
		else:
			t.image = None

		t.put()
		return redirect(url_for('index'))	
	retrieve = Tweet.all()
	retrieve.order("-date")
	photo_url = {}
	display = []
	retrieve.ancestor(tweetmaster)
	for member in retrieve:
		d = TweetDisplay()
		photo_link = url_for(".show", key=member.key())
		d.keyd = str(member.key())
		if member.image is None:
			d.image_link = None
		else:
			d.image_link = photo_link
		d.content = member.content
		d.date = member.date
		display.append(d)
	
	return render_template("index.html", form=form, display=display, retrieve=retrieve)
	
@app.route('/show/<key>', methods=["GET"])
def show(key):
	photo = db.get(key)
	if not photo:
		return ""
	else:
		mimetype="image/png"
		return Response(photo.image, mimetype=mimetype)


	