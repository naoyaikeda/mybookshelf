# -*- coding: utf-8 -*-
# app.urls
# 

# Following few lines is an example urlmapping with an older interface.
"""
from werkzeug.routing import EndpointPrefix, Rule

def make_rules():
  return [
    EndpointPrefix('app/', [
      Rule('/', endpoint='index'),
    ]),
  ]

all_views = {
  'app/index': 'app.views.index',
}
"""

from kay.routing import (
  ViewGroup, Rule
)

view_groups = [
  ViewGroup(
    Rule('/', endpoint='index', view='app.views.index'),
  )
]

