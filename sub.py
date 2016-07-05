# subscriber

import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('pgm://239.192.1.1:5000')
socket.setsockopt(zmq.SUBSCRIBE, "+")

data = "!"
try:
    video = open('testpython.mp4','wb')
    
    while len(data) :
        identifier , data, block_num = socket.recv_multipart()
        video.write( data )
        print block_num

except Exception as e:
    print e
    video.close()
    socket.close()

finally:
    video.close()
    socket.close()
    print "end"
