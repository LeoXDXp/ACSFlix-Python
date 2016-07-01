# publisher

import zmq, os

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.setsockopt(zmq.LINGER, 0)    # discard unsent messages on close
socket.bind('pgm://239.192.1.1:5000')

block_size = 1024
video_file = "/root/video4k/Sony_4K_Camp.mp4"

try:
    video = open(video_file,"rb")
    block_total = ( os.path.getsize(video_file) / 1024 ) + 1
    block_num = 1

    while block_total > block_num:
        block = video.read( block_size  )
        # Send  block
        socket.send_multipart( ['+', block] ) # Enabling ZMQ_SNDMORE
        print block_num 
        block_num += 1

except Exception as e:
    print e

finally:
    socket.send_multipart( ['+', ""] )
    video.close()
    socket.close()
    print "end"
