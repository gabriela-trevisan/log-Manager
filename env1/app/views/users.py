from app import db
from flask import request, jsonify
from ..models.users import Users, user_schema, users_schema


"""Retorna lista de alimentos"""


# def get_users():
#     name = request.args.get('name')
#     if name:
#         users = Users.query.filter(Users.name.like(f'%{name}%')).all()
#     else:
#         users = Users.query.all()
#     if users:
#         result = users_schema.dump(users)
#         return jsonify({'message': 'successfully fetched', 'data': result.data})

#     return jsonify({'message': 'nothing found', 'data': {}})


def get_user(current_user):
    print('get_user()', current_user)

    # FIXME:
    # if not current_user.admin:
    #     return jsonify({'message' : 'Cannot perform that function!'})

    username = request.args.get('username')
    
    if username:
        users = Users.query.filter(Users.username.like(f'%{username}%')).all()
    else:
        users = Users.query.all()
    if users:
        result = users_schema.dump(users)
        return jsonify({'message': 'successfully fetched', 'data': result})

    return jsonify({'message': 'nothing found', 'data': {}})


# """Retorna usuário específico pelo ID no parametro da request"""


# def get_user(id):
#     food = Users.query.get(id)
#     if food:
#         result = food_schema.dump(food)
#         return jsonify({'message': 'successfully fetched', 'data': result.data}), 201

#     return jsonify({'message': "food don't exist", 'data': {}}), 404


"""Cadastro de alimentos com validação de existência"""


# def post_food(name):
#     food = food_by_name(name)
#     if food:
#         result = food_schema.dump(food)
#         return jsonify({'message': 'food already exists', 'data': {}})

#     food = Users(name)
#     print(food)
#     try:
#         db.session.add(food)
#         db.session.commit()
#         result = food_schema.dump(food)
#         print(result)
#         return jsonify({'message': 'successfully registered', 'data': result.name}), 201
#     except:
#         return jsonify({'message': 'unable to save', 'data': {}}), 500


"""Atualiza usuário baseado no ID, caso o mesmo exista."""


# def update_user(id):
#     username = request.json['username']
#     password = request.json['password']
#     name = request.json['name']
#     email = request.json['email']
#     food = Users.query.get(id)

#     if not food:
#         return jsonify({'message': "food don't exist", 'data': {}}), 404

#     pass_hash = generate_password_hash(password)

#     if food:
#         try:
#             food.username = username
#             food.password = pass_hash
#             food.name = name
#             food.email = email
#             db.session.commit()
#             result = food_schema.dump(food)
#             return jsonify({'message': 'successfully updated', 'data': result.data}), 201
#         except:
#             return jsonify({'message': 'unable to update', 'data':{}}), 500


# """Deleta usuário com base no ID da request"""


# def delete_user(id):
#     food = Users.query.get(id)
#     if not food:
#         return jsonify({'message': "food don't exist", 'data': {}}), 404

#     if food:
#         try:
#             db.session.delete(food)
#             db.session.commit()
#             result = food_schema.dump(food)
#             return jsonify({'message': 'successfully deleted', 'data': result.data}), 200
#         except:
#             return jsonify({'message': 'unable to delete', 'data': {}}), 500


# def food_by_name(name):
#     try:
#         return Users.query.filter(Users.name == name).one()
#     except:
#         return None

def get_password(username):
    user = Users.query.filter(Users.username == username).first()
    if user:
        return user.password
    return None


def get_user_auth(username):
    user = Users.query.filter(Users.username == username).first()
    if user:
        result = user_schema.dump(user)
        print('result: ', result)
        # print(result['password'])
        return result
        # return jsonify({'message': 'successfully fetched', 'data': result}), 201

    return jsonify({'message': "user don't exist", 'data': {}}), 404