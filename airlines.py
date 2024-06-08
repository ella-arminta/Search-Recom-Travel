from nameko.rpc import rpc
import requests
import dependencies

class AirlinesService:

    name = 'airlines_service'

    database = dependencies.Database()

    # @rpc
    # def get_all_airline(self,nama_maskapai):
    #     airlines_service = self.database.get_service_by_type(2)
    #     return airlines_service
    @rpc
    def get_all_airlines(self):
        flights_services = self.database.get_service_by_type(2)
        data=[]
        
        for flights_service in flights_services:
            endpoint_url = flights_service['url']
            
            #get all flights
            try:
                 # /airlines
                response = requests.get(endpoint_url)
                response.raise_for_status()
                data = response.json()
                # data yang diterima bentuknya : DUMMY
                # PERTANYAAN apakah hotel masih menyimpan hotel detail
                # yang ngecek apakah roomnya avail atau gk itu dari function hotel, atau function search&Recom
                data = [
                    {   
                        'flight_id':'1',
                        'flight_code_id':'ID123',
                        'class_id':'1',
                        'airport_id':'1',
                        'capacity':100,
                        'date':'01/01/2001',
                        'weight':50,
                        'delay':100,
                        'status':True
                    },
                    {   
                        'flight_id':'2',
                        'flight_code_id':'ID123',
                        'class_id':'2',
                        'airport_id':'2',
                        'capacity':100,
                        'date':'02/02/2002',
                        'weight':50,
                        'delay':100,
                        'status':True
                    },
                ]
                
            except requests.exceptions.RequestException as e:
                # Handle any exceptions that occur during the request
                # TODO add error to database
                continue
        return{
            'code':200,
            'data':data
        }