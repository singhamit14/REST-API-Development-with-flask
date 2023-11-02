import pyodbc

class ItemDatabase():
        def __init__(self):
                # self.conn = pyodbc.connect('DRIVER={SQL Server};SERVER=Amit-Laptop;DATABASE=cafe;')
                # self.cursor = self.conn.cursor()
                self.conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=cafe-rn.database.windows.net;DATABASE=cafe;UID=singhamit14;PWD=xxxxxxxxxxx')
                self.cursor = self.conn.cursor()
        
        def get_items(self):
                result = []
                query = "SELECT * FROM item"
                self.cursor.execute(query)
                for row in self.cursor.fetchall():
                        item_dict = {}
                        item_dict["id"], item_dict["name"], item_dict["price"] = row
                        result.append(item_dict)
                return result

        def get_item(self, item_id):
                query = f"SELECT * FROM item Where id = '{item_id}'"
                self.cursor.execute(query)
                for row in self.cursor.fetchall():
                        item_dict = {}
                        item_dict["id"], item_dict["name"], item_dict["price"] = row
                        return [item_dict]

        def add_item(self, id, body):
                query = f"insert into item (id, name, price) values ('{id}', '{body['name']}', {body['price']})"
                self.cursor.execute(query)
                self.conn.commit()

        def update_item(self, id, body):
                query = f"UPDATE item SET name = '{body['name']}', price = {body['price']} where id = '{id}'"
                self.cursor.execute(query)
                if self.cursor.rowcount == 0:
                        return False
                else:
                        self.conn.commit()
                        return True
                    
        def delete_item(self, id):
                query = f"DELETE FROM item where id = '{id}'"
                self.cursor.execute(query)
                if self.cursor.rowcount == 0:
                        return False
                else:
                        self.conn.commit()
                        return True


# db = ItemDatabase()
# db.add_item(id='a5ee97d5b9084910b70bc80fc6034368', body={'name':'Orange Juice', 'price': 50 })












# items = [
#         { "id": "585e42e0596d4f9fa0ec53238016f00a",
#                 "item":{
#                         'name': 'Green Apple Mojito',
#                         'price': 160
#                        },
#         },
#         { "id": "a5ee97d5b9084910b70bc80fc6034367",
#                 "item":{
#                         'name': 'Momos',
#                         'price': 60
#                        },
#         },
#         { "id": "4d756100436e46c59af46c208a33fd29",
#                 "item":{
#                         'name': 'Special Chat',
#                         'price': 45
#                        }
#         }
# ]