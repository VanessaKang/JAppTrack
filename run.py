import os
from app import create_app, db, ma
from app.models.company import Company
from app.models.posting import Posting
from app.models.user import User
from app.models.interview import Interview
from app.models.file import File
from app.models.application import Application, ApplicationStatusEnum
from marshmallow_enum import EnumField
from flask import jsonify

basedir = os.path.abspath(os.path.dirname(__file__))

app = create_app()
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir, "app.db")

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field()
    first_name = ma.auto_field()
    last_name = ma.auto_field()
    applications = ma.auto_field()

class ApplicationSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Application
        include_fk = True
    
    id = ma.auto_field()
    submission_date = ma.auto_field()
    status = EnumField(ApplicationStatusEnum)
    

@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Company": Company, "Posting": Posting,
            "User": User, "Interview": Interview, "File": File,
            "Application": Application,
            "UserSchema": UserSchema, "ApplicationSchema": ApplicationSchema}

@app.route("/api/users")
def get_users():
    """
    Example return
    {
        "results": [
            {id=id, first_name='vanessa', last_name='kang', username='vkang'},
            {id=id, first_name='robin', last_name='kang', username='vkang'},    
        ]
    }
    """

    results = []
    for user in User.find_active():
        results.append(user.to_json())
    return jsonify({
        "results": results
    })

@app.route("/api/users/<int:id>")
def get_user_from_id(id):
    """
    Example return
    {
        "results": [
            {id=id, first_name='vanessa', last_name='kang', username='vkang'},
            {id=id, first_name='robin', last_name='kang', username='vkang'},    
        ]
    }
    """
    if User.find_by_id(id):
        return {"results": User.find_by_id(id).to_json()}
    return {
        "error": {
            "code": 404,
            "message": "User with that id not found"
        }
    }, 404

@app.after_request
def after_request_func(response):
    print(response.headers)
    response.headers['Server'] = 'NOT GOING TO SHOW YOU'
    print(response.headers)
    return response
