import os

SECRET_KEY = 'you-will-never-guess'
DEBUG = True
DB_USERNAME = 'root'
DB_PASSWORD = ''
BLOG_DATABASE_NAME = 'myblog'
DB_HOST = 'localhost'
DB_URI = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{BLOG_DATABASE_NAME}"
SQLALCHEMY_DATABASE_URI = DB_URI


