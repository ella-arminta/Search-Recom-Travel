# Model Hotel
from flask import jsonify
import requests
class Insurance:
    def __init__(self):
        return
    
    def get_all_user(self):
        # endpoint_url_kel_lain = 'http://678.67.8678.678/mahasiswa'
        # try: 
        #     response = requests.get(endpoint_url)
        #     response.raise_for_status()
        #     data = response.json()
            
        #     return data
        
        # except requests.exceptions.RequestException as e:
        #     # Handle any exceptions that occur during the request
        #     return jsonify({"error": str(e)}), 500
        return [
            {
                "id_user":"user1",
                "nama_user": "Ella Arminta",
                "nomor_telepon": "1234567890",
                "alamat": "Bumi"
            },
            {
                "id_user":"user2",
                "nama_user": "Michael Adi",
                "nomor_telepon": "1234567890",
                "alamat": "Bumi"
            },
            {
                "id_user":"user3",
                "nama_user": "Yuandi Vick",
                "nomor_telepon": "1234567890",
                "alamat": "Bumi"
            }
        ]
    
    def get_all_booking(self):
        return [
            {
                "id_booking":"123",
                "id_pembelian":"12345"
            },
            {
                "id_booking":"456",
                "id_pembelian":"12345"
            },
            {
                "id_booking":"789",
                "id_pembelian":"12345"
            }
        ]
    
    def get_all_tipe_asuransi(self):
        return [
            {
                "id_tipe_asuransi":"tipeasuransi1",
                "id_kategori":"kategori1",
                "nama_tipe":"Perusahan",
                "premi_asuransi":"100000"
            },
            {
                "id_tipe_asuransi":"tipeasuransi2",
                "id_kategori":"kategori2",
                "nama_tipe":"Perusahaan",
                "premi_asuransi":"50000"
            },
            {
                "id_tipe_asuransi":"tipeasuransi3",
                "id_kategori":"kategori3",
                "nama_tipe":"Perusahaan",
                "premi_asuransi":"20000"
            }
        ]
    
    def get_all_kategori_asuransi(self):
        return [
            {
                "id_kategori":"kategori1",
                "nama_kategori":"Asuransi kelas A"
                
            },
            {
                "id_kategori":"kategori2",
                "nama_kategori":"Asuransi kelas B"
            },
            {
                "id_kategori":"kategori3",
                "nama_kategori":"Asuransi kelas C"
            }
        ]

    def get_all_pembelian_asuransi(self):
        return [
            {
                "id_pembelian":"0001",
                "id_user":"user1",
                "id_tipe_asuransi":"tipeasuransi1",
                "date_time":"01-01-2001 10:10:10",
                "status_pembayaran":"1"
            },
            {
                "id_pembelian":"0002",
                "id_user":"user2",
                "id_tipe_asuransi":"tipeasuransi2",
                "date_time":"02-02-2002 10:10:10",
                "status_pembayaran":"1"
            },
            {
                "id_pembelian":"0003",
                "id_user":"user3",
                "id_tipe_asuransi":"tipeasuransi3",
                "date_time":"03-03-2003 10:10:10",
                "status_pembayaran":"1"
            }
        ]
    
    def get_all_klaim_asuransi(self):
        return
    def get_all_pembayaran_asuransi(self):
        return
    def get_all_coverage_asuransi(self):
        return
    

