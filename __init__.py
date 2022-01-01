from flask import Flask, render_template, session, redirect, request, url_for
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_paginate import Pagination, get_page_parameter
import re

app = Flask(__name__, static_url_path='/')

app.secret_key = 'Vinothkikikisite'
app.url_map.strict_slashes = False

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('logged_in') != True:
            return redirect(url_for('admin.login'))
        return f(*args, **kwargs)
    return decorated_function


# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:Munish#123@database-1.csjcgnnefaw9.us-east-2.rds.amazonaws.com:3306/vinoth'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://vinoth:Vinoth#123@localhost/vinoth'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)
# import views

# from tamildhool.video.views import Video_BluePrint
# from tamildhool.video_page.views import VideoPage_Blueprint
# # from tamildhool.movies.views import Movies_BluePrint
# from tamildhool.admin.views import admin_Blueprint
# # from tamildhool.trending.views import Trending_BluePrint

# app.register_blueprint(Video_BluePrint,url_prefix="/video-page-view")
# app.register_blueprint(VideoPage_Blueprint, url_prefix="/serial")
# # app.register_blueprint(Movies_BluePrint, url_prefix="/movies")
# app.register_blueprint(admin_Blueprint, url_prefix="/admin")
# # app.register_blueprint(Trending_BluePrint, url_prefix="/trending")


from tamildhool.models import VideoPage

def urlsluggenerator(string):
    return re.sub(' +', '-', string).lower()

def getvijaytvserials():
    return VideoPage.query.filter(VideoPage.VideoCategory.in_([1])).all()

def getsuntvserials():
    return VideoPage.query.filter(VideoPage.VideoCategory.in_([2])).all()

def getzeetamiltvserials():
    return VideoPage.query.filter(VideoPage.VideoCategory.in_([3])).all()

app.jinja_env.globals.update(urlsluggenerator=urlsluggenerator)
app.jinja_env.globals.update(getvijaytvserials=getvijaytvserials)
app.jinja_env.globals.update(getsuntvserials=getsuntvserials)
app.jinja_env.globals.update(getzeetamiltvserials=getzeetamiltvserials)



    
