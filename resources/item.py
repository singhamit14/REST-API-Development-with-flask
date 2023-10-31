import uuid 
from db.item import ItemDatabase
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from Schemas import ItemSchema,ItemGetSchema,ItemQuerrySchema,ItemOptionalQuerrySchema 
from flask_jwt_extended import jwt_required

blp = Blueprint("items",__name__,description='Operations on items')

@blp.route("/item") 
class Item(MethodView):

    def __init__(self):
        self.db = ItemDatabase()

    @jwt_required()
    @blp.response(200, ItemGetSchema(many=True)) # is schema return many type object the we write like this
    @blp.arguments(ItemOptionalQuerrySchema, location="query")
    def get(self, args):
        id = args.get("id")
        if id is None:
            return self.db.get_items()
        else:
            result = self.db.get_item(id)
            if result is None:
                abort(404, message="Record does't exist")   # we use abort for default value in swagger - ui
            return result
        
    @jwt_required()   
    @blp.arguments(ItemSchema)
    @blp.arguments(ItemQuerrySchema, location="query")
    def put(self, request_data, args):
        id = args.get("id")      
        if self.db.update_item(id, request_data): 
            return {"massege": "Item updated successfully"} 
        abort(404, message="Item not found")

    @jwt_required()
    @blp.arguments(ItemSchema)
    def post(self, request_data):
        id = uuid.uuid4().hex
        self.db.add_item(id,request_data)
        return {"massege": "Item added Successfully"}, 201

    @jwt_required()
    @blp.arguments(ItemQuerrySchema, location="query")
    def delete(self, args):
        id = args.get("id")
        if self.db.delete_item(id):
                return {"message":"Item deleted succesfully"}
        abort(404, message="Given id does't exist")