from nameko.rpc import rpc
from decimal import Decimal
import dependencies
import requests
import random

class TravelAgentService:

    name = 'travel_agent_service'

    database = dependencies.Database()

    @rpc
    def get_all_agent(self, id_lokasi,packagename,startdate,enddate,people,minprice, maxprice, rating, sort):
        
        # get all service that is hotel and in a location
        if id_lokasi != '-':
            agent_services = self.database.get_service_by_type_lokasi(3, id_lokasi)
        else:
            agent_services = self.database.get_service_by_type(3)
        
        return agent_services