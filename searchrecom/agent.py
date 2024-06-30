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
    def get_all_agent(self,name,departure_date, return_date, number_of_people,minprice,maxprice, sort):
        package_services = self.database.get_service_by_type(3)
        packages = []

        for package_service in package_services:
            endpoint_url = package_service['url']
            try:
                response = requests.get(endpoint_url)
                response.raise_for_status()
                data = response.json()

                print("Data received from endpoint:")
                print(data)

                if not isinstance(data, list):
                    print(f"Unexpected data type: {type(data)}, content: {data}")
                    continue

                filtered_data = []

                for d in data:
                    if not isinstance(d, dict):
                        print(f"Unexpected item type in data: {type(d)}, content: {d}")
                        continue

                    print(f"Processing item: {d}")

                    if name != '-' and d.get('name') != name:
                        print(f"Filtered out by name: {d.get('name')}")
                        pass

                    if number_of_people != '-':
                        print(f"Checking number_of_people: {d.get('number_of_people')} vs {number_of_people}")
                        if d.get('number_of_people', -1) < int(number_of_people):
                            print(f"Filtered out by number of people: {d.get('number_of_people')}")
                            pass

                    if departure_date != '-' and d.get('departure_date') != departure_date:
                        print(f"Filtered out by departure_date: {d.get('departure_date')} != {departure_date}")
                        pass

                    if return_date != '-' and d.get('return_date') != return_date:
                        print(f"Filtered out by return_date: {d.get('return_date')} != {return_date}")
                        pass

                    filtered_data.append(d)

                print("Filtered data:")
                print(filtered_data)
                packages.extend(filtered_data)

            except requests.exceptions.RequestException as e:
                print(f"Request failed for {endpoint_url}: {e}")
                continue

        print("Final packages before sorting:")
        print(packages)

        if sort != '-':
            if sort == 'lowestprice':
                packages.sort(key=lambda x: x['price'])
            elif sort == 'highestprice':
                packages.sort(key=lambda x: x['price'], reverse=True)
            elif sort == 'departure_date':
                packages.sort(key=lambda x: x['departure_date'])
            elif sort == 'city':
                packages.sort(key=lambda x: x['name'])
            elif sort == 'quota':
                packages.sort(key=lambda x: x['quota'])

        print("Final packages after sorting:")
        print(packages)
        return {
            'code': 200,
            'data': packages
        }
        
    @rpc
    def get_agent_by_id(self, service_id,packagename,departuredate,returndate,people,price,images):
        agents_services = self.database.get_service_by_id(service_id)
        
        agents=[]
        unique_agents = []
        
        for agent_service in agents_services:
            endpoint_url = agents_services['url']
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
                        'service_id':agents_services['id'],
                        'name':packagename,
                        'departure_date':departuredate,
                        'return_date':returndate,
                        'number_of_people':people,
                        'price' : price,
                        'images' : images,
                        'agent_url':agents_services['url'],
                        'agent_url_full':agents_services['url']+'/'+packagename+'/'+departuredate+'/'+returndate+'/'+people
                    },
                ]
                
                for agent in data:
                    if packagename != '-' and agent['name'] != packagename:
                        continue
                    if departuredate != '-' and agent['departure_date'] != departuredate:
                        continue
                    if returndate != '-' and agent['return_date'] != returndate:
                        continue
                    if people != '-' and agent['number_of_people'] != people:
                        continue
                    
                    agents.append(agent)

                unique_agents = []
                seen = set()
                for agent in agents:
                    agent_tuple = tuple(agent.items())
                    if agent_tuple not in seen:
                        seen.add(agent_tuple)
                        unique_agents.append(agent)
            except requests.exceptions.RequestException as e:
                    # Handle any exceptions that occur during the request
                    # self.database.add_request_error(endpoint_url+'/package/returndate/'+departuredate+'/returndate'+returndate, str(e), package_service['id'], 3)
                    pass

        return {
                    'code': 200,
                    'data': unique_agents
                }