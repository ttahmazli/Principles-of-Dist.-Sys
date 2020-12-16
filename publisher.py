import zmq
import os
import time

context = zmq.Context()
sckt = context.socket(zmq.PUB)  # creating publisher socket
sckt.bind('tcp://127.0.0.1:2000')  # binding this socket to my server with a host IP and a port

myStr = input()  # take string as input
os.chdir(myStr)  # change directory to that string

while True:
    for root, directories, files in os.walk("."):
        for file in files:
            sckt.send_string("Folder named" + " " + myStr + " has " + os.path.join(file))
        # for file in directories:
        #     sckt.send_string("Folder named" + " " + myStr + " has " + os.path.join(file))
        # for file in root:
        #     sckt.send_string("Folder named" + " " + myStr + " has " + os.path.join(file))
    time.sleep(5)
    # Sleeping here for putting buffer for while
    # as server won't be shut down because I use loop.
    # I could skip putting while and server would be down auto.ly
    # but as I saw from recordings, you were shutting it down manually too.
    # Also, I searched for ways of scanning a directory
    # I cut the parts that I found useless and didn't understand :D
    # Second loop streams folder names in directory too
    # Third loop does interesting things that I discovered by mistake :D
