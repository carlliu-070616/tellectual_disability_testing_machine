from datetime import datetime
from main import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(30),unique=True,index=True)
    password_hash = db.Column(db.String(128))
    Intellectual_disability = db.Column(db.Integer,default=100)
    email = db.Column(db.String(254), unique=True, index=True)
    name = db.Column(db.String(30))
    messages = db.relationship("Message",back_populates="user")
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)


    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)
	
	
class Message(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime,default=datetime.utcnow,index=True)
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"))
    user = db.relationship("User",back_populates="messages")