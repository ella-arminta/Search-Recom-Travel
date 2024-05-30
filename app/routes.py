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

@app.route('/user', methods=['POST','GET'])
def user():
    if request.method == 'POST':
        response = hotel_controller.create_users_controller()
        return response
    else:
        response = hotel_controller.get_users_controller()
        return response
    return response

# routes transportasi - Ella

# routes Airlines - Yu

# routes Insurance - Yu

# routes travel agent - MAP
#VIEWS
@app.route('/agentview', methods=['GET'])
def viewAgent():
    return agent_controller.view()

@app.route('/agentview', methods=['GET'])
def viewAgent2():
    return agent_controller.view2()

@app.route('/agentcontroller', methods=['GET'])
def viewAgentController():
    return agent_controller.test_controller()

#Routes Agent
@app.route('/agent', methods=['GET'])
def agent():
    agent_name = request.args.get('agent_name')
    response = agent_controller.get_agent(agent_name)
    return response

# routes Atraksi - MAP
#VIEWS
@app.route('/attractionview', methods=['GET'])
def viewAttraction():
    return attraction_controller.view()

@app.route('/attractioncontroller', methods=['GET'])
def viewAttractionController():
    return attraction_controller.test_controller()

#Routes Attraction
@app.route('/attraction', methods=['GET'])
def attraction():
    attraction_name = request.args.get('attraction_name')
    response = attraction_controller.get_attraction(attraction_name)
    return response