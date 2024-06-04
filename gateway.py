import json

from nameko.rpc import RpcProxy
from nameko.web.handlers import http


class GatewayService:
    name = 'gateway'
    searhrecom_rpc = RpcProxy('searchrecom')

# Hotel
# Transportasi
# Travel Agent
# Atraksi
# Airlines
# Insurance