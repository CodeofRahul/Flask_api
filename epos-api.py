from flask import Flask, request
from flask_restful import Resource, Api
from flask_restful import reqparse

# Initialise the flask class and the API libarary
app = Flask(__name__)
api = Api(app)

rms = {
    "restaurant":{"name":"KFC", "Phone Number":"07894334854", "Address":"122 Newclose, London"},
    "menu":{
        "Wings":{"price":5.50, "quantity_remaining":30}
    }
}

class restaurant(Resource):
    def get(self):
        return rms['restaurant']
    
class menu(Resource):
    def get(self, item):
        try:
            return rms['menu'][item]
        except KeyError:
            return {}

    
# Mapping classes to different end points
api.add_resource(restaurant, "/restaurant")
api.add_resource(menu, "/menu/<item>")

# Starting the server
if __name__ == "__main__":
    app.run(debug=True)

