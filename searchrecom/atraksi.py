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
    def get_all_atraksi(self, title, alamat, kota_name, lowest_price, sort):
        atraksi_services = self.database.get_service_by_type(5)
        atraksi = []

        for atraksi_service in atraksi_services:
            endpoint_url = atraksi_service['url']

            try:
                response = requests.get(endpoint_url)
                response.raise_for_status()
                data = response.json()

                # # Debug print untuk melihat data yang diterima
                # print("Data received from API:", data)

                # Jika data adalah dictionary, kita mengambil list atraksi dari key yang relevan
                if isinstance(data, dict):
                    data = [data]

                for d in data:
                    # Check nama atraksi
                    if title != '-' and d['title'] != title:
                        continue
                    
                    # Check harga
                    if lowest_price != '-' and d['lowest_price'] < int(lowest_price):
                        continue

                    if alamat != '-' and d['alamat'] != alamat:
                        continue

                    if kota_name != '-' and d['kota_name'] != kota_name:
                        continue

                    atraksi.append(d)
                
                # Sorting based on sort parameter
                if sort == 'lowestprice':
                    atraksi = sorted(atraksi, key=lambda x: x['lowest_price'])
                elif sort == 'highestprice':
                    atraksi = sorted(atraksi, key=lambda x: x['lowest_price'], reverse=True)
                elif sort == 'kota_name':
                    atraksi = sorted(atraksi, key=lambda x: x['kota_name'])

            except requests.exceptions.RequestException as e:
                # self.database.add_request_error(endpoint_booking + '/atraksi/tanggal/' + tanggal, str(e), endpoint_url, 5)
                continue

        return {
            'code': 200,
            'data': atraksi
        }

    @rpc
    def get_all_paket(self, title,type_name,deskripsi,fasilitas):
        paket_services = self.database.get_service_by_type(5)
        paket = []

        for paket_service in paket_services:
            endpoint_url = paket_service['url']

            try:
                response = requests.get(endpoint_url)
                response.raise_for_status()
                data = response.json()

                # # Debug print untuk melihat data yang diterima
                # print("Data received from API:", data)

                # Jika data adalah dictionary, kita mengambil list paket dari key yang relevan
                if isinstance(data, dict):
                    data = [data]

                for d in data:
                    # Check nama paket
                    if title != '-' and d['title'] != title:
                        continue
                    
                    if type_name != '-' and d['type_name'] != type_name:
                        continue

                    if deskripsi != '-' and d['deskripsi'] != deskripsi:
                        continue
                    if fasilitas != '-' and d['fasilitas'] != fasilitas:
                        continue

                    paket.append(d)
                
            except requests.exceptions.RequestException as e:
                # self.database.add_request_error(endpoint_booking + '/atraksi/tanggal/' + tanggal, str(e), endpoint_url, 5)
                continue

        return {
            'code': 200,
            'data': paket
        }

    