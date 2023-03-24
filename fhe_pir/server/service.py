import tenseal as ts
from google.protobuf import empty_pb2

import pir_pb2 as pb2
import pir_pb2_grpc as pb2_grpc
from fhe_pir.ad_catalog.index_tree import IndexTree
from fhe_pir.server.pir.server import Server


class PirService(pb2_grpc.PirServicer):
    context: ts.Context
    pir_server: Server

    def __init__(self, pir_server):
        self.pir_server = pir_server

    def GetIndexTree(self, request, context):
        index_tree = IndexTree()
        return pb2.IndexTreeResponse(idx_tree=index_tree.serialize())

    def SaveContext(self, request_iterator, context):
        msg = bytearray()
        for req in request_iterator:
            msg.extend(req.ctx)
        self.context = ts.context_from(bytes(msg))
        return empty_pb2.Empty()

    def GetResponse(self, request, context):
        row = ts.CKKSVector.load(self.context, request.row)
        col = ts.CKKSVector.load(self.context, request.col)
        data = self.pir_server.get_data(row, col)
        return pb2.PirResponse(response=data.serialize())
