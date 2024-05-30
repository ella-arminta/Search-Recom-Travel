from flask import jsonify, render_template
from app.models.Insurance import Insurance

# Agent
class InsuranceController:
    def __init__(self):
        self.insurance = Insurance()

    def view(self):
        data = self.get_users()
        return render_template('insurance.php', data=data)
    
    
    def get_users(self):
        allUsers = self.insurance.get_all_user()
        # pemfilteran user
        return allUsers
    
    
    def get_insurance(self):
        allInsurance = self.insurance.get_all_kategori_asuransi()
        return allInsurance
    
    def test_controller(self):
        return jsonify({'message':'Ini INSURANCE :)'}),200