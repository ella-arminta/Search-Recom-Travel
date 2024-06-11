from nameko.rpc import rpc
from decimal import Decimal
import dependencies
import requests
import random

class AtraksiService:

    name = 'atraksi_service'

    database = dependencies.Database()

    @rpc
    def get_all_atraksi(self,id_lokasi,attractioname,tanggal,minprice,maxprice,rating,sort):
         # get all service that is attraction and in a location
        if id_lokasi != '-':
            atraksi_services = self.database.get_service_by_type_lokasi(5,id_lokasi)
        
        else:
            atraksi_services = self.database.get_service_by_type(5)

        # get attraction ratings and popularity from review (for sort by reviewscore/countBooked and popularity)
        review = {}
        ratings_allowed = []
        if rating != '-' and rating != '00000' and len(rating) == 5:
            ratings_allowed = []
            for i in range(5):
                if rating[i] == '1':
                    ratings_allowed.append(i + 1)
            endpoint_booking = self.database.get_service_by_name('booking')['url']
            try: 
                # TODO testing review service
                response = requests.get(endpoint_booking + '/review/atraksi')
                response.raise_for_status()
                review = response.json()
            except requests.exceptions.RequestException as e:
                # Handle any exceptions that occur during the request
                self.database.add_request_error(endpoint_booking + '/review/atraksi', str(e), self.database.get_service_by_name('booking')['id'] , 5)

                pass
                # return {
                #     'code': 500,
                #     'data': 'Error fetching rating'
                # }

        atraksi = []


        for atraksi_service in atraksi_services:
            atraksi_service['lokasi'] = self.database.get_lokasi_by_id(atraksi_service['id_lokasi'])
            endpoint_url = atraksi_service['url']
            temp_atraksi = {}

            # harga awal atraksi / start price:
            atraksi_start_price = None

            # check atraksi ratings
            # if ratings_allowed: 
            #     if atraksi_service['nama'] not in rating_data:
            #         continue
            #     if rating_data[atraksi_service['nama']] not in ratings_allowed:
            #         continue
            try: 
                # /atraksi
                response = requests.get(endpoint_url)
                response.raise_for_status()
                data = response.json()
                # data yang diterima bentuknya : DUMMY
                # PERTANYAAN apakah atraksi masih menyimpan atraksi detail
                # yang ngecek apakah atraksi avail atau gk itu dari function atraksi, atau function search&Recom
                data = [
                    {   
                        'id' : 1,
                        'nama' : 'Jatim Park 1',
                        'tanggal' : '01/01/2024',
                        #'waktu'   : '10:00 - 16:30',
                        'price'   : '130000',
                        'city'    : 'Batu, Malang',
                    },
                    {   
                        'id' : 2,
                        'nama' : 'Jatim Park 2',
                        'tanggal'  : '02/01/2024',
                        #'waktu'    : '09:00 - 17:30',
                        'price'    : '125000',
                        'city'     : 'Batu, Malang',
                    },
                    {   
                        'id' : 3,
                        'nama' : 'Taman Safari Indonesia II',
                        'tanggal'  : '03/02/2024',
                        #'waktu'    : '10:00 - 18:00',
                        'price'    : '150000',
                        'city'     : 'Prigen, Pasuruan',
                    },
                ]
                
                # Filter atraksi:
                for d in data:
                    if minprice != '-' :
                        if d['price'] < minprice:
                            continue

                    if maxprice != '-' :
                        if d['price'] > maxprice:
                            continue

                    # set atraksi start price:
                    if atraksi_start_price is None :
                        atraksi_start_price = d['price']
                    else:
                        if d['price'] < atraksi_start_price:
                            atraksi_start_price = d['price']

                    # check atraksi Availability 
                    # Panggil function check availabilitynya Yull
                    # input : atraksi_id, tanggal
                    # output : boolean

                    available = True
                    if not available:
                        continue

                    if temp_atraksi == {}:
                        temp_atraksi ={
                            'atraksi_id' : atraksi_service['id'],
                            'atraksi_name' : atraksi_service['nama'],
                            'atraksi_city' : atraksi_service['lokasi']['nama_kota'],
                            'atraksi_price' : atraksi_service['price'],
                            'atraksi_tanggal' : atraksi_service['tanggal'],
                            'atraksi_url' : atraksi_service['url'],
                            # 'atraksi_score' : review[atraksi_service['nama']]['rating'] if atraksi_service['nama'] in review else 0,
                            'atraksi_score' : random.randint(1, 10),
                            # 'atraksi_popularity' : review[atraksi_service['nama']]['countBooked'] if atraksi_service['nama'] in review else 0,
                            'atraksi_popularity' : random.randint(1, 10)
                        }
                    
                    temp_atraksi.setdefault('details',[]).append({
                        'atraksi_id' : d['id'],
                        'atraksi_name' : d['nama'],
                        'atraksi_tanggal' : d['tanggal'],
                        'atraksi_price' : d['price'], # ini perlu dimasukkan append atau di atraksi_service aja?
                        'atraksi_city' : d['city']
                        #'atraksi_hour' : d['waktu']
                    })

                if temp_atraksi != {} :
                    temp_atraksi['atraksi_start_price'] = atraksi_start_price

                # ADD ATRAKSI and SORT BY ATRAKSI:
                if temp_atraksi != {}:
                    if sort == 'lowestprice':
                        if len(atraksi) == 0:
                            atraksi.append(temp_atraksi)
                            continue
                        else:
                            index = 0
                            for a in atraksi:
                                if atraksi_start_price <= a['atraksi_start_price'] :
                                    atraksi.insert(index, temp_atraksi)
                                    break
                                elif index == len(atraksi) - 1:
                                    atraksi.append(temp_atraksi)
                                    break
                                index += 1
                    elif sort == 'highestprice':
                        if len(atraksi) == 0:
                            atraksi.append(temp_atraksi)
                            continue
                        else:
                            index = 0
                            for a in atraksi:
                                if atraksi_start_price >= a['atraksi_start_price'] :
                                    atraksi.insert(index, temp_atraksi)
                                    break
                                elif index == len(atraksi) - 1:
                                    atraksi.append(temp_atraksi)
                                    break
                                index += 1
                    elif sort == 'highestpopularity':
                        if len(atraksi) == 0:
                            atraksi.append(temp_atraksi)
                            continue
                        else:
                            index = 0
                            for a in atraksi:
                                if temp_atraksi['atraksi_popularity'] >= a['atraksi_popularity'] :
                                    atraksi.insert(index, temp_atraksi)
                                    break
                                elif index == len(atraksi) - 1:
                                    atraksi.append(temp_atraksi)
                                    break
                                index += 1
                    elif sort == 'reviewscore':
                        if len(atraksi) == 0:
                            atraksi.append(temp_atraksi)
                            continue
                        else:
                            index = 0
                            for a in atraksi:
                                if temp_atraksi['atraksi_score'] >= a['atraksi_score'] :
                                    atraksi.insert(index, temp_atraksi)
                                    break
                                elif index == len(atraksi) - 1:
                                    atraksi.append(temp_atraksi)
                                    break
                                index += 1
                    else:
                        atraksi.append(temp_atraksi)



            except requests.exceptions.RequestException as e:
                # Handle any exceptions that occur during the request
                self.database.add_request_error(endpoint_booking+'/atraksi/tanggal/'+tanggal, str(e), endpoint_url, 5)

                continue


        return {
            'code': 200,
            'data': atraksi
        }