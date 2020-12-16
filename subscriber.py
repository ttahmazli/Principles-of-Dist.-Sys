import zmq
import time

context = zmq.Context()
sckt = context.socket(zmq.SUB)  # creating subscriber socket
sckt.connect('tcp://127.0.0.1:2000')  # connecting this socket the server
sckt.setsockopt_string(zmq.SUBSCRIBE, 'Folder')

while True:
    time.sleep(2)  # also sleeping here for not taking all file names at once
    message = sckt.recv()  # copying received string to message
    print(message)  # printing message

