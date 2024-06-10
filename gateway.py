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
    carrental_rpc = RpcProxy('carrental_service')

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
            if nama is None or url is None or id_service_type is None:
                return 400,json.dumps({
                    "data": "Invalid form data, empty data required. nama (string), id_lokasi (int), url (string) and id_service_type (int) is required"
                    })
            
            # cek tipe data
            if (id_lokasi != '' and type(id_lokasi) != int) or type(id_service_type) != int:
                # convert to int from strimng
                try:
                    if id_lokasi != '':
                        id_lokasi = int(id_lokasi)
                    id_service_type = int(id_service_type)
                except:
                    error = []
                    if type(id_lokasi) != int:
                        error.append('id_lokasi (int)')
                    if type(id_service_type) != int:
                        error.append('id_service_type (int)')
                    
                    return 400,json.dumps({
                        "data": "Invalid form data type. " + ', '.join(error)
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
    @http('GET', '/hotel/city/<string:id_lokasi>/checkin/<string:checkin>/checkout/<string:checkout>/people/<string:people>/minprice/<string:minprice>/maxprice/<string:maxprice>/rating/<string:rating>/sort/<string:sort>')
    def get_all_hotel(self, request, id_lokasi = '-', checkin = '-', checkout = '-', people = '-', minprice = '-', maxprice = '-', rating = '-', sort='-'):
        # rating : 00000 -> no rating, 10000 -> 1 star, 11000 -> 1 and 2 star, 11100 -> 1,2,3 star, 11110 -> 1,2,3,4 star, 11111 -> 1,2,3,4,5 star
        # min price -> room start from
        # max price -> room start from
        sort = sort.lower()
        allowed_sort = ['lowestprice', 'highestprice', 'highestpopularity','reviewscore','-']
        if sort not in allowed_sort:
            return 400, json.dumps({
                'code': 400,
                'data': 'Invalid sort parameter. Available sort : ' + str(allowed_sort)
            })
        
        # cek id_lokasi angka atau bukan
        try:
            if id_lokasi != '-':
              id_lokasi = int(id_lokasi)
            if people != '-':
              people = int(people)
            if minprice != '-':
              minprice = int(minprice)
            if maxprice != '-':
              maxprice = int(maxprice)
        except:
            return 400, json.dumps({
                'code': 400,
                'data': 'Invalid id_lokasi/people/minprice/maxprice parameter. must be integer'
            })
        
        all_hotel = self.hotel_rpc.get_all_hotel(id_lokasi, checkin, checkout,people, minprice, maxprice, rating, sort)
        return all_hotel['code'], json.dumps(all_hotel)
    
    @http('GET', '/hotel/sort')
    def get_all_hotel_sort(self,request):
        result = {
            'code': 200,
            'data': ['lowestprice', 'highestprice', 'highestpopularity','reviewscore','-']
        }
        return result['code'], json.dumps(result)

# TRANSPORTASI
    @http('GET','/carrental/driver/<int:driver>/city/<int:id_lokasi>/startdate/<string:startdate>/enddate/<string:enddate>/capacity/<string:capacity>/cartype/<string:cartype>/provider/<string:provider>/transmission/<string:transmission>/sort/<string:sort>')
    def get_all_transportasi(self,request, driver, id_lokasi, startdate, enddate, capacity='-', cartype='-', provider='-', transmission='-', sort='-',):
        # Sorting Option
        sort = sort.lower()
        allowed_sort = ['lowestprice', 'highestprice', 'lowestcapacity','highestcapacity','-']
        if sort not in allowed_sort:
            return 400, json.dumps({
                'code': 400,
                'data': 'Invalid sort parameter. Available sort : ' + str(allowed_sort)
            })
        result = self.carrental_rpc.get_all_carrental(driver, id_lokasi, startdate, enddate, capacity, cartype, provider,transmission, sort)
        return result['code'], json.dumps(result)
    # get all cartype
    @http('GET','/carrental/cartype/lokasi/<int:id_lokasi>')
    def get_all_cartype(self,request, id_lokasi):
        result = self.carrental_rpc.get_all_cartype(id_lokasi)
        return result['code'], json.dumps(result)
    # get all provider
    @http('GET','/carrental/provider/lokasi/<int:id_lokasi>')
    def get_all_cartype(self,request, id_lokasi):
        result = self.carrental_rpc.get_all_provider(id_lokasi)
        return result['code'], json.dumps(result)
    
# TRAVEL AGENT
    @http('GET', '/agent')
    def get_all_agent(self,request):
        all_agent = self.agent_rpc.get_all_agent()
        return 200, json.dumps(all_agent)
# ATRAKSI
    @http('GET', '/atraksi/city/<int:id_lokasi>/attractioname/<string:attractioname>/tanggal/<string:tanggal>/hari/<string:hari>/waktu/<string:waktu>/minprice/<int:minprice>/maxprice/<int:maxprice>/rating/<int:rating>')
    def get_all_atraksi(self,request,id_lokasi,attractioname,tanggal,hari,waktu,minprice,maxprice,rating):
        all_atraksi = self.atraksi_rpc.get_all_atraksi(id_lokasi,attractioname,tanggal,hari,waktu)
        return all_atraksi['code'], json.dumps(all_atraksi)
    
# AIRLINES
    @http('GET', '/airlines/airport_origin_location_code/<string:airport_origin_location_code>/airport_destination_location_code/<string:airport_destination_location_code>/minprice/<string:minprice>/maxprice/<string:maxprice>/date/<string:date>/start_time/<string:start_time>/end_time/<string:end_time>')
    def get_all_airlines(self,request,airport_origin_location_code,airport_destination_location_code,minprice,maxprice,date,start_time,end_time):
        if minprice != '-':
            minprice = int(minprice)
        if maxprice != '-':
            maxprice = int(maxprice)
        all_airlines = self.airlines_rpc.get_all_airlines(airport_origin_location_code,airport_destination_location_code,minprice,maxprice,date,start_time,end_time)
        return 200, json.dumps(all_airlines)
# INSURANCE
    @http('GET', '/insurance')
    def get_all_insurance(self,request):
        all_insurance = self.insurance_rpc.get_all_insurance()
        return 200, json.dumps(all_insurance)