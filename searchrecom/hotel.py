from nameko.rpc import rpc
from decimal import Decimal
import searchrecom.dependencies as dependencies
import requests
import random
import math

class HotelService:

    name = 'hotel_service'

    database = dependencies.Database()
    
    @rpc
    def get_all_hotel(self, id_lokasi, checkin, checkout,people, minprice, maxprice, rating, sort, room):
        # get all service that is hotel and in a location
        if id_lokasi != '-':
            hotel_services = self.database.get_service_by_type_lokasi(1, id_lokasi)
        else:
            hotel_services = self.database.get_service_by_type(1)
        
        # get hotel star 
        ratings_allowed = []
        if rating != '-' and rating != '00000' and len(rating) == 5:
            ratings_allowed = []
            for i in range(5):
                if rating[i] == '1':
                    ratings_allowed.append(i + 1)
        
        review = {}
        # get hotel score and popularity from review (for sort by reviewscore/countBooked and popularity)
        endpoint_booking = self.database.get_service_by_name('booking')['url']
        try: 
            # TODO testing review service
            response = requests.get(endpoint_booking + '/review/hotel')
            response.raise_for_status()
            review = response.json()
        except requests.exceptions.RequestException as e:
            # Handle any exceptions that occur during the request
            self.database.add_request_error(endpoint_booking + '/review/hotel', str(e), self.database.get_service_by_name('booking')['id'] , 1)
            pass
                # return {
                #     'code': 500,
                #     'data': 'Error fetching rating'
                # }

        hotels = []
        
        for hotel_service in hotel_services:
            hotel_service['lokasi'] = self.database.get_lokasi_by_id(hotel_service['id_lokasi'])
            endpoint_url = hotel_service['url']
            temp_hotel = {}

            # TODO uncomment
            # get hotel detail
            hotel_detail = {}
            #  dummy
            hotel_detail = {
                'id': 1,
                'star' : random.randint(1, 5),
                'image': 'https://hotel-images-soa.s3.amazonaws.com/merlynn_park_hotel.jpg'
            }
            #     # cth hotel detail
            #     # {
            #     # "id": 1,
            #     # "name": "Merlynn Park Hotel",
            #     # "image": "https://hotel-images-soa.s3.amazonaws.com/merlynn_park_hotel.jpg",
            #     # "description": "Not only located within easy reach of various places of interests for your adventure, but staying at Merlynn Park Hotel will also give you a pleasant stay.",
            #     # "star": 5,
            #     # "address": "Jl. K.H.Hasyim Ashari 29-31, Gambir, Petojo Utara, Jakarta, Indonesia, 10130",
            #     # "facilities": "AC, Restaurant, Swimming Pool, 24-Hour Front Desk, Parking, Elevator, WiFi",
            #     # "country": "Indonesia",
            #     # "city": "Jakarta",
            #     # "post_code": "10130"
            #     # }
            # try:
            #     #cth endpoint_url:  http://localhost:8000/merlynn_park_hotel/
            #     response = requests.get(endpoint_url)
            #     response.raise_for_status()
            #     hotel_detail = response.json()
            # except requests.exceptions.RequestException as e:
            #     # Handle any exceptions that occur during the request
            #     self.database.add_request_error(endpoint_url, str(e), hotel_service['id'], 1)
            #     continue

            # Get Hotel Price start from (for sort by price)
            hotel_start_price = None
            
            # check hotel ratings
            if ratings_allowed: 
                if 'star' in hotel_detail:
                    if hotel_detail['star'] not in ratings_allowed:
                        continue
            
            # Get hotel rooms
            try: 
                # TODO uncomment
                # /rooms
                # cth path : http://localhost:8000/merlynn_park_hotel/room_type/"2024-06-24"&"2024-06-26"
                # response = requests.get(endpoint_url + '/room_type/'+checkin+'&'+checkout)
                # response.raise_for_status()
                # data = response.json()
                # availability dicek kel hotel
                data = [
                    {   
                        'total_room' : 2,
                        'id': 1,
                        'type' : 'Suite',
                        'detail' : 'asdfasdf',
                        'capacity': 3,
                        'price' : random.randint(1, 10)
                    },
                    {   
                        'id' : 2, 
                        'total_room' : 3,
                        'type' : 'Master',
                        'detail' : 'asdfasdf',
                        'capacity': 6,
                        'price' : random.randint(1, 10)
                    },
                    {   
                        'id' : 3,
                        'total_room' : 3,
                        'type' : 'Master',
                        'detail' : 'asdfasdf',
                        'capacity': 6,
                        'price' : random.randint(1, 10)
                    },
                ]

                # Filter hotels
                for d in data:

                    if minprice != '-': 
                        if d['price'] < minprice:
                            continue
                    if maxprice != '-':
                        if d['price'] > maxprice:
                            continue

                    # set hotel start price
                    if hotel_start_price is None:
                        hotel_start_price = d['price']
                    else: 
                        if d['price'] < hotel_start_price:
                            hotel_start_price = d['price']
                    
                    minpeople = '-'
                    if room != '-':
                        minpeople = math.ceil(people / room)
                    else:
                        minpeople = people

                    if minpeople != '-':
                        if d['capacity'] < minpeople:
                            continue
                    
                    # check hotel Availability 
                    # Panggil function check availabilitynya Yull
                    # input : type, checkin, checkout
                    # output : boolean
                    available = True
                    if not available:
                        continue
                    
                    if temp_hotel == {}:
                        temp_hotel = {
                            'service_id': hotel_service['id'],
                            'hotel_name': hotel_service['nama'],
                            'hotel_location': hotel_service['lokasi']['nama_kota'],
                            'hotel_url': hotel_service['url'],
                            # 'hotel_score' : review[hotel_service['nama']]['rating'] if hotel_service['nama'] in review else 0,
                            'hotel_score' : random.randint(1, 10),
                            # 'hotel_popularity' : review[hotel_service['nama']]['countBooked'] if hotel_service['nama'] in review else 0,
                            'hotel_popularity' : random.randint(1, 10),
                            'hotel_image': hotel_detail['image'],
                            'star' : hotel_detail['star'] if 'star' in hotel_detail else 0,
                            'rooms': []
                        }
                    
                    # temp_hotel['rooms'].append({
                    #     'room_id': d['type'],
                    #     'room_type': d['type'],
                    #     'room_price': d['price'],
                    #     'room_capacity': d['capacity'],
                    #     'room_detail': d['detail']
                    # })
                    temp_hotel['rooms'].append(d)
                
                if temp_hotel != {}:
                    temp_hotel['hotel_start_price'] = hotel_start_price
                
                # ADD HOTEL and SORT BY
                if temp_hotel != {}:
                    if sort == 'lowestprice':
                        if len(hotels) == 0:
                            hotels.append(temp_hotel)
                            continue
                        else:
                            index = 0
                            for h in hotels:
                                if hotel_start_price <= h['hotel_start_price'] :
                                    hotels.insert(index, temp_hotel)
                                    break
                                elif index == len(hotels) - 1:
                                    hotels.append(temp_hotel)
                                    break
                                index += 1
                    elif sort == 'highestprice':
                        if len(hotels) == 0:
                            hotels.append(temp_hotel)
                            continue
                        else:
                            index = 0
                            for h in hotels:
                                if hotel_start_price >= h['hotel_start_price'] :
                                    hotels.insert(index, temp_hotel)
                                    break
                                elif index == len(hotels) - 1:
                                    hotels.append(temp_hotel)
                                    break
                                index += 1
                    elif sort == 'highestpopularity':
                        if len(hotels) == 0:
                            hotels.append(temp_hotel)
                            continue
                        else:
                            index = 0
                            for h in hotels:
                                if temp_hotel['hotel_popularity'] >= h['hotel_popularity'] :
                                    hotels.insert(index, temp_hotel)
                                    break
                                elif index == len(hotels) - 1:
                                    hotels.append(temp_hotel)
                                    break
                                index += 1
                    elif sort == 'reviewscore':
                        if len(hotels) == 0:
                            hotels.append(temp_hotel)
                            continue
                        else:
                            index = 0
                            for h in hotels:
                                if temp_hotel['hotel_score'] >= h['hotel_score'] :
                                    hotels.insert(index, temp_hotel)
                                    break
                                elif index == len(hotels) - 1:
                                    hotels.append(temp_hotel)
                                    break
                                index += 1
                    else:
                        hotels.append(temp_hotel)

            except requests.exceptions.RequestException as e:
                # Handle any exceptions that occur during the request
                self.database.add_request_error(endpoint_booking+'/rooms/checkin/'+checkin+'/checkout'+checkout, str(e), endpoint_url, 1)

                continue

        return {
            'code': 200,
            'data': hotels
        }
    
    @rpc
    def get_hotel_by_id(self, id, people, minprice, maxprice, room):
        hotel_service = self.database.get_service_by_id(id)
        hotel_service['lokasi'] = self.database.get_lokasi_by_id(hotel_service['id_lokasi'])
        if hotel_service is None:
            return {
                'code': 404,
                'data': 'Hotel not found'
            }

        endpoint_url = hotel_service['url']
        temp_hotel = {}

        # get hotel score and popularity from review (for sort by reviewscore/countBooked and popularity)
        review = {}
        endpoint_booking = self.database.get_service_by_name('booking')['url']
        try: 
            # TODO testing review service
            response = requests.get(endpoint_booking + '/review/hotel')
            response.raise_for_status()
            review = response.json()
        except requests.exceptions.RequestException as e:
            # Handle any exceptions that occur during the request
            self.database.add_request_error(endpoint_booking + '/review/hotel', str(e), self.database.get_service_by_name('booking')['id'] , 1)
            pass
                # return {
                #     'code': 500,
                #     'data': 'Error fetching rating'
                # }

        # TODO uncomment
        # get hotel detail
        hotel_detail = {}
        #  dummy
        hotel_detail = {
            'id': 1,
            'star' : random.randint(1, 5),
            'image': 'https://hotel-images-soa.s3.amazonaws.com/merlynn_park_hotel.jpg'
        }
        #     # cth hotel detail
        #     # {
        #     # "id": 1,
        #     # "name": "Merlynn Park Hotel",
        #     # "image": "https://hotel-images-soa.s3.amazonaws.com/merlynn_park_hotel.jpg",
        #     # "description": "Not only located within easy reach of various places of interests for your adventure, but staying at Merlynn Park Hotel will also give you a pleasant stay.",
        #     # "star": 5,
        #     # "address": "Jl. K.H.Hasyim Ashari 29-31, Gambir, Petojo Utara, Jakarta, Indonesia, 10130",
        #     # "facilities": "AC, Restaurant, Swimming Pool, 24-Hour Front Desk, Parking, Elevator, WiFi",
        #     # "country": "Indonesia",
        #     # "city": "Jakarta",
        #     # "post_code": "10130"
        #     # }
        # try:
        #     #cth endpoint_url:  http://localhost:8000/merlynn_park_hotel/
        #     response = requests.get(endpoint_url)
        #     response.raise_for_status()
        #     hotel_detail = response.json()
        # except requests.exceptions.RequestException as e:
        #     # Handle any exceptions that occur during the request
        #     self.database.add_request_error(endpoint_url, str(e), hotel_service['id'], 1)
        #     continue
        
        # add all data to temp_hotel
        for key, value in hotel_detail.items():
            temp_hotel[key] = value

        # Get Hotel Price start from (for sort by price)
        hotel_start_price = None
        # Get hotel rooms
        try: 
            # TODO uncomment
            # /rooms
            # cth path : http://localhost:8000/merlynn_park_hotel/room_type/"2024-06-24"&"2024-06-26"
            # response = requests.get(endpoint_url + '/room_type/'+checkin+'&'+checkout)
            # response.raise_for_status()
            # data = response.json()
            # availability dicek kel hotel
            data = [
                {   
                    'total_room' : 2,
                    'type' : 'Suite',
                    'detail' : 'asdfasdf',
                    'capacity': 3,
                    'price' : random.randint(1, 10)
                },
                {   
                    'total_room' : 3,
                    'type' : 'Master',
                    'detail' : 'asdfasdf',
                    'capacity': 6,
                    'price' : random.randint(1, 10)
                },
                {   
                    'total_room' : 3,
                    'type' : 'Master',
                    'detail' : 'asdfasdf',
                    'capacity': 6,
                    'price' : random.randint(1, 10)
                },
            ]

            # Filter hotels
            i = 0
            for d in data:
                if minprice != '-': 
                    if d['price'] < minprice:
                        continue
                if maxprice != '-':
                    if d['price'] > maxprice:
                        continue

                # set hotel start price
                if hotel_start_price is None:
                    hotel_start_price = d['price']
                else: 
                    if d['price'] < hotel_start_price:
                        hotel_start_price = d['price']
                
                minpeople = '-'
                if room != '-':
                    minpeople = math.ceil(people / room)
                else:
                    minpeople = people

                if minpeople != '-':
                    if d['capacity'] < minpeople:
                        continue
                
                if i == 0:
                    temp2_hotel = {
                        'service_id': hotel_service['id'],
                        'hotel_location': hotel_service['lokasi']['nama_kota'],
                        'hotel_url': hotel_service['url'],
                        # 'hotel_score' : review[hotel_service['nama']]['rating'] if hotel_service['nama'] in review else 0,
                        'hotel_score' : random.randint(1, 10),
                        # 'hotel_popularity' : review[hotel_service['nama']]['countBooked'] if hotel_service['nama'] in review else 0,
                        'hotel_popularity' : random.randint(1, 10),
                        'rooms': []
                    }

                    for key, value in temp2_hotel.items():
                        temp_hotel[key] = value
                
                temp_hotel['rooms'].append(d)
                i += 1
            
            if temp_hotel != {}:
                temp_hotel['hotel_start_price'] = hotel_start_price

        except requests.exceptions.RequestException as e:
                # Handle any exceptions that occur during the request
                # self.database.add_request_error(endpoint_booking+'/rooms/checkin/'+checkin+'/checkout'+checkout, str(e), endpoint_url, 1)
                pass
        
        return {
            'code': 200,
            'data': temp_hotel
        }