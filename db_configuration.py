#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 

Course work: 

@author: raja

Source:
    https://docs.mongoengine.org/guide/defining-documents.html#fields
'''

# Import necessary modules
from flask_pymongo import PyMongo,pymongo
from flask_mongoengine import MongoEngine

# Local Import
from application import application

mongo  = PyMongo(application)

# Setup Mongo Engine
db = MongoEngine()
db.init_app(application)

# Vanilla variables
test_info_van               = mongo.db.test_info  #taken from TestDB

'''
test_info:
    name                
    age       
'''
class test_info(db.Document):

    name       = db.StringField() 
    age        = db.IntField()    


    def to_json(self):
        return {
            'name'          :self.name,
            'age'           :self.age
        }

