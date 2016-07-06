# publisher

import zmq, os

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.setsockopt(zmq.LINGER, 0)    # discard unsent messages on close
socket.bind('pgm://239.192.1.1:5000')

block_size = 512.0
video_file = "/root/video4k/Sony_4K_Camp.mp4"

try:
    video = open(video_file,"rb")
    # We multiply by the percent we want to send, in order to make tests shorter.
    block_total = ( os.path.getsize(video_file) / block_size ) * 0.01
    block_num = 1

    while block_total > block_num:
        block = video.read( block_size  )
        # Send  block
        socket.send_multipart( ['+', block, str(block_num) ], copy=False ) # Enabling ZMQ_SNDMORE
        print block_num 
        block_num += 1

except (Exception, KeyboardInterrupt) as e:
    print e

finally:
    video.close()
    socket.close()
    print "End. Packets sent: %d, B sent: %d, KB sent: %d " %(block_num  ,block_num * block_size, block_num * block_size / 1024)
