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
                "nama_user": "Ella ",
                "nomor_telepon": "1234567890",
                "alamat": "Bumi",
            },
            {
                "id_user":"002",
                "nama_user": "Michael Adi",
                "nomor_telepon": "1234567890",
                "alamat": "Bumi",
            },
            {
                "id_user":"003",
                "nama_user": "Yuandi Vick",
                "nomor_telepon": "1234567890",
                "alamat": "Bumi",
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
        return [
            {
                "id_klaim_asuransi":"001",
                "id_user":"001",
                "id_tipe_asuransi":"001",
                "id_pembelian":"001",
                "id_pembayaran":"001",
                "link_bukti":"testlink1",
                "date_time":"10-10-2010 10:10:10",
                "status_klaim":"1",
            },
            {
                "id_klaim_asuransi":"002",
                "id_user":"002",
                "id_tipe_asuransi":"002",
                "id_pembelian":"002",
                "id_pembayaran":"002",
                "link_bukti":"testlink2",
                "date_time":"11-11-2011 10:10:10",
                "status_klaim":"1",
            },
            {
                "id_klaim_asuransi":"003",
                "id_user":"003",
                "id_tipe_asuransi":"003",
                "id_pembelian":"003",
                "id_pembayaran":"003",
                "link_bukti":"testlink3",
                "date_time":"12-12-2012 10:10:10",
                "status_klaim":"1",
            }
        ]
    def get_all_pembayaran_asuransi(self):
        return [
            {
                "id_pembayaran":"001",
                "id_user":"001",
                "id_pembelian":"001",
                "timestamp": "05-05-2010 10:10:10",
                "total_bayar":"100000",
                "pajak":"1000",
                "jenis_pembayaran":"1",
                "nomor_kartu":"55667788",
                "nomor_telepon":"1234567890",
            },
            {
                "id_pembayaran":"002",
                "id_user":"002",
                "id_pembelian":"002",
                "timestamp": "06-05-2010 10:10:10",
                "total_bayar":"50000",
                "pajak":"1000",
                "jenis_pembayaran":"1",
                "nomor_kartu":"88990011",
                "nomor_telepon":"1234567890",
            },
            {
                "id_pembayaran":"003",
                "id_user":"003",
                "id_pembelian":"003",
                "timestamp": "07-05-2010 10:10:10",
                "total_bayar":"20000",
                "pajak":"1000",
                "jenis_pembayaran":"1",
                "nomor_kartu":"11223344",
                "nomor_telepon":"1234567890",
            }
            
        ]
    def get_all_coverage_asuransi(self):
        return [
            {
                "id_coverage_asuransi":"001",
                "id_tipe_asuransi":"001",
                "coverage":"abcdefg",
                "detail":"ini detail",
                "status":"1"
            },
            {
                "id_coverage_asuransi":"002",
                "id_tipe_asuransi":"002",
                "coverage":"hijklmn",
                "detail":"ini detail",
                "status":"1"
            },
            {
                "id_coverage_asuransi":"002",
                "id_tipe_asuransi":"002",
                "coverage":"opqrstu",
                "detail":"ini detail",
                "status":"1"
            },
        ]
    

