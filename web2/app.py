import os

from flask import Flask, render_template, request

import grpc

import email_pb2
import email_pb2_grpc
import product_pb2
import product_pb2_grpc

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        MAX_MESSAGE_LENGTH = 4 * 1024 * 1024 * 10
        options = [
            ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
            ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH)
        ]
        channel = grpc.insecure_channel(
            os.environ.get("EMAIL_SERVER_PORT", "localhost:50053"),
            options=options,
        )
        stub = email_pb2_grpc.EmailStub(channel)
        response = stub.SendEmail(email_pb2.EmptyRequest())
        # print("Response is below ========")
        print(response)
        return render_template('forgot.html', response=response)
    return render_template('login.html')


@app.route('/products', methods=['GET'])
def products():
    MAX_MESSAGE_LENGTH = 4 * 1024 * 1024 * 10
    options = [
        ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
        ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH)
    ]
    channel1 = grpc.insecure_channel(
        os.environ.get("PRODUCT_SERVER_PORT", "localhost:50055"),
        options=options,
    )
    stub1 = product_pb2_grpc.ProductAPIStub(channel1)
    response = stub1.GetAllProducts(product_pb2.EmptyRequest())
    return render_template('products.html', response=response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
