from flask import jsonify, render_template
from app.models.Hotel import Hotel
from app.models.User import User
from app import db

# hotel
class HotelController:
    def __init__(self):
        self.hotel = Hotel()
    
    def view(self):
        data = self.get_hotel()
        return render_template('index.php', data=data)
    
    def get_hotel(self):
        allHotel = self.hotel.get_all_hotel()
        # pemfilteran hotel
        return allHotel
    
    def test_controller(self):
        return jsonify({'message':'Hello World'}),200
    
    # testing 
    def create_users_controller(self):
        user = User(name="sample user",age=10, address="test address")
        db.session.add(user)
        db.session.commit()

        return jsonify({'message':'User created'}),200
    
    def get_users_controller(self):
        users = db.session.query(User).all()
        return jsonify({
            'data': [
                {
                    'name': user.name,
                    'age': user.age,
                    'address': user.address
                } for user in users
            ],
            'message':'Success',
            'code': 200
        }),200
