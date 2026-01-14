from flask import Blueprint, request, jsonify, session
from ..db import db
from ..db.models import User
api_v1_user = Blueprint(name='api_v1_user',import_name=__name__,url_prefix='/api/v1/users')


@api_v1_user.route("/", methods=["POST", "GET", "PUT", "PATCH"])
def user_list_and_current_user_crud():
    if request.method == "GET":
        if session and (session["role"] == "admin"):
            users = db.session.execute(db.select(User).order_by(User.username)).scalars()
            return jsonify({"users": [user.to_dic() for user in users]})
        return jsonify({ "message": "you are not allowed to access that resource"}), 401
    
    if request.method in ("PATCH","PUT"):
        firstname = request.get_json().get('firstname')
        lastname = request.get_json().get('lastname')
        password = request.get_json().get('password')
        email = request.get_json().get('email')
        if session and 'user_id' in session:
            user = db.get_or_404(User, session['user_id'])
            if email is not None:
                user.email = email 
                session["email"] = email
                session.permanent = True
            if password is not None:
                user.password = password
            if firstname is not None:
                user.firstname = firstname
            if lastname is not None:
                user.lastname = lastname
                db.session.commit()
            return jsonify({ "message": f"user has been successfully updated"}), 200
        else:
            return jsonify({ "message": "bad request"}), 400
          
    
    if request.method == "POST":
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        try:
            user = db.session.execute(db.select(User).filter_by(email=email)).scalar_one()
            if user and (user.email == email):
                return jsonify({"message": "bad request"}), 400
        except:
            new_user = User()
            new_user.password = password
            new_user.firstname = firstname 
            new_user.lastname = lastname
            new_user.email = email
            db.session.add(new_user)
            db.session.commit()
            return jsonify({"message": "user created"}), 201

@api_v1_user.route('/me', methods=["GET"])
def get_me():
    if 'user_id' in session:
        user = db.get_or_404(User, session['user_id'])
        if not user:
            session.pop('email', None)
            session.pop('user_id', None)
            session.pop('role', None)
            return jsonify({ "message": "bad request"}), 400
        return jsonify({"user": user.to_dic()})
    else:
        return jsonify({ "message": "bad request"}), 401


@api_v1_user.route("/<int:id>", methods=['GET', 'PUT', 'PATCH','DELETE'])
def get_user(id):
    try:
        user = db.get_or_404(User, id)
        if request.method in ["PUT", "PATCH"]:
            data = request.get_json()
            firstname = data.get('firstname')
            if (firstname is not None) and firstname.isalpha():
                user.firstname = firstname
            lastname = data.get('lastname')  
            if (lastname is not None) and lastname.isalpha():
                user.lastname = lastname
            email = data.get('email')  
            if (email is not None):
                user.email = email
            password = data.get('password')
            if (password is not None) and len(password) >= 12:
                user.password = password
            return jsonify({"message": f"user with id {id} has been successfully updated"}), 200

        if request.method == "DELETE":
            if session["role"] == "admin" or session["email"] == user.email:
                db.session.delete(user)
                db.session.commit()
                return jsonify({"message":f"user {user.id} has been successfully deleted"}), 200
            else:
                return jsonify({"message":f"you are not allowed to delete the user with id {user.id}"}), 401
            
        if request.method == "GET":
            if 'role' in session and (session["role"] == "admin" or session["email"] == user.email):
                return jsonify({"user": user.to_dic()})
        return jsonify({"message":f"user {user.id}"})  
    except:
        return jsonify({ "message":f"invalid user id : {id}"}) 