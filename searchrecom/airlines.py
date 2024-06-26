from nameko.rpc import rpc
import requests
import searchrecom.dependencies as dependencies

class AirlinesService:

    name = 'airlines_service'

    database = dependencies.Database()
    # @rpc
    # def get_all_airline(self,nama_maskapai):
    #     airlines_service = self.database.get_service_by_type(2)
    #     return airlines_service
    @rpc
    def get_all_airlines(self,airport_origin_location_code,airport_destination_location_code,minprice,maxprice,date,start_time,end_time,sort):
        flights_services = self.database.get_service_by_type(2)
        flights=[]
        unique_flights = []
        
        for flights_service in flights_services:
            endpoint_url = flights_service['url']
            # url:http://34.200.80.155:8003/flight
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
                        'id':1,
                        'flight_code':'GA208',
                        'airport_origin_name':'Soekarno-Hatta Intl',
                        'airport_origin_location_code':'CGK',
                        'airport_origin_city_name':'Jakarta',
                        'airport_destination_name':'New Yogyakarta Int.',
                        'airport_destination_location_code':'YIA',
                        'airport_destination_city_name':'Yogyakarta',
                        'start_time':'17:30:00',
                        'end_time':'18:50:00',
                        'class_name':'Business Class',
                        'capacity':50,
                        'price':3000000,
                        'date':'2024-06-12',
                        'weight':30,
                        'delay':0,
                    },
                    {   
                        'id':2, 
                        'flight_code':'ID123',
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
                    
                    {   
                        'id':3, 
                        'flight_code':'QR1456',
                        'airport_origin_name':'New Yogyakarta Int.',
                        'airport_origin_location_code':'YIA',
                        'airport_origin_city_name':'Yogyakarta',
                        'airport_destination_name':'Bandung Airport',
                        'airport_destination_location_code':'BDO',
                        'airport_destination_city_name':'Bandung',
                        'start_time':'14:30:00',
                        'end_time':'15:50:00',
                        'class_name':'Economy',
                        'capacity':50,
                        'price':5000000,
                        'date':'2024-06-12',
                        'weight':30,
                        'delay':0,
                    },
                ]
                
                for flight in data:  # Assuming `data` is a list of flight dictionaries
                # Filter based on origin & destination
                    if airport_origin_location_code != '-' and flight['airport_origin_location_code'] != airport_origin_location_code:
                        continue
                    if airport_destination_location_code != '-' and flight['airport_destination_location_code'] != airport_destination_location_code:
                        continue

                    # Check price
                    if minprice != '-' and flight['price'] < minprice:
                        continue
                    if maxprice != '-' and flight['price'] > maxprice:
                        continue  

                    # Check date
                    if date != '-' and flight['date'] != date:
                        continue

                    # Check time
                    if start_time != '-' and flight['start_time'] != start_time:
                        continue
                    if end_time != '-' and flight['end_time'] != end_time:
                        continue

                    flights.append(flight)
                
                unique_flights = []
                seen = set()
                for flight in flights:
                    flight_tuple = tuple(flight.items())
                    if flight_tuple not in seen:
                        seen.add(flight_tuple)
                        unique_flights.append(flight)
                
                if sort!='-':
                    if sort== 'lowestprice':
                        unique_flights.sort(key=lambda x: x['price'])
                    elif sort == 'earlydeparture':
                        unique_flights.sort(key=lambda x: x['date'])
               
                    
            except requests.exceptions.RequestException as e:
                # Handle any exceptions that occur during the request
                # TODO add error to database
                continue
            
        return{
            'code':200,
            'data':unique_flights
        }
    
    @rpc    
    def get_airlines_by_id(self,service_id,airport_origin_location_code,airport_destination_location_code,flight_date,flight_code):
        flights_services = self.database.get_service_by_id(service_id)
        
        flights=[]
        unique_flights = []
        
        for flights_service in flights_services:
            endpoint_url = flights_services['url']
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
                        'service_id':flights_services['id'],
                        'airport_origin_location_code':airport_origin_location_code,
                        'airport_destination_location_code':airport_destination_location_code,
                        'flight_code':flight_code,
                        'date':flight_date,
                        'flight_url':flights_services['url'],
                        'flight_url_full':flights_services['url']+'/'+airport_origin_location_code+'/'+airport_destination_location_code+'/'+flight_date
                    },
                ]
                
                for flight in data:
                    if airport_origin_location_code != '-' and flight['airport_origin_location_code'] != airport_origin_location_code:
                        continue
                    if airport_destination_location_code != '-' and flight['airport_destination_location_code'] != airport_destination_location_code:
                        continue
                    if flight_date != '-' and flight['date'] != flight_date:
                        continue
                    if flight_code != '-' and flight['flight_code'] != flight_code:
                        continue
                    flights.append(flight)
                
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