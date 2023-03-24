from concurrent import futures

import grpc

from matrix_pir import itpir_pb2_grpc as pb2_grpc
from matrix_pir.server.pir.server import Server
from matrix_pir.server.service import PirService


def main():
    size = 10
    pir_server = Server(size)

    server1 = grpc.server(futures.ThreadPoolExecutor(max_workers=5),compression=grpc.Compression.Gzip)
    pb2_grpc.add_PirServicer_to_server(PirService(pir_server), server1)
    server1.add_insecure_port('[::]:50051')
    server1.start()
    server1.wait_for_termination()

    server2 = grpc.server(futures.ThreadPoolExecutor(max_workers=5),compression=grpc.Compression.Gzip)
    pb2_grpc.add_PirServicer_to_server(PirService(pir_server), server2)
    server2.add_insecure_port('[::]:50052')
    server2.start()
    server2.wait_for_termination()


if __name__ == "__main__":
    main()
