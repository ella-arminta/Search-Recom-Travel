from nameko.rpc import rpc
from decimal import Decimal
import searchrecom.dependencies as dependencies
import requests
import random
from datetime import datetime

class TravelAgentService:
    name = 'travel_agent_service'

    database = dependencies.Database()

    @rpc
    def get_all_agent(self, id_lokasi, departuredate, returndate, people, minprice, maxprice, sort):
        data_error = []
        error = False
        package = []
        
        # lokasi
        if id_lokasi != '-':
            package_services = self.database.get_service_by_type_lokasi(3, id_lokasi)
        else:
            package_services = self.database.get_service_by_type(3)


        def validate_date_format(date_str):
            if date_str == '-':
                return True
            try:
                datetime.strptime(date_str, '%Y-%m-%d')
                return True
            except ValueError:
                return False

        if departuredate != '-' and not validate_date_format(departuredate):
            error = True
            data_error.append('Invalid departuredate parameter. must be in format YYYY-MM-DD')
            
        elif returndate != '-' and not validate_date_format(returndate):
            error = True
            data_error.append('Invalid enddate parameter. must be in format YYYY-MM-DD')

        elif departuredate != '-' and returndate != '-':
            # Pengecekan tanggal berlaku
            now = datetime.now()
            if datetime.strptime(departuredate, '%Y-%m-%d') < now:
                error = True
                data_error.append('Invalid startdate parameter. must be after today')
            elif datetime.strptime(departuredate, '%Y-%m-%d') > datetime.strptime(returndate, '%Y-%m-%d'):
                error = True
                data_error.append('Invalid startdate parameter. must be before enddate')

        # Ensure minprice and maxprice are properly handled
        try:
            minprice = int(minprice) if minprice != '-' else 0
        except ValueError:
            minprice = 0

        try:
            maxprice = int(maxprice) if maxprice != '-' else float('inf')
        except ValueError:
            maxprice = float('inf')

        for package_service in package_services:
            package_service['lokasi'] = self.database.get_lokasi_by_id(package_service['id_lokasi'])
            endpoint_url = package_service['url']
            temp_package = {}

             # TODO uncomment
            # get hotel detail
            package_detail = {}
            #  dummy
            package_detail = {
                'id': 1,
                'star' : random.randint(1, 5),
                'image': 'https://hotel-images-soa.s3.amazonaws.com/merlynn_park_hotel.jpg'
            }
            #     # cth package detail
            #     # {
            #     # "service_id" : 3,
            #     # "id": 1,
            #     # "name": "Paket A",
            #     # "description": "liburan ke Jepang",
            #     # "departure_date": "2024-06-18",
            #     # "return_date": "2024-06-22",
            #     # "number_of_people": 4,
            #     # "quota": 20,
            #     # "price": 20000000,
            #     # }
            # try:
            #     #cth endpoint_url:  http://localhost:8000/merlynn_park_hotel/
            #     response = requests.get(endpoint_url)
            #     response.raise_for_status()
            #     package_detail = response.json()
            # except requests.exceptions.RequestException as e:
            #     # Handle any exceptions that occur during the request
            #     self.database.add_request_error(endpoint_url, str(e), package_service['id'], 3)
            #     continue

            # Get Hotel Price start from (for sort by price)
            package_start_price = None

            # Get Package Tour
            try: 
                # TODO uncomment
                # /agent
                # cth path : http://localhost:8000/merlynn_park_hotel/room_type/"2024-06-24"&"2024-06-26"
                # response = requests.get(endpoint_url + '/agent/'+departure_date+'&'+return_date)
                # response.raise_for_status()
                # data = response.json()
                # availability dicek kel hotel

                data = [
                    {   
                        'service_id' : 3,
                        'package_id' : 1,
                        'package_name' : 'Bromo & Semeru Mountain',
                        'description' : 'asdfasdf',
                        'city' : 'Probolinggo',
                        'departure_date' : '2024-09-09',
                        'return_date' : '2024-09-14',
                        'people': 2,
                        'quota' : 10,
                        'price' : random.randint(1, 10)
                    },
                    {   
                        'service_id' : 3,
                        'package_id' : 2,
                        'package_name' : 'Nusa Lembongan Bali',
                        'description' : 'asdfasdf',
                        'city' : 'Nusa Dua, Bali',
                        'departure_date' : '2024-10-10',
                        'return_date' : '2024-10-16',
                        'people': 4,
                        'quota' : 5,
                        'price' : random.randint(1, 10)
                    },
                    {   
                        'service_id' : 3,
                        'package_id' : 3,
                        'package_name' : 'Gili Trawangan Lombok',
                        'description' : 'asdfasdf',
                        'city' : 'Lombok',
                        'departure_date' : '2024-11-03',
                        'return_date' : '2024-11-09',
                        'people': 3,
                        'quota' : 6,
                        'price' : random.randint(1, 10)
                    },
                ]
                
                # Filter Package Tour
                for d in data:
                    packagename = d['package_name']

                    # cek nama atraksi
                    if packagename != '-' and d['package_name'] != packagename:
                        continue

                    if d['price'] < minprice: 
                        continue
                    if d['price'] > maxprice:
                        continue

                    if people != '-' and int(people) > d['quota']:
                        continue


                    package.append(d)
                    
                # Sorting based on sort parameter
                if sort == 'lowestprice':
                    package = sorted(package, key=lambda x: x['price'])
                elif sort == 'highestprice':
                    package = sorted(package, key=lambda x: x['price'], reverse=True)
                elif sort == 'city':
                    package = sorted(package, key=lambda x: x['city'])
                elif sort == 'quota' :
                    package = sorted(package,  key=lambda x: x['quota'], reverse=True)
                elif sort == 'departuredate' :
                    package = sorted(package,  key=lambda x: x['departure_date'])

            except requests.exceptions.RequestException as e:
                # Handle any exceptions that occur during the request
                self.database.add_request_error(endpoint_url+'/package/returndate/'+departuredate+'/returndate'+returndate, str(e), package_service['id'], 3)
                continue

        return {
            'code': 200,
            'data': package
        }
    
    @rpc
    def get_agent_by_id(self, id,people,minprice,maxprice):
        package_service = self.database.get_service_by_id(id)
        package_service['lokasi'] = self.database.get_lokasi_by_id(package_service['id_lokasi'])
        if package_service is None:
            return {
                'code': 404,
                'data': 'Package Tour not found'
            }

        endpoint_url = package_service['url']
        temp_package = {}
        package = []
        # get hotel score and popularity from review (for sort by reviewscore/countBooked and popularity)
        review = {}
        endpoint_booking = self.database.get_service_by_name('booking')['url']
        try: 
            # TODO testing review service
            response = requests.get(endpoint_booking + '/review/agent')
            response.raise_for_status()
            review = response.json()
        except requests.exceptions.RequestException as e:
            # Handle any exceptions that occur during the request
            self.database.add_request_error(endpoint_booking + '/review/agent', str(e), self.database.get_service_by_name('booking')['id'] , 3)
            pass
                # return {
                #     'code': 500,
                #     'data': 'Error fetching rating'
                # }

        # TODO uncomment
        # get hotel detail
        package_detail = {}
        #  dummy
        package_detail = {
            'id': 1,
            'image': 'https://hotel-images-soa.s3.amazonaws.com/merlynn_park_hotel.jpg'
        }
        #     # cth package detail
        #     # {
        #     # "service_id" : 3,
        #     # "id": 1,
        #     # "name": "Paket A",
        #     # "description": "liburan ke Jepang",
        #     # "departure_date": "2024-06-18",
        #     # "return_date": "2024-06-22",
        #     # "number_of_people": 4,
        #     # "quota": 20,
        #     # "price": 20000000,
        #     # }
        # try:
        #     #cth endpoint_url:  http://localhost:8000/merlynn_park_hotel/
        #     response = requests.get(endpoint_url)
        #     response.raise_for_status()
        #     package_detail = response.json()
        # except requests.exceptions.RequestException as e:
        #     # Handle any exceptions that occur during the request
        #     self.database.add_request_error(endpoint_url, str(e), package_service['id'], 3)
        #     continue
        
        # add all data to temp_hotel
        # for key, value in package_detail.items():
        #     temp_package[key] = value

        # Get Hotel Price start from (for sort by price)
        package_start_price = None
        # Get hotel rooms
        try: 
            # TODO uncomment
            # /agent
            # cth path : http://localhost:8000/merlynn_park_hotel/room_type/"2024-06-24"&"2024-06-26"
            # response = requests.get(endpoint_url + '/agent/'+departure_date+'&'+returndate)
            # response.raise_for_status()
            # data = response.json()
            # availability dicek kel hotel
            data = [
                    {   
                        'service_id' : 3,
                        'package_id' : 1,
                        'package_name' : 'Bromo & Semeru Mountain',
                        'description' : 'asdfasdf',
                        'city' : 'Probolinggo',
                        'departure_date' : '2024-09-09',
                        'return_date' : '2024-09-14',
                        'people': 2,
                        'quota' : 10,
                        'price' : random.randint(1, 10)
                    },
                    {   
                        'service_id' : 3,
                        'package_id' : 2,
                        'package_name' : 'Nusa Lembongan Bali',
                        'description' : 'asdfasdf',
                        'city' : 'Nusa Dua, Bali',
                        'departure_date' : '2024-10-10',
                        'return_date' : '2024-10-16',
                        'people': 4,
                        'quota' : 5,
                        'price' : random.randint(1, 10)
                    },
                    {   
                        'service_id' : 3,
                        'package_id' : 3,
                        'package_name' : 'Gili Trawangan Lombok',
                        'description' : 'asdfasdf',
                        'city' : 'Lombok',
                        'departure_date' : '2024-11-03',
                        'return_date' : '2024-11-09',
                        'people': 3,
                        'quota' : 6,
                        'price' : random.randint(1, 10)
                    },
                ]
            # Filter Package Tour
            for d in data:
                packagename = d['package_name']

                # cek nama atraksi
                if packagename != '-' and d['package_name'] != packagename:
                    continue

                if d['price'] < minprice: 
                    continue
                if d['price'] > maxprice:
                    continue

                if people != '-' and int(people) > d['quota']:
                    continue


                package.append(d)
        
            if package != {}:
                package['package_start_price'] = package_start_price

        except requests.exceptions.RequestException as e:
                # Handle any exceptions that occur during the request
                # self.database.add_request_error(endpoint_url+'/package/returndate/'+departuredate+'/returndate'+returndate, str(e), package_service['id'], 3)
                pass

        return {
            'code': 200,
            'data': package
        }
