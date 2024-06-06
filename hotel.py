from nameko.rpc import rpc

import dependencies
import requests

class HotelService:

    name = 'hotel_service'

    database = dependencies.Database()
    
    @rpc
    def get_all_hotel(self, id_lokasi, checkin,checkout,people):
        hotel_services = self.database.get_service_by_type_lokasi(1, id_lokasi)
        hotels = []
        for hotel_service in hotel_services:
            hotel_service['lokasi'] = self.database.get_lokasi_by_id(hotel_service['id_lokasi'])
            endpoint_url = hotel_service['api_get_all']
            try: 
                # /rooms
                response = requests.get(endpoint_url)
                response.raise_for_status()
                data = response.json()
                # data yang diterima bentuknya : DUMMY
                # PERTANYAAN apakah hotel masih menyimpan hotel detail
                # yang ngecek apakah roomnya avail atau gk itu dari function hotel, atau function search&Recom
                data = [
                    {   
                        'room_id' : 1,
                        'room_type' : {
                            'total_room' : 2,
                            'type' : 'Suite',
                            'detail' : 'asdfasdf',
                            'capacity': 3,
                            'price' : 1000000
                        } 
                    },
                    {   
                        'room_id' : 2,
                        'room_type' : {
                            'total_room' : 1,
                            'type' : 'Casual',
                            'detail' : 'asdfasdf',
                            'capacity': 2,
                            'price' : 100000
                        } 
                    },
                ]
                # check room availability 
                # Panggil function check availabilitynya Yull
                # Filter hotels


            except requests.exceptions.RequestException as e:
                # Handle any exceptions that occur during the request
                # TODO add error to database
                continue


        return {
            'code': 200,
            'data': hotels
        }