from concurrent import futures
import time
import os
import argparse
import grpc
import sys

import product_pb2_grpc
from manager import ProductManager
from utils import load_initial_data

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    product_pb2_grpc.add_ProductAPIServicer_to_server(ProductManager(), server)
    PORT = os.environ.get("PRODUCT_SERVER_PORT", "50055")
    server.add_insecure_port('[::]:{}'.format(PORT))
    sys.stdout.write(("Starting server on port {}\n"
                      "Quit the server with CONTROL-C\n").format(PORT))
    sys.stdout.flush()
    load_initial_data()
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run server for email service')
    parameters = parser.parse_args()
    serve()
