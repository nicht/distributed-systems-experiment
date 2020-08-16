#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#
import zmq
from faker import Faker


def server(port: int):
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    print(f"Starting the server at port: {port}")
    socket.bind(f"tcp://*:{port}")
    Faker.seed(0)
    fake = Faker()
    while True:
        #  Wait for next request from client
        message = socket.recv()
        print(f"Received message: {message}")

        #  Send reply back to client
        socket.send_string(fake.sentence())
