from nameko.rpc import rpc
from decimal import Decimal
import dependencies
import requests


class HotelService:

    name = 'hotel_service'

    database = dependencies.Database()
    
    @rpc
    def get_all_hotel(self, id_lokasi, checkin,checkout,people, minprice, maxprice, rating):
        # get all service that is hotel and in a location
        if id_lokasi != '-':
            hotel_services = self.database.get_service_by_type_lokasi(1, id_lokasi)
        else:
            hotel_services = self.database.get_service_by_type(1)

        # get hotel ratings
        rating_data = {}
        ratings_allowed = []
        if rating != '-' and rating != '00000':
            ratings_allowed = []
            for i in range(5):
                if rating[i] == '1':
                    ratings_allowed.append(i + 1)

            try: 
                endpoint_booking = self.database.get_service_by_name('booking')['url']
                response = requests.get(endpoint_booking + '/review/hotel')
                response.raise_for_status()
                rating_data = response.json()
            except requests.exceptions.RequestException as e:
                # Handle any exceptions that occur during the request
                # TODO add error to database
                return {
                    'code': 500,
                    'data': 'Error fetching rating'
                }

        hotels = []
        for hotel_service in hotel_services:
            hotel_service['lokasi'] = self.database.get_lokasi_by_id(hotel_service['id_lokasi'])
            endpoint_url = hotel_service['url']

            
            # check hotel ratings
            if ratings_allowed: 
                if hotel_service['nama'] not in rating_data:
                    continue
                if rating_data[hotel_service['nama']] not in ratings_allowed:
                    continue
            
            # Get hotel rooms
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
                        'room_type_id' : 1,
                        'total_room' : 2,
                        'type' : 'Suite',
                        'detail' : 'asdfasdf',
                        'capacity': 3,
                        'price' : 200000
                    },
                    {   
                        'room_type_id' : 2,
                        'total_room' : 3,
                        'type' : 'Master',
                        'detail' : 'asdfasdf',
                        'capacity': 6,
                        'price' : 1000000
                    },
                ]
                
                # Filter hotels
                for d in data:
                    if minprice != '-': 
                        if d['room_type']['price'] < minprice:
                            continue
                    if maxprice != '-':
                        if d['room_type']['price'] > maxprice:
                            continue
                    if people != '-':
                        if d['room_type']['capacity'] < people:
                            continue
                    if people != '-':
                        if d['room_type']['capacity'] != people:
                            continue
                    
                    # check hotel Availability 
                    # Panggil function check availabilitynya Yull
                    # input : room_type_id, checkin, checkout
                    # output : boolean
                    available = True
                    if not available:
                        continue
                    
                    if hotel_service['id'] not in hotels:
                        hotels[hotel_service['id']] = {
                            'hotel_id': hotel_service['id'],
                            'hotel_name': hotel_service['nama'],
                            'hotel_location': hotel_service['lokasi']['nama'],
                            'hotel_url': hotel_service['url'],
                            'rooms': []
                        }

                    hotels[hotel_service['id']]['rooms'].append({
                        'room_id': d['room_id'],
                        'room_type': d['room_type']['type'],
                        'room_price': d['room_type']['price'],
                        'room_capacity': d['room_type']['capacity'],
                        'room_detail': d['room_type']['detail']
                    })

            except requests.exceptions.RequestException as e:
                # Handle any exceptions that occur during the request
                # TODO add error to database
                continue


        return {
            'code': 200,
            'data': hotels
        }