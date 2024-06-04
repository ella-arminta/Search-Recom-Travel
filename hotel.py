from nameko.rpc import rpc

import dependencies

class HotelService:

    name = 'hotel_service'

    database = dependencies.Database()

    @rpc
    def get_all_room_type(self):
        room_types = self.database.get_all_room_type()
        return room_types

    @rpc
    def get_all_room(self):
        rooms = self.database.get_all_room()
        return {
            'code' : 200,
            'data' : rooms
        }
    
    @rpc
    def get_all_hotel(self):
        hotels = self.database.get_all_hotel()
        return hotels