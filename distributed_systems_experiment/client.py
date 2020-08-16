#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import zmq
from faker import Faker


def client(port: int):
    context = zmq.Context()
    fake = Faker()
    #  Socket to talk to server
    print(f"Connecting to server localhost with port: {port}")
    socket = context.socket(zmq.REQ)
    socket.connect(f"tcp://localhost:{port}")

    socket.send_string(fake.sentence())

    #  Get the reply.
    message = socket.recv()
    print(f"Received the following reply: {message}")
