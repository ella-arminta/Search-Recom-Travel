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
                "agent_name": "Dwidaya Tour",
                "agent_address": "Jl. Puncak Indah Lontar No.2 Pakuwon Mall Lt. B1 No.7, Babatan, Kec. Wiyung, Surabaya",
                "agent_phone": "(031) 99147277",
                "agent_city" : "Surabaya",
            },
            {
                "agent_name": "Golden Rama Tour",
                "agent_address": "Kompleks Darmo Square, Ruko Darma Square, Jl. Raya Darmo No.54-56 Blok D No. 6, DR. Soetomo, Kec. Tegalsari, Surabaya,",
                "agent_phone": "(031) 5666565",
                "agent_city" : "Surabaya",
            },
            {
                "agent_name": "Rodex Tour",
                "agent_address": "Jl. Raya Darmo, Darmo, Kec. Wonokromo, Surabaya",
                "agent_phone": "(031) 5662000",
                "agent_city" : "Surabaya",
            }
        ]
