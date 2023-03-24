import grpc
import numpy as np

from matrix_pir import itpir_pb2 as pb2
from matrix_pir import itpir_pb2_grpc as pb2_grpc
from google.protobuf import empty_pb2

from matrix_pir.ad_catalog.index_tree import IndexTree
from matrix_pir.client.pir.client import Client, ClientRequest


class PirClient(object):
    client_request: ClientRequest

    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'localhost'
        self.server1_port = 50051
        self.server2_port = 50052
        self.pir_client = Client()
        self.client_request = self.pir_client.create_requests(10, 5)

        # instantiate a channel
        self.channel1 = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server1_port))
        self.channel2 = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server1_port))

        # bind the client and the server
        self.stub1 = pb2_grpc.PirStub(self.channel1)
        self.stub2 = pb2_grpc.PirStub(self.channel2)

    def get_response(self):
        """
        Client function to call the rpc for GetResponse
        """
        req1 = pb2.PirRequest(request=self.client_request.req1.tobytes())
        response1 = self.stub1.GetResponse(req1)
        req2 = pb2.PirRequest(request=self.client_request.req2.tobytes())
        response2 = self.stub2.GetResponse(req2)
        resp1 = np.frombuffer(response1.response)
        resp2 = np.frombuffer(response2.response)
        return np.logical_xor(resp1, resp2)

    def get_index_tree(self):
        idx_tree = self.stub1.GetIndexTree(empty_pb2.Empty(), compression=grpc.Compression.Gzip)
        return IndexTree().de_serialize(idx_tree)


def main():
    client = PirClient()
    index_tree = client.get_index_tree()
    print(index_tree.serialize())
    response = client.get_response()
    print(f'{response}')


if __name__ == '__main__':
    main()
