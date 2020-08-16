import random
import time
from multiprocessing.context import Process

from distributed_systems_experiment.client import client
from distributed_systems_experiment.server import server

if __name__ == "__main__":
    ports = [5555, 5556, 5557, 5558, 5559, 5510, 5511]

    for port in ports.__iter__():
        Process(target=server, args=(port,)).start()

    while True:
        time.sleep(3)
        random_port = random.choice(ports)
        Process(target=client, args=(random_port,)).start()
