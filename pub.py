# producer

import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.setsockopt(zmq.LINGER, 0)    # discard unsent messages on close
socket.bind('pgm://239.192.1.1:5000')

while True:
    msg = raw_input('> ')
    if msg == 'quit':
        break
    else:
        socket.send("+%d" %(msg) )
socket.close()
