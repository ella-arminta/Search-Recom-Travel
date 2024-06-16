from nameko.rpc import rpc
from decimal import Decimal
import dependencies
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
            try:
                id_lokasi = int(id_lokasi)
                check_lokasi = self.database.get_lokasi_by_id(id_lokasi)
                if not check_lokasi:
                    error = True
                    data_error.append('Invalid id_lokasi parameter. lokasi not found')
            except ValueError:
                error = True
                data_error.append('Invalid id_lokasi parameter. must be integer')

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

        # GET ALL SERVICE THAT IS travel agent and in a location
        package_services = self.database.get_service_by_type_lokasi(3, id_lokasi)

        endpoint_booking = self.database.get_service_by_name('booking')['url']
        
        try:
            response = requests.get(endpoint_booking + '/review/atraksi')
            response.raise_for_status()
            review = response.json()
        except requests.exceptions.RequestException as e:
            self.database.add_request_error(endpoint_booking + '/review/atraksi', str(e), self.database.get_service_by_name('booking')['id'], 5)
            pass

        for package_service in package_services:
            package_service['lokasi'] = self.database.get_lokasi_by_id(package_service['id_lokasi'])
            endpoint_url = package_service['url']
            temp_package = {}

            # Get Package Tour start from (for sort by price)
            package_start_price = None
            
            # Get Package Tour
            try: 
                data = [
                    {   
                        'package_id' : 1,
                        'package_name' : 'Bromo & Semeru Mountain',
                        'detail' : 'asdfasdf',
                        'tgl_awal' : '2024-09-09',
                        'tgl_akhir' : '2024-09-14',
                        'people': 2,
                        'price' : random.randint(1, 10)
                    },
                    {   
                        'package_id' : 2,
                        'package_name' : 'Nusa Lembongan Bali',
                        'detail' : 'asdfasdf',
                        'tgl_awal' : '2024-10-10',
                        'tgl_akhir' : '2024-10-16',
                        'people': 4,
                        'price' : random.randint(1, 10)
                    },
                    {   
                        'package_id' : 3,
                        'package_name' : 'Gili Trawangan Lombok',
                        'detail' : 'asdfasdf',
                        'tgl_awal' : '2024-11-03',
                        'tgl_akhir' : '2024-11-09',
                        'people': 3,
                        'price' : random.randint(1, 10)
                    },
                ]

                # Filter Package Tour
                for d in data:
                    if minprice != '-' and d['price'] < int(minprice): 
                        continue
                    if maxprice != '-' and d['price'] > int(maxprice):
                        continue

                    # set package tour start price
                    if package_start_price is None:
                        package_start_price = d['price']
                    else: 
                        if d['price'] < package_start_price:
                            package_start_price = d['price']

                    available = True  # Simulate availability check
                    if not available:
                        continue
                    
                    if temp_package == {}:
                        temp_package = {
                            'package_id': package_service['id'],
                            'package_name': package_service['nama'],
                            'package_location': package_service['lokasi']['nama_kota'],
                            'package_url': package_service['url'],
                            'details': []
                        }
                    
                    temp_package['details'].append({
                        'tour_id': d['package_id'],
                        'tour_name': d['package_name'],
                        'tour_price': d['price'],
                        'tour_date_start': d['tgl_awal'],
                        'tour_date_end' : d['tgl_akhir'],
                        'tour_capacity': d['people'],
                        'tour_detail': d['detail']
                    })
                
                if temp_package != {}:
                    temp_package['package_start_price'] = package_start_price
                    package.append(temp_package)


                # # ADD PACKAGE TOUR and SORT BY
                # if temp_package != {}:
                #     if sort == 'lowestprice':
                #         if len(package) == 0:
                #             package.append(temp_package)
                #         else:
                #             index = 0
                #             for p in package:
                #                 if temp_package['package_start_price'] <= p['package_start_price']:
                #                     package.insert(index, temp_package)
                #                     break
                #                 elif index == len(package) - 1:
                #                     package.append(temp_package)
                #                     break
                #                 index += 1
                #     elif sort == 'highestprice':
                #         if len(package) == 0:
                #             package.append(temp_package)
                #         else:
                #             index = 0
                #             for p in package:
                #                 if temp_package['package_start_price'] >= p['package_start_price']:
                #                     package.insert(index, temp_package)
                #                     break
                #                 elif index == len(package) - 1:
                #                     package.append(temp_package)
                #                     break
                #                 index += 1
                    
                #     else:
                #         package.append(temp_package)

            except requests.exceptions.RequestException as e:
                # Handle any exceptions that occur during the request
                if endpoint_booking:
                    self.database.add_request_error(endpoint_booking+'/package/startdate/'+startdate+'/enddate'+enddate, str(e), endpoint_url, 3)
                continue

        # SORT
        if sort == 'lowestprice':
            package = sorted(package, key=lambda x: x['package_start_price'])
        elif sort == 'highestprice':
            package = sorted(package, key=lambda x: x['package_start_price'], reverse=True)

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
