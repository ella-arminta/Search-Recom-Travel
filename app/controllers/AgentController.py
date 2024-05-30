from flask import jsonify, render_template
from app.models.Agent import Agent

# Agent
class AgentController:
    def __init__(self):
        self.agent = Agent()
        self.detail = Agent()
    def view(self):
        data = self.get_agent()
        # data = self.get_package()
        # data = self.get_all_detail_package()
        return render_template('agent.php', data=data)
    
    def view2(self):
        data2 = self.get_package()
        return render_template('agent.php',data=data2)
    
    def get_agent(self):
        allAgent = self.agent.get_all_agent()
        # pemfilteran agent
        return allAgent
    
    def get_package(self):
        allPackage = self.agent.get_all_package()
        return allPackage
    
    def get_all_detail_package(self):
        allDetail = self.detail.get_all_detail_package()
        return allDetail
    
    def test_controller(self):
        return jsonify({'message':'Ini Travel AGENT! :) '}),200