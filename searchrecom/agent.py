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
    def get_all_agent(self, id_lokasi, startdate, enddate, people, minprice, maxprice, sort):
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

        if startdate != '-' and not validate_date_format(startdate):
            error = True
            data_error.append('Invalid startdate parameter. must be in format YYYY-MM-DD')
            
        elif enddate != '-' and not validate_date_format(enddate):
            error = True
            data_error.append('Invalid enddate parameter. must be in format YYYY-MM-DD')

        elif startdate != '-' and enddate != '-':
            # Pengecekan tanggal berlaku
            now = datetime.now()
            if datetime.strptime(startdate, '%Y-%m-%d') < now:
                error = True
                data_error.append('Invalid startdate parameter. must be after today')
            elif datetime.strptime(startdate, '%Y-%m-%d') > datetime.strptime(enddate, '%Y-%m-%d'):
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

            # Get Package Tour
            try: 
                data = [
                    {   
                        'package_id' : 1,
                        'package_name' : 'Bromo & Semeru Mountain',
                        'detail' : 'asdfasdf',
                        'city' : 'Probolinggo',
                        'tgl_awal' : '2024-09-09',
                        'tgl_akhir' : '2024-09-14',
                        'people': 2,
                        'quota' : 10,
                        'price' : random.randint(1, 10)
                    },
                    {   
                        'package_id' : 2,
                        'package_name' : 'Nusa Lembongan Bali',
                        'detail' : 'asdfasdf',
                        'city' : 'Nusa Dua, Bali',
                        'tgl_awal' : '2024-10-10',
                        'tgl_akhir' : '2024-10-16',
                        'people': 4,
                        'quota' : 5,
                        'price' : random.randint(1, 10)
                    },
                    {   
                        'package_id' : 3,
                        'package_name' : 'Gili Trawangan Lombok',
                        'detail' : 'asdfasdf',
                        'city' : 'Lombok',
                        'tgl_awal' : '2024-11-03',
                        'tgl_akhir' : '2024-11-09',
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
                elif sort == 'startdate' :
                    package = sorted(package,  key=lambda x: x['tgl_awal'])

            except requests.exceptions.RequestException as e:
                # Handle any exceptions that occur during the request
                self.database.add_request_error(endpoint_url+'/package/startdate/'+startdate+'/enddate'+enddate, str(e), package_service['id'], 3)
                continue

        return {
            'code': 200,
            'data': package
        }
    
    def get_all_agent_by_location(self, id_lokasi):
        package_services = self.database.get_service_by_type_lokasi(3, id_lokasi)
        tourlist = {}
        for paket in package_services:
            endpoint_url = paket['url']
            try:
                response = requests.get(endpoint_url + '/package')
                response.raise_for_status()
                tour = response.json()
                for t in tour:
                    if t['package_name'] not in tourlist:
                        tourlist[t['package_id']] = [paket['id']]
                    else:
                        tourlist[t['package_id']].append(paket['id'])
            except requests.exceptions.RequestException as e:
                self.database.add_request_error(endpoint_url + '/package', str(e), paket['id'] , 4)
                pass

        return {
            'code':200,
            'data': tourlist
        }
