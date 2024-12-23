from flask import Flask, request
from flask_restful import Resource, Api
from flask_restful import reqparse

# Initialise the flask class and the API libarary
app = Flask(__name__)
api = Api(app)

rms = {
    "restaurant":{"name":"KFC", "Phone Number":"07894334854", "Address":"122 Newclose, London"},
    "menu":{
        "Wings":{"price":"5.5", "quantity_remaining":"1000"}
    }
}

class restaurant(Resource):
    def get(self):
        return rms['restaurant']

class main(Resource):
    def get(self):
        return rms['menu']



    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('item')
        parser.add_argument('price')
        parser.add_argument('quantity_remaining')    
        # Data that the user has sent to us
        result = parser.parse_args()
        if result['item'] == None or result['price'] == None or result['quantity_remaining'] == None:
            return {"Error":"Missing fields"}

        # Adding item onto rms dictionary
        rms['menu'][result["item"]] = {'price':result['price'], 'quantity_remaining':result['quantity_remaining']}
        return {"message":f"{result['item']} added to the menu successfully!"}

    
class menu(Resource):
    def get(self, item):
        try:
            return rms['menu'][item]
        except KeyError:
            return {}
    
    def put(self, item):
        try:
            rms['menu'][item]
        except KeyError:
            return {"Error":item+" Does not exist on the menu"}
        
        
        parser = reqparse.RequestParser()
        parser.add_argument('price')
        parser.add_argument('quantity_remaining')
        # Data that user has sent to us
        result = parser.parse_args()
        # Update the menu dictionary with data the user has sent
        if result['price'] == None and result['quantity_remaining'] == None:
            return {"Error":"Update either needs price or quantity or both"}
        else:
            # Updating dictionary
            if result["price"] != None:
                rms['menu'][item]['price'] = result['price']
            if result["quantity_remaining"] != None:
                rms["menu"][item]['quantity_remaining'] = result["quantity_remaining"]
            return {"message": item+" Updated!"}

    def delete(self, item):
        # check if the item is valid
        try:
            rms['menu'][item]
        except KeyError:
            return {"Error":item+" Does not exist"}

        # Deleting item from the menu
        del rms['menu'][item]
        return{"message":item+" Deleted!"}

    
# Mapping classes to different end points
api.add_resource(restaurant, "/restaurant")
api.add_resource(menu, "/menu/<item>")
api.add_resource(main,"/menu")

# Starting the server
if __name__ == "__main__":
    app.run(debug=True)

