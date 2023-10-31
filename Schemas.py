from marshmallow import Schema, fields

class ItemSchema(Schema):
    # id = fields.Str(dump_only=True)   # if any case we have to return then write it 
    name = fields.Str(required=True)     # for somthing we have to add then write it 
    price = fields.Int(required=True)    

class ItemGetSchema(Schema):
    id = fields.Str(dump_only=True)  # we have create this function for showing data type in swagger-ui
    # item = fields.Nested(ItemSchema)  # if we want use any schma in another schema then we use Nested
    name = fields.Str(dump_only=True)     # for somthing we have to add then write it 
    price = fields.Int(dump_only=True)

# class SuccessMessageSchema(Schema):
#     message = fields.Str(dump_only=True)

class ItemQuerrySchema(Schema):       # we have pass parameter in delete and put so for that we write this class
    id = fields.Str(required=True)

class ItemOptionalQuerrySchema(Schema):       # we have aslo pass parameter in get but it is optional
    id = fields.Str(required=False)

# Users

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)

class UserQuerrySchema(Schema):      
    id = fields.Int(required=True)