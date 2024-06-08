from nameko.rpc import rpc

import dependencies
import requests
class AtraksiService:

    name = 'atraksi_service'

    database = dependencies.Database()

    @rpc
    def get_all_atraksi(self,id_lokasi,attractioname,tanggal,hari,waktu):
        atraksi_services = self.database.get_service_by_type_lokasi(5,id_lokasi)
        atraksi = []

        for atraksi_service in atraksi_services:
            atraksi_service['lokasi'] = self.database.get_lokasi_by_id(atraksi_service['id_lokasi'])
            endpoint_url = atraksi_service['url']
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
                        'atraksi_id' : 1,
                        'atraksi_name' : 'Jatim Park 1',
                        'Tanggal'       : '01/01/2024',
                        'Hari'          : 'Senin',
                        'Waktu'         : '10:00 - 16:30',
                        'price'      : '130000',
                        'city'      : 'Batu, Malang',
                    },
                    {   
                        'atraksi_id' : 2,
                        'atraksi_name' : 'Jatim Park 2',
                        'Tanggal'       : '02/01/2024',
                        'Hari'          : 'Selasa',
                        'Waktu'         : '09:00 - 17:30',
                        'price'      : '125000',
                        'city'      : 'Batu, Malang',
                    },
                ]
                # check attraction availability 
                # Panggil function check availabilitynya Yull
                # Filter atraksi


            except requests.exceptions.RequestException as e:
                # Handle any exceptions that occur during the request
                # TODO add error to database
                continue


        return {
            'code': 200,
            'data': atraksi
        }