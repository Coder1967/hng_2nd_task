#!/usr/bin/python3
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix='/api/')


from models import storage
from models.user import User

from .users import *
