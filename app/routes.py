from app import app
from app.controllers.HotelController import HotelController
from app.controllers.AttractionController import AttractionController
from app.controllers.AgentController import AgentController
from flask import request

hotel_controller = HotelController()
agent_controller = AgentController()
attraction_controller = AttractionController()
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
@app.route('/agent', methods=['GET'])
def agent():
    agent_name = request.args.get('agent_name')
    response = agent_controller.get_agent(agent_name)
    return response

# routes Atraksi - MAP
@app.route('/attraction', methods=['GET'])
def attraction():
    attraction_name = request.args.get('attraction_name')
    response = attraction_controller.get_attraction(attraction_name)
    return response