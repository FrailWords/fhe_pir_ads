from concurrent import futures

import grpc

import pir_pb2_grpc as pb2_grpc
from fhe_pir.server.pir.server import Server

from fhe_pir.server.service import PirService


def main():
    size = 10
    pir_server = Server(size)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5),compression=grpc.Compression.Gzip)
    pb2_grpc.add_PirServicer_to_server(PirService(pir_server), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    main()
