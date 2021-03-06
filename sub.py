# subscriber

import zmq,os

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('epgm://10.10.3.177;239.192.1.1:5000')
#socket.connect('tcp://10.10.3.161:5000')
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
        if not data:
            break

except (Exception, KeyboardInterrupt) as e:
    print "Error e: %s .Packets received = %d, total packets = %s" %(e, data_received, block_num)
    video.close()
    socket.close()

finally:
    print "packets received = %d, total packets = %d" %(data_received, block_num)
    video.close()
    socket.close()
    print "end"
