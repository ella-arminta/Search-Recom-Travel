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
                "highlights"      : "<br> - Taman Safari Prigen merupakan kebun binatang dengan konsep safari yang terletak di Prigen, Jawa Timur, di mana kita dapat melihat satwa lewat Safari Adventure.<br>- Lihat dan berinteraksi lebih dekat dengan satwa-satwa lewat pertunjukan satwa, seperti Elephant’s Story dan Bird Show." 
                                    ,
            },
            {
                "atraksi_id"    : "002",
                "attraction_name": "Jatim Park 2",
                "attraction_address": "Jl. Raya Oro-Oro Ombo No.9, Temas, Kec. Batu, Kota Batu",
                "attraction_price": "Rp. 125.000",
                "highlights"      : " - Nikmati hari yang penuh keceriaan bersama lebih dari 200 hewan memukau di Batu Secret Zoo",
            },
            {
                "atraksi_id"    : "003",
                "attraction_name": "Batu Night Spectacular",
                "attraction_address": "Jl. Hayam Wuruk No.1, Oro-Oro Ombo, Kec. Batu, Kota Batu",
                "attraction_price": "Rp. 125.000",
                "highlights"      : " - Spend your evening at Batu Night Spectacular, a next-level night market in Batu",
            }
        ]

    def get_all_photos(self):
        return [
            {
                "id_photos" : "001",
                "atraksi_id"    : "001",
                "image" :"PIC1",
                "placeholder" : "Foto1",
            },
            {
                "id_photos" : "002",
                "atraksi_id"    : "002",
                "image" :"PIC2",
                "placeholder" : "Foto2",
            },
            {
                "id_photos" : "003",
                "atraksi_id"    : "003",
                "image" :"PIC3",
                "placeholder" : "Foto3",
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