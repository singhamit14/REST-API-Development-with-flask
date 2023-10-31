from db.user import UserDatabase
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from Schemas import UserSchema, UserQuerrySchema
import hashlib
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from blocklist import BLOCKLIST

blp = Blueprint("Users",__name__,description='Operations on users')

@blp.route("/login")
class UserLogin(MethodView):
    def __init__(self):
        self.db = UserDatabase()

    @blp.arguments(UserSchema)
    def post(self, request_data):

        username = request_data["username"]
        password = hashlib.sha256(request_data["password"].encode('utf-8')).hexdigest()
        user_id = self.db.verify_user(username,password)
        if user_id:
            return {
                "access_token" : create_access_token(identity=user_id)
            }
        abort(404, message="username or password is incorrect")


@blp.route("/logout")
class UserLogout(MethodView):

    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {
               "message": "Successfully logged out."
        }
     

@blp.route("/user") 
class Item(MethodView):

    def __init__(self):
        self.db = UserDatabase()

    @blp.response(200, UserSchema)
    @blp.arguments(UserQuerrySchema, location="query")
    def get(self, args):
        id = args.get("id")
        result = self.db.get_user(id)
        if result is None:
            abort(404, message="User does't exist")   
        return result

    @blp.arguments(UserSchema)
    def post(self, request_data):
        username = request_data["username"]
        password = hashlib.sha256(request_data["password"].encode('utf-8')).hexdigest()
        if self.db.add_user(username, password):
            return {"massege": "User added Successfully"}, 201
        return abort(403, message="User allready exist") 

    @blp.arguments(UserQuerrySchema, location="query")
    def delete(self, args):
        id = args.get("id")
        if self.db.delete_user(id):
                return {"message":"Item deleted succesfully"}
        abort(404, message="Given id does't exist")