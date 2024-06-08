import json

from nameko.rpc import RpcProxy
from nameko.web.handlers import http


class GatewayService:
    name = 'gateway'
    service_rpc = RpcProxy('service_list')
    hotel_rpc = RpcProxy('hotel_service')
    agent_rpc = RpcProxy('travel_agent_service')
    atraksi_rpc = RpcProxy('atraksi_service')
    airlines_rpc = RpcProxy('airlines_service')
    insurance_rpc = RpcProxy('insurance_service')
# SERVICE_LIST
    @http('GET,POST', '/service')
    def service(self, request):
        if request.method == 'GET':
            # if name_service is not None:
            #     result = self.service_rpc.get_service(name_service)
            # else:
            result = self.service_rpc.get_all_service()
            return 200,json.dumps(result)
        
        elif request.method == 'POST':
             # YET Rest Client Payload
            # data = request.get_data(as_text=True)
            # if data == '':
            #     return 400,json.dumps({
            #         "data": "Invalid form data, empty data required. nama (string), id_lokasi (int), url (string) and id_service_type (int) is required"
            #         })
            
            # data = json.loads(data)
            # nama = data.get('nama', None)
            # id_lokasi = data.get('id_lokasi', None)
            # url = data.get('url', None)
            # id_service_type =  data.get('id_service_type', None)

            # Postman form-data
            nama = request.form.get('nama')
            id_lokasi = request.form.get('id_lokasi')
            url = request.form.get('url')
            id_service_type =  request.form.get('id_service_type')

            # cek wajib ada
            if nama is None or id_lokasi is None or url is None or id_service_type is None:
                return 400,json.dumps({
                    "data": "Invalid form data, empty data required. nama (string), id_lokasi (int), url (string) and id_service_type (int) is required"
                    })
            
            # cek tipe data
            if type(id_lokasi) != int or type(id_service_type) != int:
                # convert to int from strimng
                try:
                    id_lokasi = int(id_lokasi)
                    id_service_type = int(id_service_type)
                except:
                    return 400,json.dumps({
                        "data": "Invalid form data type. nama (string), id_lokasi (int), url (string) and id_service_type (int) is required"
                        })

            result = self.service_rpc.add_service(nama, id_lokasi, url, id_service_type)
            return result['code'],json.dumps(result) 
    
    @http('GET', '/service_type')
    def get_all_service_type(self, request):
        result = self.service_rpc.get_all_service_type()
        return 200,json.dumps(result)
    
    @http('GET', '/lokasi')
    def get_all_lokasi(self, request):
        result = self.service_rpc.get_all_lokasi()
        return 200,json.dumps(result)

# HOTEL
    @http('GET', '/hotel/city/<int:id_lokasi>/checkin/<string:checkin>/checkout/<string:checkout>/people/<int:people>/minprice/<int:minprice>/maxprice/<int:maxprice>/rating/<string:rating>')
    def get_all_hotel(self, request, id_lokasi = '-', checkin = '-', checkout = '-', people = '-', minprice = '-', maxprice = '-', rating = '-'):
        # rating : 00000 -> no rating, 10000 -> 1 star, 11000 -> 1 and 2 star, 11100 -> 1,2,3 star, 11110 -> 1,2,3,4 star, 11111 -> 1,2,3,4,5 star
        # min price -> room start from
        # max price -> room start from
        all_hotel = self.hotel_rpc.get_all_hotel(id_lokasi, checkin,checkout,people)
        return all_hotel['code'], json.dumps(all_hotel)

# TRANSPORTASI
# TRAVEL AGENT
    @http('GET', '/agent')
    def get_all_agent(self,request):
        all_agent = self.agent_rpc.get_all_agent()
        return 200, json.dumps(all_agent)
# ATRAKSI
    @http('GET', '/atraksi')
    def get_all_atraksi(self,request):
        all_atraksi = self.atraksi_rpc.get_all_atraksi()
        return 200, json.dumps(all_atraksi)
# AIRLINES
    @http('GET', '/airlines')
    def get_all_airlines(self,request):
            all_airlines = self.airlines_rpc.get_all_airlines()
            return 200, json.dumps(all_airlines)
# INSURANCE
    @http('GET', '/insurance')
    def get_all_insurance(self,request):
            all_insurance = self.insurance_rpc.get_all_insurance()
            return 200, json.dumps(all_insurance)