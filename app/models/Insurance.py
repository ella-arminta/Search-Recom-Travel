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
                "id_user":"001",
                "nama_user": "Ella Arminta",
                "nomor_telepon": "1234567890",
                "alamat": "Bumi"
            },
            {
                "id_user":"002",
                "nama_user": "Michael Adi",
                "nomor_telepon": "1234567890",
                "alamat": "Bumi"
            },
            {
                "id_user":"003",
                "nama_user": "Yuandi Vick",
                "nomor_telepon": "1234567890",
                "alamat": "Bumi"
            }
        ]
    
    def get_all_booking(self):
        return [
            {
                "id_booking":"001",
                "id_pembelian":"001"
            },
            {
                "id_booking":"002",
                "id_pembelian":"0002"
            },
            {
                "id_booking":"003",
                "id_pembelian":"003"
            }
        ]
    
    def get_all_tipe_asuransi(self):
        return [
            {
                "id_tipe_asuransi":"001",
                "id_kategori":"001",
                "nama_tipe":"Perusahan",
                "premi_asuransi":"100000"
            },
            {
                "id_tipe_asuransi":"002",
                "id_kategori":"002",
                "nama_tipe":"Perusahaan",
                "premi_asuransi":"50000"
            },
            {
                "id_tipe_asuransi":"003",
                "id_kategori":"003",
                "nama_tipe":"Perusahaan",
                "premi_asuransi":"20000"
            }
        ]
    
    def get_all_kategori_asuransi(self):
        return [
            {
                "id_kategori":"001",
                "nama_kategori":"Asuransi kelas A"
                
            },
            {
                "id_kategori":"002",
                "nama_kategori":"Asuransi kelas B"
            },
            {
                "id_kategori":"003",
                "nama_kategori":"Asuransi kelas C"
            }
        ]

    def get_all_pembelian_asuransi(self):
        return [
            {
                "id_pembelian":"001",
                "id_user":"001",
                "id_tipe_asuransi":"001",
                "date_time":"01-01-2001 10:10:10",
                "status_pembayaran":"1"
            },
            {
                "id_pembelian":"002",
                "id_user":"002",
                "id_tipe_asuransi":"002",
                "date_time":"02-02-2002 10:10:10",
                "status_pembayaran":"1"
            },
            {
                "id_pembelian":"003",
                "id_user":"003",
                "id_tipe_asuransi":"003",
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
    

