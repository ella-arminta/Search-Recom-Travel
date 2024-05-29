from flask import jsonify
import requests

class Agent:
    def __init__(self):
        return
    
    def get_all_agent(self):
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
                "id_agent"  : "001",
                "agent_name": "Dwidaya Tour",
                "agent_address": "Jl. Puncak Indah Lontar No.2 Pakuwon Mall Lt. B1 No.7, Babatan, Kec. Wiyung, Surabaya",
                "agent_phone": "(031) 99147277",
                "agent_city" : "Surabaya",
            },
            {
                "id_agent"  : "002",
                "agent_name": "Golden Rama Tour",
                "agent_address": "Kompleks Darmo Square, Ruko Darma Square, Jl. Raya Darmo No.54-56 Blok D No. 6, DR. Soetomo, Kec. Tegalsari, Surabaya,",
                "agent_phone": "(031) 5666565",
                "agent_city" : "Surabaya",
            },
            {
                "id_agent"  : "003",
                "agent_name": "Rodex Tour",
                "agent_address": "Jl. Raya Darmo, Darmo, Kec. Wonokromo, Surabaya",
                "agent_phone": "(031) 5662000",
                "agent_city" : "Surabaya",
            }
        ]

    def get_all_package(self):
        return  [
            {
                "id_package" : "001",
                "ticket_id"  : "001",
                "hotel_reservation_id" : "001",
                "eticket_id" : "001",
                "price"      : "Rp 500000",
            },
            {
                "id_package" : "002",
                "ticket_id"  : "002",
                "hotel_reservation_id" : "002",
                "eticket_id" : "002",
                "price"      : "Rp 300000",
            },
            {
                "id_package" : "003",
                "ticket_id"  : "003",
                "hotel_reservation_id" : "003",
                "eticket_id" : "003",
                "price"      : "Rp 200000",
            }
        ]
    
    def get_all_detail_package(self):
        return [
            {
                "id_detail" : "001",
                "id_package": "001",
                "description": "Halo ini package termurah!",
                "origin_city": "Surabaya",
                "destination_city": "Jakarta",
                "departure_date" : "29/05/2024",
                "return_date" : "01/06/2024",
                "number_of_people" : "4", 
            },
            {
                "id_detail" : "002",
                "id_package": "002",
                "description": "Halo ini package terjauh!",
                "origin_city": "Denpasar",
                "destination_city": "Surabaya",
                "departure_date" : "24/05/2024",
                "return_date" : "30/05/2024",
                "number_of_people" : "4", 
            },
            {
                "id_detail" : "003",
                "id_package": "003",
                "description": "Halo ini package termahal!",
                "origin_city": "Jakarta",
                "destination_city": "Medan",
                "departure_date" : "31/05/2024",
                "return_date" : "04/06/2024",
                "number_of_people" : "6", 
            }
        ]