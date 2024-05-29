from flask import jsonify, render_template
from app.models.Agent import Agent

# Agent
class AgentController:
    def __init__(self):
        self.agent = Agent()
    
    def view(self):
        data = self.get_agent()
        return render_template('agent.php', data=data)
    
    def get_agent(self):
        allAgent = self.agent.get_all_agent()
        # pemfilteran agent
        return allAgent
    
    def test_controller(self):
        return jsonify({'message':'Ini Travel AGENT! :) '}),200