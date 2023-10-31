from flask import Flask, request 
import uuid 
from db import items

app = Flask(__name__)


#making unifaorm API we have to remove get,add,post,update, delete from decorater methode

# @app.get("/items")    #http://127.0.0.1:5000/get-items
# def get_items():
#     return {"Items": items}   # if i want only values not unique id so change return{"Items": list(items.values())}


# @app.get("/get-item/<string:name>")    #example of dynamic URL
# def get_item(name):
#     for item in items:
#         if name == item["name"]:
#             return item
#     return {"message":"Record does't exist"}, 404

# @app.get("/item")    #Query parameter(we can fetch data by giving name in query params in postman)
# def get_item():
#     name = request.args.get("name")
#     for item in items:
#         if name == item["name"]:
#             return item
#     return {"message":"Record does't exist"}, 404

@app.get("/item")    #Now we are going to get item by its unique id
def get_item():
    id = request.args.get("id")
    if id is None:
        return {"Items": items}
    try:
        return items[id]
    except KeyError:
        return {"message":"Record does't exist"}, 404

# @app.post("/item")
# def add_item():
#     request_data = request.get_json()  
#     items.append(request_data)
#     return {"massege": "Item added Successfully"}, 201 # it is API code to indicate item is created

@app.post("/item")        #add item and generate its unique id
def add_item(): 
    request_data = request.get_json()
    if "name" not in request_data or "price" not in request_data:  #adding data validation in request body
        return {"message": "'name' and 'price' must be in body"},404
    items[uuid.uuid4().hex] = request_data 
    return {"massege": "Item added Successfully"}, 201

# @app.put("/item")
# def update_item():
#     request_data = request.get_json()  
#     for item in items:
#         if item['name'] == request_data['name']:
#             item['price'] = request_data['price']
#             return {"massege": "Item updated Successfully"}
#     return {"massege": "Given Record doesn't exist"}, 404

@app.put("/item")          # updating item by unique id and we can change both price and name
def update_item():
    id = request.args.get("id")     # this way we can take data from parameter of postman
    if id == None:
        return {"message":"Given id not found"},404 
    if id in items.keys():
        request_data = request.get_json() # this way we can take body data of postman 
        if "name" not in request_data or "price" not in request_data:  #adding data validation in request body
            return {"message": "'name' and 'price' must be in body"},404
        items[id] = request_data
        return {"massege": "Item update successfully"}, 200 
    return {"massege": "Given Record doesn't exist"}, 404

# @app.delete("/item")    
# def delete_item():
#     name = request.args.get("id")
#     for item in items:
#         if name == item["name"]:
#             items.remove(item)
#             return {"message":"Item deleted succesfully"}
#     return {"message":"Record does't exist"}, 404

@app.delete("/item")    
def delete_item():
    id = request.args.get("id")
    if id == None:
        return {"message":"Given id not found"},404 
    if id in items.keys():
        del items[id]
        return {"message":"Item deleted succesfully"}
    return {"message":"Record does't exist"}, 404