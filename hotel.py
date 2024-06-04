from nameko.rpc import rpc

import dependencies

class HotelService:

    name = 'hotel_service'

    database = dependencies.Database()
    
    @rpc
    def get_all_hotel(self):
        hotel_services = self.database.get_service_by_type(1)
        return hotel_services