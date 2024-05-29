from flask import jsonify, render_template
from app.models.Attraction import Attraction

# Attraction
class AttractionController:
    def __init__(self):
        self.attraction = Attraction()
    
    def view(self):
        data = self.get_attraction()
        return render_template('attraction.php', data=data)
    
    def get_attraction(self):
        allAttraction = self.attraction.get_all_attraction()
        # pemfilteran attraction
        return allAttraction
    
    def test_controller(self):
        return jsonify({'message':'Hi salken! :) '}),200