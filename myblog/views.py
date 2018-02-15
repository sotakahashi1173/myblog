from blog import app
from flask import render_template, redirect, flash, url_for
from myblog.form import SetupForm
from blog import db
from author.models import Author
from myblog.models import Blog


@app.route('/')
@app.route('/index')
def index():
    return 'Hello World'


@app.route('/admin')
def admin():
    blogs = Blog.query.count()
    if not blogs:
        return redirect(url_for('setup'))
    return render_template('blog/admin.html')


@app.route('/setup')
def setup():
    form = SetupForm()

    return render_template('blog/setup.html', form=form)



