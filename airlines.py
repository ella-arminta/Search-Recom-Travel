from nameko.rpc import rpc

import dependencies

class AirlinesService:

    name = 'airlines_service'

    database = dependencies.Database()

    @rpc
    def get_all_airlines(self):
        airlines_service = self.database.get_service_by_type(2)
        return airlines_service