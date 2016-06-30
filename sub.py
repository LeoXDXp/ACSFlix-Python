# consumer

import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('pgm://239.192.1.1:5000')
socket.setsockopt(zmq.SUBSCRIBE, "+")

try:
    video = open('testpython.mp4','wb')
    data = 1
    while data :
        data = socket.recv_multipart()
        #video.write( data )
        print data

except Exception as e:
    print e

finally:
    video.close()
    socket.close()

