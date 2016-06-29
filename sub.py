# consumer

import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('epgm://239.192.1.1:5000')
socket.setsockopt(zmq.SUBSCRIBE, 'test')
socket.setsockopt(zmq.SUBSCRIBE, 'topic_1')

while True:
    data = socket.recv()
    print data
