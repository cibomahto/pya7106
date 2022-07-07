import a7106
import struct
import time

class eink_server:
    def __init__(self, gateway_id=0x930B51DE, channel=0):
        self.radio = a7106.A7106(spi=[0,0])

        self.gateway_id = gateway_id
        self.radio.set_id(self.gateway_id)

    def serve(self):
        clients = {}

        while True:
            try:
                payload = self.radio.blocking_receive()
                [client_id] = struct.unpack('>I',payload[0:4])
                print('got packet, client_id=0x{:08x}'.format(client_id))

                if not client_id in clients:
                    clients[client_id] = {'rx_count':0}
                clients[client_id]['rx_count'] += 1

                self.radio.set_id(client_id)
                self.radio.transmit('Hi there! count:{}'.format(clients[client_id]['rx_count']).encode('utf-8'))
                self.radio.set_id(self.gateway_id)

                print(clients)


            except a7106.RxError as e:
                print(e)

server = eink_server()
server.serve()
