import a7106
import struct
import time
import argparse

class eink_client:
    def __init__(self, client_id=0x12345679, gateway_id=0x930B51DE, channel=0):
        pins = {
                'cs':10,
                'ck':9,
                'da':11,
                'io1':5,
                'io2':6,
                }
        self.radio = a7106.A7106(pins=pins)

        self.client_id = client_id
        self.gateway_id = gateway_id

    def test(self):
        print('Starting client simulator, id=0x{:08x}'.format(self.client_id))
        while True:
            self.radio.set_id(self.gateway_id)

            payload = bytearray()
            payload.extend(struct.pack('>I', self.client_id))
            self.radio.transmit(payload)

            self.radio.set_id(self.client_id)

            try:
                payload = self.radio.blocking_receive()
                print('got packet, payload={}'.format(payload.decode('utf-8')))


            except a7106.RxError as e:
                print(e)

            time.sleep(1)

parser = argparse.ArgumentParser(description='A7106 eink client simulator')
parser.add_argument('--id', help='Client ID')
args = parser.parse_args()

client = eink_client(client_id=int(args.id, base=0))
client.test()
