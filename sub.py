# subscriber

import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('pgm://239.192.1.1:5000')
socket.setsockopt(zmq.SUBSCRIBE, "+")

data = 1
counter = 1
try:
    video = open('testpython.mp4','wb')
    
    while data :
        identifier , data = socket.recv_multipart()
        video.write( data )
        print counter, len(data)
        counter += 1

except Exception as e:
    print e
    video.close()
    socket.close()

finally:
    video.close()
    socket.close()
    print "end"
