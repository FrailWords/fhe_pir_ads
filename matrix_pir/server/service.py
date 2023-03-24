import numpy as np

from matrix_pir import itpir_pb2 as pb2
from matrix_pir import itpir_pb2_grpc as pb2_grpc
from matrix_pir.ad_catalog.index_tree import IndexTree
from matrix_pir.server.pir.server import Server


class PirService(pb2_grpc.PirServicer):
    pir_server: Server

    def __init__(self, pir_server):
        self.pir_server = pir_server

    def GetIndexTree(self, request, context):
        index_tree = IndexTree()
        return pb2.IndexTreeResponse(idx_tree=index_tree.serialize())

    def GetResponse(self, request, context):
        req = np.frombuffer(request.request)
        data = self.pir_server.get_data(req)
        return pb2.PirResponse(response=data.tobytes())
