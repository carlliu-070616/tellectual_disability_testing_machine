from flask import flash,render_template, redirect, url_for, request,jsonify
from flask_login import current_user,login_required,login_user, logout_user
import random


from main import app,db,bs,redirect_back
from main.forms import LoginForm,RegisterForm,MessageForm
from main.models import User,Message


@app.route("/index")
def index():
   return render_template('index.html',bs=bs) 
   

@app.route("/message", methods=['GET', 'POST'])
@login_required
def message():
   form = MessageForm()
   if form.validate_on_submit():
      title = form.title.data
      body = form.body.data
      message = Message(title=title,body=body,user_id=current_user.id)
      db.session.add(message)
      db.session.commit()
      flash('已成功发送', 'info')
      return redirect(url_for('message'))
   page = request.args.get('page', 1, type=int)
   per_page = app.config['MESSAGE_PER_PAGE']
   pagination = Message.query.order_by(Message.timestamp.desc()).paginate(page,per_page=per_page)
   messages = pagination.items
   return render_template('message.html',pagination=pagination,messages=messages,bs=bs,form=form)
   
   
@app.route("/userindex")
@login_required
def userindex():
   pass
   
   
@app.route("/about")
def about():
   pass
   
   
@app.route("/zzd", methods=['GET', 'POST'])
def zzd():
   if request.method == 'POST':
      data = request.get_json()
      if data['qy'] == "low":
         zzd_two = random.randint(0,50)
      else:
         zzd_two = random.randint(50,100)
      current_user.Intellectual_disability = zzd_two
      db.session.commit()
      return jsonify(zzd=zzd_two)
   zzd_one = random.randint(0,100)
   login = current_user.is_authenticated
   return jsonify(zzd=zzd_one,login=login)
   
   
@app.route("/login", methods=['GET', 'POST'])
def login():
   if current_user.is_authenticated:
      return redirect(url_for('index'))
   
   form = LoginForm()
   if form.validate_on_submit():
      username = form.username.data
      password = form.password.data
      remember = form.remember_me.data
      
      user = User.query.filter_by(username=username).first()
       
      if user is not None and user.validate_password(password):
         login_user(user,remember)
         flash('欢迎回来', 'info')
         return redirect_back()
      flash('密码或用户名错误！', 'warning')
   return render_template('login.html', form=form,bs=bs)
      
   
@app.route("/logout")
@login_required
def logout():
   logout_user()
   flash('已退出登录', 'info')
   return redirect(url_for('index'))
   
   
@app.route("/register", methods=['GET', 'POST'])
def register():
   if current_user.is_authenticated:
      return redirect(url_for('index'))

   form = RegisterForm()
   if form.validate_on_submit():
      name = form.name.data
      email = form.email.data.lower()
      username = form.username.data
      password = form.password.data
      user = User(name=name, email=email, username=username)
      user.set_password(password)
      db.session.add(user)
      db.session.commit()
      flash('已成功注册', 'info')
      return redirect(url_for('login'))
   return render_template('register.html', form=form,bs=bs)
   
   

   