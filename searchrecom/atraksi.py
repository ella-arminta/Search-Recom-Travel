from nameko.rpc import rpc
from decimal import Decimal
import searchrecom.dependencies as dependencies
import requests
import random
from datetime import datetime

class AtraksiService:

    name = 'atraksi_service'

    database = dependencies.Database()

    def validate_date_format(self, date_str):
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    @rpc
    def get_all_atraksi(self, id_lokasi, attractioname, tanggal, minprice, maxprice, rating, sort):
        # Validate attraction name
        if attractioname != '-':
            atraksi_services = [service for service in self.database.get_service_by_type_lokasi(5, id_lokasi)
                                if attractioname.lower() in service['nama'].lower()]
            if not atraksi_services:
                return {
                    'code': 404,
                    'data': 'Input nama attraction not found'
                }
        else:
            atraksi_services = self.database.get_service_by_type(5)

        # Validate date
        error = False
        data_error = []

        if tanggal != '-' and not self.validate_date_format(tanggal):
            error = True
            data_error.append('Invalid startdate parameter. must be in format YYYY-MM-DD')
        elif tanggal != '-' and datetime.strptime(tanggal, '%Y-%m-%d') < datetime.now():
            error = True
            data_error.append('Invalid startdate parameter. must be after today')

        if error:
            return {
                'code': 400,
                'data': data_error
            }

        # Debugging log
        print("Atraksi Services Initial Data:", atraksi_services)

        # Fetch review data if rating filter is applied
        review = {}
        ratings_allowed = []
        if rating != '-' and rating != '00000' and len(rating) == 5:
            for i in range(5):
                if rating[i] == '1':
                    ratings_allowed.append(i + 1)
            endpoint_booking = self.database.get_service_by_name('booking')['url']
            try:
                response = requests.get(endpoint_booking + '/review/atraksi')
                response.raise_for_status()
                review = response.json()
            except requests.exceptions.RequestException as e:
                self.database.add_request_error(endpoint_booking + '/review/atraksi', str(e), self.database.get_service_by_name('booking')['id'], 5)
                pass

        atraksi = []

        for atraksi_service in atraksi_services:
            atraksi_service['lokasi'] = self.database.get_lokasi_by_id(atraksi_service['id_lokasi'])
            endpoint_url = atraksi_service['url']
            temp_atraksi = {}

            atraksi_start_price = None

            try:
                data = [
                    {
                        'id': 1,
                        'nama': 'Jatim Park 1',
                        'tanggal': '2024-08-08',
                        'price': 30000,
                        'city': 'Batu, Malang',
                        'popularity': 6,
                    },
                    {
                        'id': 2,
                        'nama': 'Jatim Park 2',
                        'tanggal': '2024-12-25',
                        'price': 25000,
                        'city': 'Batu, Malang',
                        'popularity': 8,
                    },
                    {
                        'id': 3,
                        'nama': 'Taman Safari Indonesia II',
                        'tanggal': '2024-09-09',
                        'price': 50000,
                        'city': 'Prigen, Pasuruan',
                        'popularity': 9,
                    },
                ]

                for d in data:

                    # cek nama atraksi
                    if attractioname != '-' and d['nama'] != attractioname:
                        continue
                    
                    # cek harga:
                    if minprice != '-' and d['price'] < int(minprice):
                        continue
                    if maxprice != '-' and d['price'] > int(maxprice):
                        continue

                    # if atraksi_start_price is None or d['price'] < atraksi_start_price:
                    #     atraksi_start_price = d['price']
                    #     continue

                    
                    atraksi.append(d)
                    # if not temp_atraksi:
                    #     temp_atraksi = {
                    #         'atraksi_id': atraksi_service['id'],
                    #         'atraksi_name': atraksi_service['nama'],
                    #         'atraksi_city': atraksi_service['lokasi']['nama_kota'],
                    #         'atraksi_price': atraksi_start_price,
                    #         'atraksi_url': atraksi_service['url'],
                    #         'atraksi_score': random.randint(1, 10),
                    #         'atraksi_popularity': random.randint(1, 10),
                    #     }
                    #     continue

                    
                
                # Sorting based on sort parameter
                if sort == 'lowestprice':
                    atraksi = sorted(atraksi, key=lambda x: x['price'])
                elif sort == 'highestprice':
                    atraksi = sorted(atraksi, key=lambda x: x['price'], reverse=True)
                elif sort == 'highestpopularity':
                    atraksi = sorted(atraksi, key=lambda x: x['popularity'], reverse=True)
                elif sort == 'reviewscore':
                    atraksi = sorted(atraksi, key=lambda x: x['atraksi_score'], reverse=True)

            except requests.exceptions.RequestException as e:
                self.database.add_request_error(endpoint_booking + '/atraksi/tanggal/' + tanggal, str(e), endpoint_url, 5)
                continue


        
        return {
            'code': 200,
            'data': atraksi
        }
