from nameko.rpc import rpc
import requests
import dependencies

class AirlinesService:

    name = 'airlines_service'

    database = dependencies.Database()

    # @rpc
    # def get_all_airline(self,nama_maskapai):
    #     airlines_service = self.database.get_service_by_type(2)
    #     return airlines_service
    @rpc
    def get_all_airlines(self,airport_origin_location_code,airport_destination_location_code,minprice,maxprice,date,start_time,end_time):
        flights_services = self.database.get_service_by_type(2)
        flights=[]
        
        for flights_service in flights_services:
            endpoint_url = flights_service['url']
            
            #get all flights
            try:
                 # /airlines
                # response = requests.get(endpoint_url)
                # response.raise_for_status()
                # data = response.json()
                # data yang diterima bentuknya : DUMMY
                # PERTANYAAN apakah hotel masih menyimpan hotel detail
                # yang ngecek apakah roomnya avail atau gk itu dari function hotel, atau function search&Recom
                data = [
                    {   
                        'flight_code':'GA 208',
                        'airport_origin_name':'Soekarno-Hatta Intl',
                        'airport_origin_location_code':'CGK',
                        'airport_origin_city_name':'Jakarta',
                        'airport_destination_name':'New Yogyakarta Int.',
                        'airport_destination_location_code':'YIA',
                        'airport_destination_city_name':'Yogyakarta',
                        'start_time':'11:30:00',
                        'end_time':'12:50:00',
                        'class_name':'Business Class',
                        'capacity':50,
                        'price':3000000,
                        'date':'2024-06-12',
                        'weight':30,
                        'delay':0,
                    },
                    {   
                        'flight_code':'ID 123',
                        'airport_origin_name':'Bandung Airport',
                        'airport_origin_location_code':'BDO',
                        'airport_origin_city_name':'Bandung',
                        'airport_destination_name':'Surabaya Airport',
                        'airport_destination_location_code':'SUB',
                        'airport_destination_city_name':'Surabaya',
                        'start_time':'13:30:00',
                        'end_time':'15:50:00',
                        'class_name':'Economy',
                        'capacity':100,
                        'price':1000000,
                        'date':'2024-08-12',
                        'weight':50,
                        'delay':0,
                    },
                ]
                
                for d in data:
                    # filter
                    #     cek berdasarkan asal & tujuan
                    if airport_origin_location_code != '-' and d['airport_origin_location_code'] != airport_origin_location_code:
                        continue
                    if airport_destination_location_code != '-' and d['airport_destination_location_code'] != airport_destination_location_code:
                        continue

                    # Check price
                    if minprice != '-' and d['price'] < minprice:
                        continue
                    if maxprice != '-' and d['price'] > maxprice:
                        continue  

                    # Check date
                    if date != '-' and d['date'] != date:
                        continue

                    # Check time
                    if start_time != '-' and d['start_time'] != start_time:
                        continue
                    if end_time != '-' and d['end_time'] != end_time:
                        continue
                    # sort
                    flights.append(d)
                
                unique_flights = []
                seen = set()
                for flight in flights:
                    flight_tuple = tuple(flight.items())
                    if flight_tuple not in seen:
                        seen.add(flight_tuple)
                        unique_flights.append(flight)
            except requests.exceptions.RequestException as e:
                # Handle any exceptions that occur during the request
                # TODO add error to database
                continue
            
        return{
            'code':200,
            'data':unique_flights
        }