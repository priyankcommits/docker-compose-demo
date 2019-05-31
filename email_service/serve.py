from concurrent import futures
import time
import os
import argparse
import grpc
import sys

import email_pb2_grpc
from manager import EmailManager

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    email_pb2_grpc.add_EmailServicer_to_server(EmailManager(), server)
    PORT = os.environ.get("EMAIL_SERVER_PORT", "50053")
    server.add_insecure_port('[::]:{}'.format(PORT))
    sys.stdout.write(("Starting server on port {}\n"
                      "Quit the server with CONTROL-C\n").format(PORT))
    sys.stdout.flush()
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
