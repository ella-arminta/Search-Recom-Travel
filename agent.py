from nameko.rpc import rpc

import dependencies

class TravelAgentService:

    name = 'travel_agent_service'

    database = dependencies.Database()

    @rpc
    def get_all_agent(self):
        agent_services = self.database.get_service_by_type(3)
        return agent_services