#!/usr/bin/env python3

import socket
import threading
from time import sleep

designator=b'GAR' # This stations identification. Three bytes.
receivefrom=[ b'THU', b'GAR'] # Our neighbouring stations
unmanned=True

def send_signal(dst_ip, data, type=b'\x01', dst_port=5919, magic=b'GVB'):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(magic + type +data, (dst_ip, dst_port))
    s.close()

def recv_signal(bind_ip='0.0.0.0', bind_port=5919, magic=b'GVB'):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((bind_ip, bind_port))
    while True:
        data, addr = s.recvfrom(1024)
        if data[0:3] == magic and data[4:7] in receivefrom and data[3] == b'\x01':
            print("Packet from %s" % data[4:7])
            if unmanned and data[6:9] != designator:
                send_signal(dst_ip='127.0.0.1', data=designator + data[3:6])
                print("Resent")

def send_alive():
    while True:
        send_signal('127.0.0.1', b'ALL'+designator, type=b'\x02')
        sleep(1)

def get_input():
    while True:
        input("Press enter")
        send_signal('127.0.0.1', designator)

if __name__ == "__main__":
    receiver = threading.Thread(target=recv_signal)
    receiver.start()
    print("Receiver running")
    sender = threading.Thread(target=get_input)
    sender.start()
