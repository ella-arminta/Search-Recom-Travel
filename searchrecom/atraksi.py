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

        atraksi = []

        for atraksi_service in atraksi_services:
            atraksi_service['lokasi'] = self.database.get_lokasi_by_id(atraksi_service['id_lokasi'])
            endpoint_url = atraksi_service['url']
            temp_atraksi = []

            # TODO uncomment
            # get atraksi detail
            atraksi_detail = {}
            # Dummy data for testing
            atraksi_detail = {
                'id': 1,
                'image': 'https://hotel-images-soa.s3.amazonaws.com/merlynn_park_hotel.jpg'
            }
            #     # cth atraksi detail
            #     # {
            #     # "service_id" : 5,
            #     # "id": 1,
            #     # "title": "Dufan",
            #     # "slug": "https://hotel-images-soa.s3.amazonaws.com/merlynn_park_hotel.jpg",
            #     # "deskripsi": "Dufan",
            #     # "info_penting": "<ul>\n                                <li>Tidak termasuk tiket masuk Pintu Gerbang Utama Ancol. Beli tiket Pintu Gerbang Utama Ancol di sini untuk pengalaman liburan yang tak terlupakan.</li>\n                                <li>Pengunjung dilarang membawa makanan dan minuman ke dalam area Dufan.</li>\n                                <li>Loket Dufan dan Pintu Gerbang Dunia Fantasi ditutup 1 jam lebih awal dari jam operasional yang berlaku.</li>\n                            </ul>",
            #     # "highlight": "<ul>\n                                <li>Dufan adalah wahana yang menghadirkan tempat bermain asyik yang terbagi menjadi empat kategori, yakni Children Rides, Family Ride, Water Ride, dan Thrill Ride.</li>\n                                <li>Bawa anak-anakmu ke wahana Dufan khusus anak, seperti Ontang-Anting yang riuh dan Istana Boneka yang penuh pesona.</li>\n                                <li>Sekaranglah waktunya untuk membuat kenangan berharga bersama keluarga dan teman-teman. Cek harga tiket Dufan 2024 di bawah, pilih tiketnya, dan nikmati petualangan yang seru!</li>\n                                <li>Cocok untuk: Keluarga Asyik, Bersama Pasangan, dan Geng Asyik.</li>\n                            </ul>",
            #     # "alamat": "Jl. Lodan Timur No.7, Ancol, Kec. Pademangan, Jkt Utara, Daerah Khusus Ibukota Jakarta 14430",
            #     # "negara": "Indonesia",
            #     # "kota": "Jakarta",
            #     # "lowest_price": "100000"
            #     # }
            # try:
            #     response = requests.get(endpoint_url)
            #     response.raise_for_status()
            #     atraksi_detail = response.json()
            # except requests.exceptions.RequestException as e:
            #     self.database.add_request_error(endpoint_url, str(e), atraksi_service['id'], 5)
            #     continue

            atraksi_start_price = None

            try:
                # Dummy data for testing
                data = [
                    {
                        'service_id':atraksi_service['id'],
                        'id': 1,
                        'nama': 'Jatim Park 1',
                        'tanggal': '2024-08-08',
                        'price': 30000,
                        'city': 'Batu, Malang',
                        'popularity': 6,
                    },
                    {
                        'service_id':atraksi_service['id'],
                        'id': 2,
                        'nama': 'Jatim Park 2',
                        'tanggal': '2024-12-25',
                        'price': 25000,
                        'city': 'Batu, Malang',
                        'popularity': 8,
                    },
                    {
                        'service_id':atraksi_service['id'],
                        'id': 3,
                        'nama': 'Taman Safari Indonesia II',
                        'tanggal': '2024-09-09',
                        'price': 50000,
                        'city': 'Prigen, Pasuruan',
                        'popularity': 9,
                    },
                ]

                for d in data:
                    # Check nama atraksi
                    if attractioname != '-' and d['nama'] != attractioname:
                        continue
                    
                    # Check harga
                    if minprice != '-' and d['price'] < int(minprice):
                        continue
                    if maxprice != '-' and d['price'] > int(maxprice):
                        continue

                    if atraksi_start_price is None:
                        atraksi_start_price = d['price']
                    else: 
                        if d['price'] < atraksi_start_price:
                            atraksi_start_price = d['price']

                    atraksi.append(d)
                
                # Sorting based on sort parameter
                if sort == 'lowestprice':
                    atraksi = sorted(atraksi, key=lambda x: x['price'])
                elif sort == 'highestprice':
                    atraksi = sorted(atraksi, key=lambda x: x['price'], reverse=True)
                elif sort == 'highestpopularity':
                    atraksi = sorted(atraksi, key=lambda x: x['popularity'], reverse=True)
                # elif sort == 'reviewscore':
                #     atraksi = sorted(atraksi, key=lambda x: x['atraksi_score'], reverse=True)

            except requests.exceptions.RequestException as e:
                self.database.add_request_error(endpoint_booking + '/atraksi/tanggal/' + tanggal, str(e), endpoint_url, 5)
                continue


        
        return {
            'code': 200,
            'data': atraksi
        }

    @rpc
    def get_atraksi_by_id(self, service_id, attractioname,attractiondate, minprice, maxprice):
        # Validate attraction name
        if attractioname != '-':
            atraksi_services = [service for service in self.database.get_service_by_type_lokasi(5, service_id)
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

        if attractiondate != '-' and not self.validate_date_format(attractiondate):
            error = True
            data_error.append('Invalid startdate parameter. must be in format YYYY-MM-DD')
        elif attractiondate != '-' and datetime.strptime(attractiondate, '%Y-%m-%d') < datetime.now():
            error = True
            data_error.append('Invalid startdate parameter. must be after today')

        if error:
            return {
                'code': 400,
                'data': data_error
            }

        atraksi = []

        for atraksi_service in atraksi_services:
            atraksi_service['lokasi'] = self.database.get_lokasi_by_id(atraksi_service['id_lokasi'])
            endpoint_url = atraksi_service['url']
            temp_atraksi = []

            # TODO uncomment
            # get atraksi detail
            atraksi_detail = {}
            # Dummy data for testing
            atraksi_detail = {
                'id': 1,
                'image': 'https://hotel-images-soa.s3.amazonaws.com/merlynn_park_hotel.jpg'
            }
            #     # cth atraksi detail
            #     # {
            #     # "service_id" : 5,
            #     # "id": 1,
            #     # "title": "Dufan",
            #     # "slug": "https://hotel-images-soa.s3.amazonaws.com/merlynn_park_hotel.jpg",
            #     # "deskripsi": "Dufan",
            #     # "info_penting": "<ul>\n                                <li>Tidak termasuk tiket masuk Pintu Gerbang Utama Ancol. Beli tiket Pintu Gerbang Utama Ancol di sini untuk pengalaman liburan yang tak terlupakan.</li>\n                                <li>Pengunjung dilarang membawa makanan dan minuman ke dalam area Dufan.</li>\n                                <li>Loket Dufan dan Pintu Gerbang Dunia Fantasi ditutup 1 jam lebih awal dari jam operasional yang berlaku.</li>\n                            </ul>",
            #     # "highlight": "<ul>\n                                <li>Dufan adalah wahana yang menghadirkan tempat bermain asyik yang terbagi menjadi empat kategori, yakni Children Rides, Family Ride, Water Ride, dan Thrill Ride.</li>\n                                <li>Bawa anak-anakmu ke wahana Dufan khusus anak, seperti Ontang-Anting yang riuh dan Istana Boneka yang penuh pesona.</li>\n                                <li>Sekaranglah waktunya untuk membuat kenangan berharga bersama keluarga dan teman-teman. Cek harga tiket Dufan 2024 di bawah, pilih tiketnya, dan nikmati petualangan yang seru!</li>\n                                <li>Cocok untuk: Keluarga Asyik, Bersama Pasangan, dan Geng Asyik.</li>\n                            </ul>",
            #     # "alamat": "Jl. Lodan Timur No.7, Ancol, Kec. Pademangan, Jkt Utara, Daerah Khusus Ibukota Jakarta 14430",
            #     # "negara": "Indonesia",
            #     # "kota": "Jakarta",
            #     # "lowest_price": "100000"
            #     # }
            # try:
            #     response = requests.get(endpoint_url)
            #     response.raise_for_status()
            #     atraksi_detail = response.json()
            # except requests.exceptions.RequestException as e:
            #     self.database.add_request_error(endpoint_url, str(e), atraksi_service['id'], 5)
            #     continue


        # Get atraksi start price (for sort by price)
        atraksi_start_price = None
        try:
            data = [
                {
                    'service_id': 5,
                    'id': 1,
                    'nama': 'Jatim Park 1',
                    'tanggal': '2024-08-08',
                    'price': 30000,
                    'city': 'Batu, Malang',
                    'popularity': 6,
                },
                {
                    'service_id': 5,
                    'id': 2,
                    'nama': 'Jatim Park 2',
                    'tanggal': '2024-12-25',
                    'price': 25000,
                    'city': 'Batu, Malang',
                    'popularity': 8,
                },
                {
                    'service_id': 5,
                    'id': 3,
                    'nama': 'Taman Safari Indonesia II',
                    'tanggal': '2024-09-09',
                    'price': 50000,
                    'city': 'Prigen, Pasuruan',
                    'popularity': 9,
                },
            ]

            for d in data:
                # Check nama atraksi
                if attractioname != '-' and d['nama'] != attractioname:
                    continue
                
                # Check harga
                if minprice != '-' and d['price'] < int(minprice):
                    continue
                if maxprice != '-' and d['price'] > int(maxprice):
                    continue

                        if atraksi_start_price is None:
                            atraksi_start_price = d['price']
                        else: 
                            if d['price'] < atraksi_start_price:
                                atraksi_start_price = d['price']

                        atraksi.append(d)

            except requests.exceptions.RequestException as e:
                # self.database.add_request_error(endpoint_booking + '/atraksi/' + attractioname, str(e), endpoint_url, 5)
                pass
        
        return {
            'code': 200,
            'data': atraksi
        }