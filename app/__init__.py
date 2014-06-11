from flask import Flask
import redis

app = Flask(__name__)
POOL = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)
redis_server = redis.Redis(connection_pool=POOL)
from app import views
