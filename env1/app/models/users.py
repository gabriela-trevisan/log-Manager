from app import db, ma
import datetime

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    date_create = db.Column(db.DateTime, default=datetime.datetime.now())
    date_update = db.Column(db.DateTime, onupdate=datetime.datetime.now())

    def __init__(self, username, name, email, password):
        self.username = username
        self.name = name
        self.email = email
        self.password = password


class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'name', 'email', 'password', 'date_create', 'date_update')

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)