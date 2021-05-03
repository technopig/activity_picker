from flask import Flask
import logging
logging.basicConfig(filename='demo.log', level=logging.DEBUG)


app = Flask(__name__)

from app import routes
