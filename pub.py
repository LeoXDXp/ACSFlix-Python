# publisher

import zmq, os

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.setsockopt(zmq.LINGER, 0)    # discard unsent messages on close
sock.setsockopt(zmq.SWAP, 200*2**10) # 200 KB Swapfile handled by ZMQ
#  For example ZMQ_RATE, ZMQ_RECOVERY_IVL and ZMQ_MCAST_LOOP for PGM.       
socket.bind('pgm://239.192.1.1:5000')
#socket.bind('tcp://10.10.3.161:5000')

block_size = 256.0
video_file = "/root/video4k/Sony_4K_Camp.mp4"

try:
    video = open(video_file,"rb")
    # We multiply by the percent we want to send, in order to make tests shorter.
    block_total = ( os.path.getsize(video_file) / block_size ) * 0.05
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
    socket.send_multipart( ['+', '', str(block_num)   ], copy=False )
    video.close()
    socket.close()
    print "End. Packets sent: %d, B sent: %d, MB sent: %f " %(block_num  ,block_num * block_size, block_num * block_size / 1024**2)
