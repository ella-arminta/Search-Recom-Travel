from app import app
from app.controllers.HotelController import HotelController
from flask import request

hotel_controller = HotelController()
### VIEWS ###
@app.route('/')
def index():
    return hotel_controller.view()
    


#### API ####
@app.route('/test', methods=['GET'])
def test_route():
    return hotel_controller.test_controller()

# routes hotel - Ella
@app.route('/hotel', methods=['GET'])
def hotel():
    hotel_name = request.args.get('hotel_name')
    response = hotel_controller.get_hotel(hotel_name)
    return response

# routes transportasi - Ella

# routes Airlines - Yu

# routes Insurance - Yu

# routes travel agent - MAP

# routes Atraksi - MAP