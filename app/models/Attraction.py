from flask import jsonify
import requests

# class Attraction
class Attraction:
    def __init__(self):
        return
    
    def get_all_attraction(self):
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
                "atraksi_id"    : "001",
                "attraction_name": "Taman Safari Prigen",
                "attraction_address": "Jl. RT.12/RW.06, Gn. Princi, Jatiarjo, Kec. Prigen, Pasuruan",
                "attraction_price": "Rp. 200.000",
                "Kota"            : "Pasuruan",
                "Provinsi"        : "Jawa Timur",
                "gps_location"    : "0",
                "lowest_price"    : "0",
                "discount_price"  : "0",
                "is_active"       : "1",
                "deskripsi"       : "asdjjfk",
                "info_penting"    : "akakjdkk",
                "highlights"      : "<br> - Taman Safari Prigen merupakan kebun binatang dengan konsep safari yang terletak di Prigen, Jawa Timur, di mana kita dapat melihat satwa lewat Safari Adventure.<br>- Lihat dan berinteraksi lebih dekat dengan satwa-satwa lewat pertunjukan satwa, seperti Elephant’s Story dan Bird Show." 
                                    ,
            },
            {
                "atraksi_id"    : "002",
                "attraction_name": "Jatim Park 2",
                "attraction_address": "Jl. Raya Oro-Oro Ombo No.9, Temas, Kec. Batu, Kota Batu",
                "attraction_price": "Rp. 125.000",
                "Kota"            : "Batu",
                "Provinsi"        : "Jawa Timur",
                "gps_location"    : "0",
                "lowest_price"    : "0",
                "discount_price"  : "0",
                "is_active"       : "1",
                "highlights"      : " - Nikmati hari yang penuh keceriaan bersama lebih dari 200 hewan memukau di Batu Secret Zoo",
            },
            {
                "atraksi_id"    : "003",
                "attraction_name": "Batu Night Spectacular",
                "attraction_address": "Jl. Hayam Wuruk No.1, Oro-Oro Ombo, Kec. Batu, Kota Batu",
                "attraction_price": "Rp. 125.000",
                "Kota"            : "Batu",
                "Provinsi"        : "Jawa Timur",
                "gps_location"    : "0",
                "lowest_price"    : "0",
                "discount_price"  : "0",
                "is_active"       : "1",
                "highlights"      : " - Spend your evening at Batu Night Spectacular, a next-level night market in Batu",
            }
        ]

    def get_all_photos(self):
        return [
            {
                "id_photos" : "001",
                "atraksi_id"    : "001",
                "image" :"upload/atraksi/image/1234567abcd.png",
                "placeholder" : "Foto1.png",
            },
            {
                "id_photos" : "002",
                "atraksi_id"    : "002",
                "image" :"upload/atraksi/image/567891efgh.png",
                "placeholder" : "Foto2.png",
            },
            {
                "id_photos" : "003",
                "atraksi_id"    : "003",
                "image" :"upload/atraksi/image/1234789jklm.png",
                "placeholder" : "Foto3.png",
            }
        ]
    
    def get_jam_buka(self):
        return [
            {
                "id_jam_buka" : "001",
                "atraksi_id" : "001",
                "hari" : "Senin-Minggu",
                "waktu" : "09:00 - 18:00",
                "is_active" : "True",
            },
            {
                "id_jam_buka" : "002",
                "atraksi_id" : "002",
                "hari" : "Senin-Minggu",
                "waktu" : "10:00 - 17:00",
                "is_active" : "True",
            },
            {
                "id_jam_buka" : "003",
                "atraksi_id" : "003",
                "hari" : "Senin-Minggu",
                "waktu" : "09:30 - 16:30",
                "is_active" : "True",
            }
        ]
    
    def get_all_paket(self):
        return [
            {
                "id_paket" : "001",
                "atraksi_id" : "001",
                "type_id" : "001",
                "title" : "Tiket fast track", 
                "deskripsi"       : "asdjjfk",
                "fasilitas"     : "Mushola",
                "cara_penukaran" : "aadfsa",
                "syarat_dan_ketentuan" : "adewnsjs",
                "harga" : "Rp. 100.000",
                "harga_discount" : "Rp 30.000",
                "masa_berlaku" : "1",
                "is_refundable" : "1",
            },
            {
                "id_paket" : "002",
                "atraksi_id" : "002",
                "type_id" : "002",
                "title" : "Tiket terusan (full day)", 
                "deskripsi"       : "bcdesa",
                "fasilitas"     : "Gereja",
                "cara_penukaran" : "redeem",
                "syarat_dan_ketentuan" : "nshsjkiak",
                "harga" : "Rp. 120.000",
                "harga_discount" : "Rp 25.000",
                "masa_berlaku" : "1",
                "is_refundable" : "1",
            },
            {
                "id_paket" : "003",
                "atraksi_id" : "003",
                "type_id" : "003",
                "title" : "Tiket two day pass", 
                "deskripsi"       : "klmnaok",
                "fasilitas"     : "Toilet Difabel",
                "cara_penukaran" : "bnkdlsa",
                "syarat_dan_ketentuan" : "mnslaoka",
                "harga" : "Rp. 75.000",
                "harga_discount" : "Rp 15.000",
                "masa_berlaku" : "1",
                "is_refundable" : "0",
            }
        ]
    
    def get_eticket(self):
        return [
            {
                "id_eticket" : "001",
                "booking_code" : "001",
                "tiket_code" : "A100",
                "atraksi_id" : "001",
                "paket_id"   : "001",
                "nama"       : "Budi",
                "jenis"      : "Online",
            },
            {
                "id_eticket" : "002",
                "booking_code" : "002",
                "tiket_code" : "A101",
                "atraksi_id" : "002",
                "paket_id"   : "002",
                "nama"       : "Johny",
                "jenis"      : "Offline",
            },
            {
                "id_eticket" : "001",
                "booking_code" : "003",
                "tiket_code" : "A102",
                "atraksi_id" : "003",
                "paket_id"   : "003",
                "nama"       : "Andy",
                "jenis"      : "Online",
            }
        ]