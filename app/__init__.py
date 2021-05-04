from flask import Flask
import logging
import json_log_formatter

formatter = json_log_formatter.JSONFormatter()

json_handler = logging.FileHandler(filename='/Users/sam.cipriani/github/activity_picker/activity_picker.log')
json_handler.setFormatter(formatter)

logger = logging.getLogger('my_json')
logger.addHandler(json_handler)
logger.setLevel(logging.INFO)

logger.info('Application Startup', extra={'successful': 'true'})


app = Flask(__name__)

from app import routes
