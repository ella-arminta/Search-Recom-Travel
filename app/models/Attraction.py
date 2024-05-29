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
                "attraction_name": "Taman Safari Prigen",
                "attraction_address": "Jl. RT.12/RW.06, Gn. Princi, Jatiarjo, Kec. Prigen, Pasuruan",
                "attraction_price": "Rp. 200.000",
                "highlights"      : " - Taman Safari Prigen merupakan kebun binatang dengan konsep safari yang terletak di Prigen, Jawa Timur, di mana kita dapat melihat satwa lewat Safari Adventure."
                                    " - Lihat dan berinteraksi lebih dekat dengan satwa-satwa lewat pertunjukan satwa, seperti Elephant’s Story dan Bird Show."
                                    " - Kunjungi dan berfoto dengan satwa-satwa yang ada di Baby Zoo, Aquatic Land, dan Satwa Tunggang."
                                    " - Cocok untuk: Keluarga Asyik dan Bersama Pasangan.",
            },
            {
                "attraction_name": "Jatim Park 2",
                "attraction_address": "Jl. Raya Oro-Oro Ombo No.9, Temas, Kec. Batu, Kota Batu",
                "attraction_price": "Rp. 125.000",
                "highlights"      : " - Nikmati hari yang penuh keceriaan bersama lebih dari 200 hewan memukau di Batu Secret Zoo"
                                    " - Jelajahi era kuno yang memukau dengan pengunjungi Museum Satwa, rumah bagi sekitar 1,000 replika spesies prasejarah"
                                    " - Temui hewan-hewan menggemaskan dan dapatkan kesempatan memberi makan burung pelikan sambil berlayar di atas perahu di River Adventure"
                                    " - Abadikan momen manismu di Sweet Memories Selfie, surganya selfie yang dihiasi instalasi-instalasi unik",
            },
            {
                "attraction_name": "Batu Night Spectacular",
                "attraction_address": "Jl. Hayam Wuruk No.1, Oro-Oro Ombo, Kec. Batu, Kota Batu",
                "attraction_price": "Rp. 125.000",
                "highlights"      : " - Spend your evening at Batu Night Spectacular, a next-level night market in Batu"
                                    " - For thrill seekers, you can put your courage to test by going inside Rumah Hantu and Witch Castle"
                                    " - Are you up for more challenge? Try cycling upside-down on Sepeda Gila or standing against the gravity at Gravitron"
                                    " - Your little ones can also have fun trying rides like Merry Go Round and Mini Train",
            }
        ]
