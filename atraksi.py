from nameko.rpc import rpc

import dependencies

class AtraksiService:

    name = 'atraksi_service'

    database = dependencies.Database()

    @rpc
    def get_all_atraksi(self):
        atraksi_services = self.database.get_service_by_type(5)
        return atraksi_services