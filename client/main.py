import grpc

import pir_pb2 as pb2
import pir_pb2_grpc as pb2_grpc
import tenseal as ts
from google.protobuf import empty_pb2

from client.pir.client import Client
from ad_catalog.index_tree import IndexTree


class PirClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051
        self.pir_client = Client()
        self.client_request = self.pir_client.make_and_dec_req(10, 5, 5)

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.PirStub(self.channel)

    def _chunked(self, size, source):
        for i in range(0, len(source), size):
            yield source[i:i + size]

    def get_context(self):
        return self.client_request.ctx

    def push_context(self):
        ctx_bytes = self.client_request.ctx.serialize()
        chunk_size = 1024 * 1024 * 2  # 4 MB
        chunks = self._chunked(chunk_size, ctx_bytes)
        requests = (pb2.PirContext(ctx=c) for c in chunks)
        return self.stub.SaveContext(requests, compression=grpc.Compression.Gzip)

    def get_response(self):
        """
        Client function to call the rpc for GetResponse
        """
        message = pb2.PirRequest(row=self.client_request.row.serialize(),
                                 col=self.client_request.col.serialize())
        return self.stub.GetResponse(message, compression=grpc.Compression.Gzip)

    def get_index_tree(self):
        idx_tree = self.stub.GetIndexTree(empty_pb2.Empty(), compression=grpc.Compression.Gzip)
        return IndexTree().de_serialize(idx_tree)


if __name__ == '__main__':
    client = PirClient()
    client.push_context()
    index_tree = client.get_index_tree()
    print(index_tree.serialize())
    response = client.get_response()
    result = ts.CKKSVector.load(client.get_context(), response.response)
    print(f'{result.decrypt()}')
