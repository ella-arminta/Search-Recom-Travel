from nameko.rpc import rpc
from decimal import Decimal
import searchrecom.dependencies as dependencies
import requests
import random


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
        
        # get hotel ratings and popularity from review (for sort by reviewscore/countBooked and popularity)
        review = {}
        ratings_allowed = []
        if rating != '-' and rating != '00000' and len(rating) == 5:
            ratings_allowed = []
            for i in range(5):
                if rating[i] == '1':
                    ratings_allowed.append(i + 1)
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

            # Get Hotel Price start from (for sort by price)
            hotel_start_price = None
            
            # check hotel ratings
            # if ratings_allowed: 
            #     if hotel_service['nama'] not in rating_data:
            #         continue
            #     if rating_data[hotel_service['nama']] not in ratings_allowed:
            #         continue
            
            # Get hotel rooms
            try: 
                # /rooms
                # response = requests.get(endpoint_url + '/rooms/checkin/'+checkin+'/checkout'+checkout)
                # response.raise_for_status()
                # data = response.json()
                # availability dicek kel hotel
                data = [
                    {   
                        'room_type_id' : 1,
                        'total_room' : 2,
                        'type' : 'Suite',
                        'detail' : 'asdfasdf',
                        'capacity': 3,
                        'price' : random.randint(1, 10)
                    },
                    {   
                        'room_type_id' : 2,
                        'total_room' : 3,
                        'type' : 'Master',
                        'detail' : 'asdfasdf',
                        'capacity': 6,
                        'price' : random.randint(1, 10)
                    },
                    {   
                        'room_type_id' : 2,
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
                    
                    if room != '-':
                        minpeople = int(people / room)
                    else:
                        minpeople = people
                    # if people != '-': #Bakal di functionnya yul pengecekannya
                    #     if d['room_type']['capacity'] < people:
                    #         continue
                    
                    # check hotel Availability 
                    # Panggil function check availabilitynya Yull
                    # input : room_type_id, checkin, checkout
                    # output : boolean
                    available = True
                    if not available:
                        continue
                    
                    if temp_hotel == {}:
                        temp_hotel = {
                            'hotel_id': hotel_service['id'],
                            'hotel_name': hotel_service['nama'],
                            'hotel_location': hotel_service['lokasi']['nama_kota'],
                            'hotel_url': hotel_service['url'],
                            # 'hotel_score' : review[hotel_service['nama']]['rating'] if hotel_service['nama'] in review else 0,
                            'hotel_score' : random.randint(1, 10),
                            # 'hotel_popularity' : review[hotel_service['nama']]['countBooked'] if hotel_service['nama'] in review else 0,
                            'hotel_popularity' : random.randint(1, 10),
                            'rooms': []
                        }
                    
                    temp_hotel['rooms'].append({
                        'room_id': d['room_type_id'],
                        'room_type': d['type'],
                        'room_price': d['price'],
                        'room_capacity': d['capacity'],
                        'room_detail': d['detail']
                    })
                
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