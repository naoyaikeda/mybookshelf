# -*- coding: utf-8 -*-
# app.models

from google.appengine.ext import db

class Book(db.Model):
    isbn = db.StringProperty(multiline=False, verbose_name=u'ISBN')
    title = db.StringProperty(multiline=False, verbose_name=u'書名')
    