from urllib.parse import urlparse, urljoin
from flask import Flask, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
import pymysql


app = Flask("main")
app.config.from_pyfile("settings.py")
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


db = SQLAlchemy(app)
pymysql.install_as_MySQLdb()
bs = Bootstrap(app)
login = LoginManager(app)
login.login_view = "login"
login.login_message = u"请先登录！"


@login.user_loader
def load_user(user_id):
   from main.models import User
   user = User.query.get(int(user_id))
   return user
   
   
def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc

    
def redirect_back(default='index', **kwargs):
    for target in request.args.get('next'), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return redirect(target)
    return redirect(url_for(default, **kwargs))


from main import views,errors,commands