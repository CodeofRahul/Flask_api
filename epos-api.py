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
        return "Welcome to RMS"
    
# Mapping classes to different end points
api.add_resource(restaurant, "/")

# Starting the server
if __name__ == "__main__":
    app.run(debug=True)
    