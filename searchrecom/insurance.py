from nameko.rpc import rpc

import searchrecom.dependencies as dependencies

class InsuranceService:

    name = 'insurance_service'

    database = dependencies.Database()

    @rpc
    def get_all_insurance(self):
        insurance_service = self.database.get_service_by_type(6)
        return insurance_service