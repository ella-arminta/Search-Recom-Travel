from nameko.rpc import rpc

import dependencies

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
        check_lokasi = self.database.get_lokasi_by_id(id_lokasi)
        check_service_type = self.database.get_service_type_by_id(id_service_type)
        all_lokasi = self.database.get_all_lokasi()
        all_service_type = self.database.get_all_service_type()

        if check_lokasi is None:
            return {
                'code' : 400,
                'data' : "Lokasi not found. Available Lokasi : " + str(all_lokasi)
            }
        if check_service_type is None:
            return {
                'code' : 400,
                'data' : "Service Type not found. Available Service Type : " + str(all_service_type)
            }
        result = self.database.add_service(nama, id_lokasi, url, id_service_type)
        return result