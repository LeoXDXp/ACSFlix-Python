# producer

import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.setsockopt(zmq.LINGER, 0)    # discard unsent messages on close
socket.bind('pgm://239.192.1.1:5000')

block_size = 1024

try:
    video = open("/root/video4k/Sony_4K_Camp.mp4","rb")
    block = 1
    while block:
        block = video.read( block_size  )
        # Send  block
        socket.send_multipart( ['+', block] ) # Enabling ZMQ_SNDMORE
except Exception as e:
    print e

finally:
    socket.send_multipart( ['+', ""] )
    video.close()
    socket.close()
    print "end"
