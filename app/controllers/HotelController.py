from flask import jsonify, render_template
from app.models.Hotel import Hotel

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