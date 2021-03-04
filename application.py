#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 

Course work: 

@author: raja

Source:
    https://stackoverflow.com/questions/3659142/bulk-insert-with-sqlalchemy-orm
'''

# Import necessary modules

from flask import Flask, render_template, request, jsonify
import os
import logging
from decouple import config

# DB import
from flask_pymongo import PyMongo,pymongo

 
application = Flask(__name__)


# logging setup
logging.basicConfig(level = logging.INFO)

# app configs
application.config["MONGO_URI"] = os.environ.get('MONGO_URI')
application.config["API_KEY"]   = os.environ.get('API_KEY')
application.config["PAGE_SIZE"] = os.environ.get('PAGE_SIZE')

application.config['MONGODB_SETTINGS'] = {
    'db': 'test_dev',
    'host': application.config["MONGO_URI"]
}

from db_configuration import *


@application.route('/')
def test():
     return render_template("index.html")

@application.route("/add", methods=["POST"])
def test_mongodb():
        test_dict={
            'name'  :request.values.get("name"),
            'age'   :request.values.get("age")
        }
        test_info_van.insert_one(test_dict)
        return render_template("show.html",data=test_dict)

if __name__ == "__main__":

    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 6002))
    application.run(host = host, port = port, use_reloader = True)