from flask import render_template, flash, redirect, session, url_for, request, g
from app import app, db
from .forms import LoginForm
from .models import User
import sqlite3 as sql

def load_user(id):
    return User.query.get(int(id))


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        t_name=form.Name.data
        t_username=form.UserName.data
        t_email=form.Email.data
        t_password=form.Password.data
        u = User(name='aaa',username='bbb',email='ccc',password='ddd').save()
        db.session.add(u)
        db.session.commit()
        #con = sql.connect("app.db")
        #cur = con.cursor()
        #cur.execute("INSERT INTO User(name,username,email,password) VALUES (?,?,?,?)", (t_name,t_username,t_email,t_password))
        #con.commit()
        #con.close()
    return render_template('login.html',form=form)