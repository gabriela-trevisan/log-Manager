from app import app
from flask import render_template, request, jsonify, url_for, redirect, make_response
import jwt
from .views import users
import time, datetime
from functools import wraps

app.config['SECRET_KEY'] = 'watson'

def cronometro(funcao):
    print('entrei cronometro')
    def wrapper():
        tempo_inicial = time.time()
        funcao()
        tempo_final = time.time()
        print(f"Duração: {tempo_final - tempo_inicial}")

        # return f(true)
    return wrapper


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        print('entrei decorator token required')
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message' : 'Token is missing!'})

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            print('data: ' , data)
            current_user = users.get_user(data['exp'])
            print('current_user: ', current_user)
        except Exception as e:
            print('Exception!! ', str(e))
            return jsonify({'message' : 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)
    
    return decorated

@app.route('/index')
@app.route('/')
def index():
    # data = "asdasdasdsa"
    return render_template("index.html")


@app.route('/users', methods=['GET'])
@token_required
def get_users(current_user):
    return users.get_user(current_user)


@app.route('/login')
def login():
    auth = request.authorization
    # print(auth)
    
    # busca info do usuario
    user_info = users.get_user_auth(auth.username)
    print(user_info)
    # print(user_info['message'])

    if auth and auth.password == user_info['password']:
        # payload
        token = jwt.encode({
                    'user' : auth.username,
                    'id_user' : user_info['id'],
                    'exp' : datetime.datetime.utcnow() + datetime.timedelta(hours=3)
                    }, 
                    app.config['SECRET_KEY'])
        return jsonify({'token' : token})

    return make_response('Could verify!', 401, {'WWW-Authenticate': 'Basic real="Login Required"'})