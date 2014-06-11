from flask import render_template, request, redirect, url_for, current_app, Response
from app import app, redis_server
from forms import TweetForm
#from tweetings import Tweet
#from retrieve import Retrieve
#from google.appengine.ext import db
#from google.appengine.api import images
import datetime
#from tweetdisplay import TweetDisplay

#default post id in redis 
ID_DEF = 1000 

@app.route('/id', methods=['GET'])
def getTweetId():
    temp=redis_server.get("tweet_id")
    #if tweet_id is null in redis, means the user never tweets
    if temp is None:
        #setting the initial tweet id on redis
        redis_server.set("tweet_id", ID_DEF)
        tweet_id=ID_DEF
    else:
        tweet_id=redis_server.incr("tweet_id",1)
    return tweet_id

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	form = TweetForm(request.form)
	#tweetmaster = Tweet(key_name='tm')
	#t = Tweet(parent=tweetmaster)

	if request.method=='POST' and form.validate():
		tweet_id = "post:" + str(getTweetId())
		content = request.form['tweet']
		date = datetime.datetime.now()
		tweet = {'content': content, 'date': str(date)}
		redis_server.hmset(tweet_id, tweet)
		redis_server.save()
		return redirect(url_for('index'))
		
	retrieve = []
	listOfPostKeys = redis_server.keys('post:*')
	for keys in listOfPostKeys:
		contentOfTweet=redis_server.hgetall(keys)
		retrieve.append(contentOfTweet)
	photo_url = {}
	display = []
	return render_template("index.html", form=form, retrieve=retrieve)
	
@app.route('/show/<key>', methods=["GET"])
def show(key):
	photo = db.get(key)
	if not photo:
		return ""
	else:
		mimetype="image/png"
		return Response(photo.image, mimetype=mimetype)


	
