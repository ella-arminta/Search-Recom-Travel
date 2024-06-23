from nameko.rpc import rpc
from decimal import Decimal
import searchrecom.dependencies as dependencies
import requests
import random
from datetime import datetime

class CarRentalService:

    name = 'carrental_service'

    database = dependencies.Database()

    @rpc
    def get_all_carrental(self, driver, id_lokasi, startdate, enddate, capacity, cartype, provider,transmission, sort):
        # VERIFY INPUT
        data_error = []
        error = False
        # driver
        if driver not in [0, 1]:
            error = True
            data_error.append('Invalid driver parameter. must be 0 or 1')
        # lokasi
        if id_lokasi != '-': 
            try :
                id_lokasi = int(id_lokasi)
                check_lokasi = self.database.get_lokasi_by_id(id_lokasi)
                if not check_lokasi:
                    error = True
                    data_error.append('Invalid id_lokasi parameter. lokasi not found')
            except:
                error = True
                data_error.append('Invalid id_lokasi parameter. must be integer')
        # date
        def validate_date_format(date_str):
            try:
                datetime.strptime(date_str, '%Y-%m-%d')
                return True
            except ValueError:
                return False
        # startdate & enddate
        if validate_date_format(startdate) == False:
            error = True
            data_error.append('Invalid startdate parameter. must be in format YYYY-MM-DD')
        if validate_date_format(enddate) == False:
            error = True
            data_error.append('Invalid enddate parameter. must be in format YYYY-MM-DD')
        if validate_date_format(startdate) and datetime.strptime(startdate, '%Y-%m-%d') < datetime.now():
            error = True
            data_error.append('Invalid startdate parameter. must be after today')
        if validate_date_format(startdate) and validate_date_format(enddate) and datetime.strptime(startdate, '%Y-%m-%d') > datetime.strptime(enddate, '%Y-%m-%d'):
            error = True
            data_error.append('Invalid startdate parameter. must be before enddate')
        # capacity
        if capacity != '-':
            temp_cap = []
            capacities = capacity.split('&')
            for cap in capacities:
                if cap not in ['4','56','7']:
                    error = True
                    data_error.append('Invalid capacity parameter. must be `4`, `56`, or `7`, meaning <= 4, 5 - 6, and 6 >. example : 4&56 for doble param')
                else: 
                    if cap == '4':
                        temp_cap += [1, 2, 3, 4]
                    elif cap == '56':
                        temp_cap += [5, 6]
                    else:
                        temp_cap += [7]
            capacity = temp_cap
        # transimission
        if transmission != '-':
            transmission = transmission.split('&')
            for i in range(len(transmission)):
                transmission[i] = transmission[i].lower()
                if transmission[i] not in ['automatic', 'manual']:
                    error = True
                    data_error.append('Invalid transmission parameter. must be `automatic` or `manual`')
        # cartype
        if cartype != '-':
            cartype = cartype.split('&')
            for i in range(len(cartype)):
                cartype[i] = cartype[i].lower()
                cartype[i] = cartype[i].replace('_',' ')
        #provider
        if provider != '-':
            provider = provider.split('&')
            for i in range(len(provider)):
                provider[i] = provider[i].lower()
                provider[i] = provider[i].replace('_',' ')
        if error:
            return {
                'code': 400,
                'data': data_error
            }
        
        
        # GET ALL SERVICE THAT IS carrental and in a location
        carrental_services = self.database.get_service_by_type_lokasi(4, id_lokasi)
        carrentals = {
            # example
            # 'daihatsu_ayla_automatic' : {
            #     'car_brand': 'Daihatsu',
            #     'car_name' : 'Ayla',
            #     'car_seats' : 4,
            #     'car_luggages': 2,
            #     'count_providers' : 0,
            #     'withdriver': driver,
            #     'start_price' : 0,
            #     'providers': [
            #         'provider_name': 'Astra Rent Car',
            #         'price_per_day': 300000,
            #         'total_price': 0,
            #         'review_score': 0,
            #     ]
            # },
            # 'toyota_agya_manual': {
            #     ...
            # }
        }

        # GET REVIEWS and PROVIDER RATING
        review = {}
        endpoint_booking = self.database.get_service_by_name('booking')['url']
        try: 
            # TODO testing review service
            response = requests.get(endpoint_booking + '/review/carrental')
            response.raise_for_status()
            review = response.json()
        except requests.exceptions.RequestException as e:
            self.database.add_request_error(endpoint_booking + '/review/carrental', str(e), self.database.get_service_by_name('booking')['id'], 7)
            pass
            # return {
            #     'code': 500,
            #     'data': 'Error fetching rating'
            # }

        
        for cr in carrental_services:
            cr['lokasi'] = self.database.get_lokasi_by_id(cr['id_lokasi'])
            endpoint_url = cr['url']
            # FILTER provider
            if provider != '-' and cr['nama'].lower() not in provider:
                continue
            try: 
                # response = requests.get(endpoint_url + '/available_cars/' + startdate + '/'+ enddate)
                # response.raise_for_status()
                # cars = response.json()
                # id cars
                cars = [4,5,6,7]
                cars_detail = []

                for car_id in cars: 
                    try: 
                        # response = requests.get(endpoint_url + '/car/' + car_id )
                        # response.raise_for_status()
                        # car = response.json()
                        car = {
                            'car_id':car_id,
                            'car_brand': random.choice(['toyota','daihatsu','suzuki','bmw']),
                            'car_name' : random.choice(['ayla','agya','xenia','innova','fortuner','x5']),
                            'car_type': random.choice(['sedan','mpv','suv']),
                            'car_transmission': random.choice(['automatic','manual']),
                            'car_year': 2019,
                            'car_seats': random.randint(1, 10),
                            'car_luggages': 2,
                            'car_price':random.randint(100000, 1000000),
                            'driver_id':2
                        }
                        # FILTER
                        if capacity != '-':
                            if car['car_seats'] not in capacity:
                                if 7 in capacity:
                                    if car['car_seats'] >= 7:
                                        pass 
                                    else: 
                                        continue
                                else:
                                    continue
                        if transmission != '-':
                            if car['car_transmission'].lower() not in transmission:
                                continue
                        if cartype != '-' and car['car_type'].lower() not in cartype:
                            continue

                        # APPEND
                        num_days = (datetime.strptime(enddate, "%Y-%m-%d") - datetime.strptime(startdate, "%Y-%m-%d")).days
                        car_key = car['car_brand'].lower() + '_' + car['car_name'].lower() + '_' + car['car_transmission'].lower()
                        if car_key not in carrentals:
                            carrentals[car_key] = {
                                'car_key' : car_key,
                                'car_brand': car['car_brand'],
                                'car_name' : car['car_name'],
                                'car_seats' : car['car_seats'],
                                'car_type' : car['car_type'],
                                'car_luggages': car['car_luggages'],
                                'car_transmission' : car['car_transmission'],
                                'count_providers' : 1,
                                'withdriver': driver,
                                'start_price' : car['car_price'],
                                'providers': [
                                    {
                                        'provider_name': cr['nama'],
                                        'provider_id': cr['id'],
                                        'lokasi': cr['lokasi'],
                                        'car_id': car['car_id'],
                                        'provider_url': cr['url'],
                                        'price_per_day': car['car_price'],
                                        'total_price': car['car_price'] * num_days,
                                        'review_score': review[cr['nama']] if cr['nama'] in review else 0,
                                    }
                                ]
                            }
                        else:
                            if car['car_price'] < carrentals[car_key]['start_price']:
                                carrentals[car_key]['start_price'] = car['car_price']
                            carrentals[car_key]['count_providers'] += 1
                            carrentals[car_key]['providers'].append({
                                'provider_name': cr['nama'],
                                'provider_id': cr['id'],
                                'lokasi': cr['lokasi'],
                                'car_id': car['car_id'],
                                'provider_url': cr['url'],
                                'price_per_day': car['car_price'],
                                'total_price': car['car_price'] * num_days,
                                'review_score': review[cr['nama']] if cr['nama'] in review else 0,
                            })
                    except requests.exceptions.RequestException as e:
                        self.database.add_request_error(endpoint_url +'/car/<id>', str(e), cr['id'] , 4)
                        continue
                        # Handle any exceptions that occur during the request
                        pass
                        # return {
                        #     'code': 500,
                        #     'data': 'Error fetching carrental'
                        # }

            except requests.exceptions.RequestException as e:
                # Handle any exceptions that occur during the request
                self.database.add_request_error(endpoint_url +'/available_cars', str(e), cr['id'] , 4)
                continue
                pass
                # return {
                #     'code': 500,
                #     'data': 'Error fetching carrental'
                # }
                
        # SORT
        if sort == 'lowestprice':
            carrentals = sorted(carrentals.values(), key=lambda x: x['start_price'])
        elif sort == 'highestprice':
            carrentals = sorted(carrentals.values(), key=lambda x: x['start_price'], reverse=True)
        elif sort == 'lowestcapacity':
            carrentals = sorted(carrentals.values(), key=lambda x: x['car_seats'])
        elif sort == 'highestcapacity':
            carrentals = sorted(carrentals.values(), key=lambda x: x['car_seats'], reverse=True)

        return {
            'code': 200,
            'data': carrentals
        }

    @rpc
    def get_all_cartype(self, id_lokasi):
        carrental_services = self.database.get_service_by_type_lokasi(4, id_lokasi)
        cartype = {}
        for cr in carrental_services:
            endpoint_url = cr['url']
            try:
                response = requests.get(endpoint_url + '/car')
                response.raise_for_status()
                cars = response.json()
                for c in cars:
                    if c['car_type'] not in cartype:
                        cartype[c['car_type']] = [cr['id']]
                    else:
                        cartype[c['car_type']].append(cr['id'])
            except requests.exceptions.RequestException as e:
                self.database.add_request_error(endpoint_url + '/car', str(e), cr['id'] , 4)
                pass

        return {
            'code':200,
            'data': cartype
        }
    
    @rpc
    def get_all_provider(self, id_lokasi):
        carrental_services = self.database.get_service_by_type_lokasi(4, id_lokasi)
        
        # get provider rating
        review = {}
        endpoint_booking = self.database.get_service_by_name('booking')['url']
        try: 
            # TODO testing review service
            response = requests.get(endpoint_booking + '/review/carrental')
            response.raise_for_status()
            review = response.json()
        except requests.exceptions.RequestException as e:
            self.database.add_request_error(endpoint_booking + '/review/carrental', str(e), self.database.get_service_by_name('booking')['id'] , 4)
            pass
            # return {
            #     'code': 500,
            #     'data': 'Error fetching rating'
            # }

        providers = []
        for cr in carrental_services:
            providers.append({
                'provider_id' : cr['id'],
                'provider_name' : cr['nama'],
                'rating' : review[cr['nama']] if cr['nama'] in review else 0,
            })

        return {
            'code':200,
            'data': providers
        }