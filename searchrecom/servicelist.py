from nameko.rpc import rpc

import searchrecom.dependencies as dependencies

class ServiceService:

    name = 'service_list'

    database = dependencies.Database()

    @rpc
    def get_all_service(self):
        services = self.database.get_all_service()
        for service in services:
            service['lokasi'] = self.database.get_lokasi_by_id(service['id_lokasi'])
            service['service_type'] = self.database.get_service_type_by_id(service['id_service_type'])
            del service['id_lokasi']
            del service['id_service_type']

        return {
            'code' : 200,
            'data' : services
        }

    @rpc 
    def get_service(self, name):
        service = self.database.get_service_by_name(name)
        if service is None:
            return {
                'code' : 404,
                'data' : "Service not found"
            }
        return {
            'code' : 200,
            'data' : service
        }
    
    @rpc 
    def get_service_by_id(self, id_service):
        service = self.database.get_service_by_id(id_service)
        if service is None:
            return {
                'code' : 404,
                'data' : "Service not found"
            }
        return {
            'code' : 200,
            'data' : service
        }

    
    @rpc
    def get_all_service_type(self):
        service_type = self.database.get_all_service_type()
        return {
            'code' : 200,
            'data' : service_type
        }
    
    @rpc
    def get_all_lokasi(self):
        lokasi = self.database.get_all_lokasi()
        return {
            'code' : 200,
            'data' : lokasi
            }
    
    @rpc
    def add_service(self, nama, id_lokasi, url, id_service_type):
        check_lokasi = None
        if id_lokasi != '':
            check_lokasi = self.database.get_lokasi_by_id(id_lokasi)
        else: 
            id_lokasi = None
        check_service_type = self.database.get_service_type_by_id(id_service_type)
        all_lokasi = self.database.get_all_lokasi()
        all_service_type = self.database.get_all_service_type()

        if id_lokasi is not None and check_lokasi is None:
            return {
                'code' : 400,
                'data' : "Lokasi not found. Available Lokasi : " + str(all_lokasi)
            }
        if check_service_type is None or check_service_type == '':
            return {
                'code' : 400,
                'data' : "Service Type not found. Available Service Type : " + str(all_service_type)
            }
        result = self.database.add_service(nama, id_lokasi, url, id_service_type)
        return result