# subscriber

import zmq,os

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('pgm://239.192.1.1:5000')
socket.setsockopt(zmq.SUBSCRIBE, "+")

data = "!"
data_received = 0
videofile = "testpython.mp4"
if os.path.exists(videofile):
    os.remove(videofile)

try:
    video = open(videofile,'wb')
    
    while data :
        identifier , data, block_num = socket.recv_multipart(copy=False)
        video.write( data )
        print block_num
        data_received += 1

except (Exception, KeyboardInterrupt) as e:
    print e
    print "packets received = %d, total packets = %d" %(data_received, block_num)
    video.close()
    socket.close()

finally:
    video.close()
    socket.close()
    print "end"
