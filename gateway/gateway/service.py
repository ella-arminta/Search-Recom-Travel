import json

from nameko.rpc import RpcProxy
from nameko.web.handlers import http


class GatewayService:
    name = 'gateway'
    header = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "POST, GET, PUT, DELETE, OPTIONS",
        "Access-Control-Allow-Headers": "*",
        "Content-type": "application/json"
    }
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
            return 200,self.header,json.dumps(result)
        
        elif request.method == 'POST':
             # YET Rest Client Payload
            # data = request.get_data(as_text=True)
            # if data == '':
            #     return 400,self.header, json.dumps({
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
                return 400,self.header,json.dumps({
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
                    
                    return 400,self.header,json.dumps({
                        "data": "Invalid form data type. " + ', '.join(error)
                        })

            result = self.service_rpc.add_service(nama, id_lokasi, url, id_service_type)
            return result['code'],self.header,json.dumps(result) 
    
    # delete service by id
    @http('DELETE','/service/<int:id_service>')
    def delete_service(self,request,id_service):
        result = self.service_rpc.delete_service(id_service)
        return result['code'],self.header,json.dumps(result)

    @http('GET', '/service_type')
    def get_all_service_type(self, request):
        result = self.service_rpc.get_all_service_type()
        return 200,self.header,json.dumps(result)
    
    @http('GET', '/lokasi')
    def get_all_lokasi(self, request):
        result = self.service_rpc.get_all_lokasi()
        return 200,self.header,json.dumps(result)
    
    @http('GET','/lokasi/<string:nama_lokasi>')
    def get_lokasi_by_name(self,request,nama_lokasi):
        result = self.service_rpc.get_lokasi_by_name(nama_lokasi)
        return result['code'],self.header,json.dumps(result)

    @http('GET','/service/<string:id_service>')
    def get_service_by_id(self,request,id_service):
        result = self.service_rpc.get_service_by_id(id_service)
        return result['code'],self.header,json.dumps(result)

# HOTEL
    @http('GET', '/hotel/city/<string:id_lokasi>/checkin/<string:checkin>/checkout/<string:checkout>/people/<string:people>/room/<string:room>/minprice/<string:minprice>/maxprice/<string:maxprice>/rating/<string:rating>/sort/<string:sort>')
    def get_all_hotel(self, request, id_lokasi = '-', checkin = '-', checkout = '-', people = '-', minprice = '-', maxprice = '-', rating = '-', sort='-', room="-"):
        # rating : 00000 -> no rating, 10000 -> 1 star, 11000 -> 1 and 2 star, 11100 -> 1,2,3 star, 11110 -> 1,2,3,4 star, 11111 -> 1,2,3,4,5 star
        # min price -> room start from
        # max price -> room start from
        sort = sort.lower()
        allowed_sort = ['lowestprice', 'highestprice', 'highestpopularity','reviewscore','-']
        if sort not in allowed_sort:
            return 400,self.header, json.dumps({
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
            if room != '-':
                room = int(room)
        except:
            return 400,self.header, json.dumps({
                'code': 400,
                'data': 'Invalid id_lokasi/people/minprice/maxprice/room parameter must be integer'
            })
        
        all_hotel = self.hotel_rpc.get_all_hotel(id_lokasi, checkin, checkout,people, minprice, maxprice, rating, sort, room)
        return all_hotel['code'],self.header, json.dumps(all_hotel)
    
    @http('GET', '/hotel/sort')
    def get_all_hotel_sort(self,request):
        result = {
            'code': 200,
            'data': ['lowestprice', 'highestprice', 'highestpopularity','reviewscore','-']
        }
        return result['code'],self.header, json.dumps(result)
    # get hotel by id
    @http('GET','/hotel/<string:id_hotel>/people/<string:people>/room/<string:room>/minprice/<string:minprice>/maxprice/<string:maxprice>')
    def get_hotel_by_id(self,request,id_hotel, people='-', room='-', minprice='-', maxprice='-'):
        try:
            if people != '-':
                people = int(people)
            if minprice != '-':
                minprice = int(minprice)
            if maxprice != '-':
                maxprice = int(maxprice)
            if room != '-':
                room = int(room)
        except:
            return 400,self.header, json.dumps({
                'code': 400,
                'data': 'Invalid id_lokasi/people/minprice/maxprice/room parameter must be integer'
            })
        
        result = self.hotel_rpc.get_hotel_by_id(id_hotel, people, minprice, maxprice, room)
        return result['code'],self.header,json.dumps(result)

# TRANSPORTASI
    @http('GET','/carrental/driver/<int:driver>/city/<int:id_lokasi>/startdate/<string:startdate>/enddate/<string:enddate>/capacity/<string:capacity>/cartype/<string:cartype>/provider/<string:provider>/transmission/<string:transmission>/sort/<string:sort>')
    def get_all_transportasi(self,request, driver, id_lokasi, startdate, enddate, capacity='-', cartype='-', provider='-', transmission='-', sort='-',):
        # Sorting Option
        sort = sort.lower()
        allowed_sort = ['lowestprice', 'highestprice', 'lowestcapacity','highestcapacity','-']
        if sort not in allowed_sort:
            return 400,self.header, json.dumps({
                'code': 400,
                'data': 'Invalid sort parameter. Available sort : ' + str(allowed_sort)
            })
        result = self.carrental_rpc.get_all_carrental(driver, id_lokasi, startdate, enddate, capacity, cartype, provider,transmission, sort)
        return result['code'],self.header, json.dumps(result)
    # get all cartype
    @http('GET','/carrental/cartype/lokasi/<string:id_lokasi>')
    def get_all_cartype(self,request, id_lokasi):
        try :
            id_lokasi = int(id_lokasi)
        except:
            return 400,self.header, json.dumps({
                'code': 400,
                'data': 'Invalid id_lokasi parameter must be integer'
            })
        result = self.carrental_rpc.get_all_cartype(id_lokasi)
        return result['code'],self.header, json.dumps(result)
    # get all provider
    @http('GET','/carrental/provider/lokasi/<int:id_lokasi>')
    def get_all_car_provider(self,request, id_lokasi):
        result = self.carrental_rpc.get_all_provider(id_lokasi)
        return result['code'],self.header, json.dumps(result)
    # get transport by id
    @http('GET','/carrental/service/<int:service_id>/pickup/<string:pickup>/returncar/<string:returncar>/car_id/<string:car_id>')
    def get_carrental_by_id(self,request, service_id, pickup='-', returncar='-', car_id='-'):
        result = self.carrental_rpc.get_carrental_by_id(service_id, pickup, returncar, car_id)
        return result['code'], self.header, json.dumps(result)
    # get carrental by car_key example suzuki_xenia_automatic
    @http('GET','/carrental/<string:car_key>')
    def get_carrental_by_key(self,request, car_key):
        result = self.carrental_rpc.get_carrental_by_key(car_key)
        return result['code'], self.header, json.dumps(result)
    
## TRAVEL AGENT

    # GET ALL PACKAGE + SORT BY PRICE
    @http('GET', '/agent/name/<string:name>/departure_date/<string:departure_date>/return_date/<string:return_date>/number_of_people/<string:number_of_people>/minprice/<string:minprice>/maxprice/<string:maxprice>/sort/<string:sort>')
    def get_all_agent(self, request, name, departure_date, return_date, number_of_people, minprice, maxprice, sort):
        sort = sort.lower()
        allowed_sort = ['lowestprice', 'highestprice', 'quota', 'city', 'departuredate', '-']
        if sort not in allowed_sort:
            return 400, self.header, json.dumps({
                'code': 400,
                'data': 'Invalid sort parameter. Available sort: ' + str(allowed_sort)
            })
        try:
            result = self.agent_rpc.get_all_agent(name, departure_date, return_date, number_of_people, minprice, maxprice, sort)
            return result['code'], self.header, json.dumps(result)
        except Exception as e:
            return 500, self.header, json.dumps({
                'code': 500,
                'data': f"Internal server error: {str(e)}"
            })
    
    @http('GET', '/agent/sort')
    def get_all_agent_sort(self,request):
        result = {
            'code': 200,
            'data': ['lowestprice', 'highestprice', 'quota','city','departuredate', '-']
        }
        return result['code'],self.header, json.dumps(result)
    
    # GET PACKAGE BY ID
    @http('GET', '/agent/<int:service_id>/packagename/<string:packagename>/departuredate/<string:departuredate>/returndate/<string:returndate>/people/<string:people>/price/<string:price>/images/<string:images>')
    def get_agent_by_id (self,request,service_id,packagename,departuredate,returndate,people,price,images):
        try:
            if price != '-':
                price = int(price)
        except:
            return 400,self.header, json.dumps({
                'code': 400,
                'data': 'Invalid service_id/people/price parameter must be integer'
            })
        result = self.agent_rpc.get_agent_by_id(service_id,packagename,departuredate,returndate,people,price,images)
        return result['code'],self.header,json.dumps(result)
    
# ATRAKSI

    # GET ALL ATRAKSI
    @http('GET', '/atraksi/city/title/<string:title>/alamat/<string:alamat>/kota_name/<string:kota_name>/lowest_price/<string:lowest_price>/sort/<string:sort>')
    def get_all_atraksi(self,request, title,alamat,kota_name,lowest_price,sort):
        
        # rating : 00000 -> no rating, 10000 -> 1 star, 11000 -> 1 and 2 star, 11100 -> 1,2,3 star, 11110 -> 1,2,3,4 star, 11111 -> 1,2,3,4,5 star
        # min price -> room start from
        # max price -> room start from
        
        sort = sort.lower()
        allowed_sort = ['lowestprice', 'highestprice', 'highestpopularity','-']
        if sort not in allowed_sort:
            return 400, self.header, json.dumps({
                'code': 400,
                'data': 'Invalid sort parameter. Available sort : ' + str(allowed_sort)
            })

        all_atraksi = self.atraksi_rpc.get_all_atraksi(title,alamat,kota_name,lowest_price,sort)

        print("All Atraksi Response:", all_atraksi)
        return all_atraksi['code'], self.header, json.dumps(all_atraksi)
    

    # GET ALL ATRAKSI
    @http('GET', '/atraksi/city/title/<string:title>/alamat/<string:alamat>/kota_name/<string:kota_name>/lowest_price/<string:lowest_price>/sort/<string:sort>')
    def get_all_atraksi(self,request, title,alamat,kota_name,lowest_price,sort):
        
        # rating : 00000 -> no rating, 10000 -> 1 star, 11000 -> 1 and 2 star, 11100 -> 1,2,3 star, 11110 -> 1,2,3,4 star, 11111 -> 1,2,3,4,5 star
        # min price -> room start from
        # max price -> room start from
        
        sort = sort.lower()
        allowed_sort = ['lowestprice', 'highestprice', 'highestpopularity','-']
        if sort not in allowed_sort:
            return 400, self.header, json.dumps({
                'code': 400,
                'data': 'Invalid sort parameter. Available sort : ' + str(allowed_sort)
            })

        all_atraksi = self.atraksi_rpc.get_all_atraksi(title,alamat,kota_name,lowest_price,sort)

        print("All Atraksi Response:", all_atraksi)
        return all_atraksi['code'], self.header, json.dumps(all_atraksi)
        
    # GET ALL ATRAKSI SORT
    @http('GET', '/atraksi/sort')
    def get_all_atraksi_sort(self,request):
        result = {
            'code': 200,
            'data': ['lowestprice', 'highestprice', 'highestpopularity','reviewscore','-']
        }
        return result['code'],self.header, json.dumps(result)

    # GET ALL PAKET
    @http('GET', '/atraksi/paket/title/<string:title>/type_name/<string:type_name>/deskripsi/<string:deskripsi>/fasilitas/<string:fasilitas>')
    def get_all_paket(self, request, title,type_name,deskripsi,fasilitas):

        result = self.atraksi_rpc.get_all_paket(title,type_name,deskripsi,fasilitas)
        return result['code'], self.header, json.dumps(result)

    # Get paket by id
    @http('GET', '/paket/<int:id_paket>/title/<string:title>/alamat/<string:alamat>/kota_name/<string:kota_name>/lowest_price/<string:lowest_price>')
    def get_paket_by_id(self, request, id_paket, title, alamat, kota_name, lowest_price):
        try:
            if lowest_price != '-':
                lowest_price = int(lowest_price)
        except ValueError:
            return 400, self.header, json.dumps({
                'code': 400,
                'data': 'Invalid lowest_price parameter. Must be integer'
            })
        
        result = self.atraksi_rpc.get_paket_by_id(id_paket, title, alamat, kota_name, lowest_price)
        return result['code'], self.header, json.dumps(result)
    
# AIRLINES
    @http('GET', '/airlines/airport_origin_location_code/<string:airport_origin_location_code>/airport_destination_location_code/<string:airport_destination_location_code>/minprice/<string:minprice>/maxprice/<string:maxprice>/date/<string:date>/start_time/<string:start_time>/end_time/<string:end_time>/sort/<string:sort>')
    def get_all_airlines(self,request,airport_origin_location_code,airport_destination_location_code,minprice,maxprice,date,start_time,end_time,sort):
        if minprice != '-':
            minprice = int(minprice)
        if maxprice != '-':
            maxprice = int(maxprice)
        all_airlines = self.airlines_rpc.get_all_airlines(airport_origin_location_code,airport_destination_location_code,minprice,maxprice,date,start_time,end_time,sort)
        return 200, self.header, json.dumps(all_airlines)
    
    #GET ALL AIRLINES SORT
    @http('GET', '/airlines/sort')
    def get_all_airlines_sort(self,request):
        result = {
            'code': 200,
            'data':['lowestprice','earlydeparture','-']
        }
        return result['code'],self.header, json.dumps(result)
    
    # GET AIRLINES BY ID
    @http('GET','/airlines/service_id/<string:service_id>/airport_origin_location_code/<string:airport_origin_location_code>/airport_destination_location_code/<string:airport_destination_location_code>/flight_date/<string:flight_date>/flight_code/<string:flight_code>')
    def get_airlines_by_id(self,request,service_id,airport_origin_location_code,airport_destination_location_code,flight_date,flight_code):
        if service_id != '-':
            service_id = int(service_id)
        result = self.airlines_rpc.get_airlines_by_id(service_id,airport_origin_location_code,airport_destination_location_code,flight_date,flight_code)
        return result['code'],self.header,json.dumps(result)
    
    
    
    
# INSURANCE
    @http('GET', '/insurance')
    def get_all_insurance(self,request):
        all_insurance = self.insurance_rpc.get_all_insurance()
        return 200,self.header, json.dumps(all_insurance)