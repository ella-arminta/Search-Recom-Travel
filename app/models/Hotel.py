# Model Hotel
from flask import jsonify
import requests
class Hotel:
    def __init__(self):
        return
    
    def get_all_hotel(self):
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
                "hotel_name": "Hotel A",
                "hotel_address": "Jalan A",
                "hotel_price": "Rp. 100.000",
                'asdfasd':'asdfsd'
            },
            {
                "hotel_name": "Hotel B",
                "hotel_address": "Jalan B",
                "hotel_price": "Rp. 200.000"
            },
            {
                "hotel_name": "Hotel C",
                "hotel_address": "Jalan C",
                "hotel_price": "Rp. 300.000"
            }
        ]

