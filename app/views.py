import random,string
from flask import render_template, flash, redirect, session, url_for, request, g
from app import app,mail
from .forms import LoginForm,LoginPage
from .models import User
from flask.ext.mongoengine import MongoEngine
from flask.ext.mail import Message
from app.models import KeysTable

def load_user(id):
    return User.query.get(int(id))


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Home')

@app.route('/loginpage',methods=['GET', 'POST'])
def loginpage():
    form=LoginPage()
    if form.validate_on_submit():
        UserName = request.form['User']
        Password= request.form['Passcode']
        document=User.objects(username=UserName).first()
        if document.password==Password:
            print("yippie")
        else:
            print("error")
    return render_template('loginform.html',form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        t_name=form.Name.data
        t_username=form.UserName.data
        t_email=form.Email.data
        t_password=form.Password.data
        VerificationKey=''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(20))
        k = KeysTable(name=t_name,username=t_username,email=t_email,password=t_password,key=VerificationKey)
        KeysTable.save(k)
        recip=[]
        recip.append(t_email)
        msg = Message('test subject', sender='whirlhammer@gmail.com', recipients=recip)
        msg.body = 'Welcome to Exceptions logger'
        msg.html = 'http://localhost:5000/login?key={}&user={}'.format(VerificationKey,t_username)
        with app.app_context():
            mail.send(msg)
    if 'key' in request.args:
        print(request.args['key'])
        VerifyKey=request.args['key']
        VerifyUser=request.args['user']
        document = KeysTable.objects(key=VerifyKey).first()
        if document.username==VerifyUser:
            u=User(name=document.name,username=document.username,email=document.email,password=document.password)
            User.save(u)
            recip=[]
            recip.append(document.email)
            msg = Message('Thank You', sender='whirlhammer@gmail.com', recipients=recip)
            msg.body = 'Welcome to Exceptions logger'
            msg.html = 'Thank you for registering. Your account is active.'
            with app.app_context():
                mail.send(msg)
            
        else:
            pass
            
    return render_template('login.html',form=form)