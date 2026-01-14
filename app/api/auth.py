from datetime import datetime as dt, timezone
from flask import Blueprint, request, jsonify, session
from ..db import db 
from ..db.models import User
api_v1_auth = Blueprint(name='api_v1_auth',import_name=__name__,url_prefix='/api/v1/auth')


@api_v1_auth.route("/login", methods=['POST'])
def login_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    try:
        user = db.session.execute(db.select(User).filter_by(email=email)).scalar_one()
        if not user:
            return jsonify({ "message": "bad request"}), 400 
        is_password_valid = user.check_password(password)
        if not is_password_valid:
            return jsonify({ "message": "bad request"}), 400 
        
        session['email'] = data.get('email')
        session['user_id'] =  user.id
        session['role'] = user.role.value
        session.permanent = True
        user.last_login = dt.now(timezone.utc)
        db.session.commit()
        print(session)
        return jsonify({ "message": "user logged in"}), 200
    except:
        return jsonify({ "message": "bad request"})

@api_v1_auth.route('/logout')
def logout():
    session.pop('email', None)
    session.pop('user_id', None)
    session.pop('role', None)
    return jsonify({"message":"user logged out"}), 200