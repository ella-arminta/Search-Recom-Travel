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
        agent_services = self.database.get_service_by_type(3)
        agent=[]
        package=[]
        
        for agent_service in agent_services:
            endpoint_url = agent_service['url']
            # url:http://3.210.234.45:8003/travel-agent --> travel agent 1. kalo mau lihat package tour, tinggal ditambahi /packages
            # url:http://174.129.21.218:8005//travel-agent --> travel agent 2. kalo mau lihat package tour, tinggal ditambahi /packages
            # url:http://100.29.145.3:8007/travel-agent --> travel agent 3. kalo mau lihat package tour, tinggal ditambahi /packages
            #get all package
            try:
                 # /agent
                response = requests.get(endpoint_url)
                response.raise_for_status()
                data = response.json()
                
                # Ensure that data is a list of dictionaries
                if not isinstance(data, list):
                    continue

                # data = [
                #     {   
                #         'service_id' : 3,
                #         'package_id' : 1,
                #         'package_name' : 'Bromo & Semeru Mountain',
                #         'description' : 'asdfasdf',
                #         'city' : 'Probolinggo',
                #         'departure_date' : '2024-09-09',
                #         'return_date' : '2024-09-14',
                #         'people': 2,
                #         'quota' : 10,
                #         'price' : random.randint(1, 10)
                #     },
                #     {   
                #         'service_id' : 3,
                #         'package_id' : 2,
                #         'package_name' : 'Nusa Lembongan Bali',
                #         'description' : 'asdfasdf',
                #         'city' : 'Nusa Dua, Bali',
                #         'departure_date' : '2024-10-10',
                #         'return_date' : '2024-10-16',
                #         'people': 4,
                #         'quota' : 5,
                #         'price' : random.randint(1, 10)
                #     },
                #     {   
                #         'service_id' : 3,
                #         'package_id' : 3,
                #         'package_name' : 'Gili Trawangan Lombok',
                #         'description' : 'asdfasdf',
                #         'city' : 'Lombok',
                #         'departure_date' : '2024-11-03',
                #         'return_date' : '2024-11-09',
                #         'people': 3,
                #         'quota' : 6,
                #         'price' : random.randint(1, 10)
                #     },
                # ]
                
                # Filter Package Tour
                for d in data:
                    if not isinstance(d, dict):
                        continue

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


                    agent.append(d)
                    
                package = []
                seen = set()
                for d in agent:
                    d_tuple = tuple(d.items())
                    if d_tuple not in seen:
                        seen.add(d_tuple)
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
                # self.database.add_request_error(endpoint_url+'/package/returndate/'+departuredate+'/returndate'+returndate, str(e), package_service['id'], 3)
                continue

        return {
            'code': 200,
            'data': package
        }
    
    @rpc
    def get_agent_by_id(self, service_id,people,minprice,maxprice,departuredate,returndate,city):
        agent_services = self.database.get_service_by_id(service_id)
        
        agent=[]
        package=[]
        
        for agent_service in agent_services:
            if not isinstance(agent_service, dict):
                continue


            endpoint_url = agent_services['url']

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
                        'service_id' : agent_service['id'],
                        'city' : city,
                        'departure_date' : departuredate,
                        'return_date' : returndate,
                        'people': people,
                        'price' : agent_services['price'],
                        'agent_url' : agent_service['url'],
                        'agent_url_full' : agent_services['url']+'/'+city+'/'+departuredate+'/'+returndate+'/'+people
                    },
                ]
                
                # Filter Package Tour
                for d in data:
                    if not isinstance(agent_service, dict):
                        continue

                    if d['price'] < minprice: 
                        continue
                    if d['price'] > maxprice:
                        continue

                    if people != '-' and int(people) > d['quota']:
                        continue


                    agent.append(d)

                package = []
                seen = set()
                for d in agent:
                    d_tuple = tuple(d.items())
                    if d_tuple not in seen:
                        seen.add(d_tuple)
                        package.append(d)

            except requests.exceptions.RequestException as e:
                # Handle any exceptions that occur during the request
                # self.database.add_request_error(endpoint_url+'/package/returndate/'+departuredate+'/returndate'+returndate, str(e), package_service['id'], 3)
                continue

        return {
            'code': 200,
            'data': package
        }
