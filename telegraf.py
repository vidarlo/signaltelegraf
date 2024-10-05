#!/usr/bin/env python3

import socket
import threading

def send_signal(dst_ip, dst_port=5919):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(bytes("PLING", "utf-8"), (dst_ip, dst_port))
    s.close()

def recv_signal(bind_ip='0.0.0.0', bind_port=5919):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((bind_ip, bind_port))
    while True:
        data, addr = s.recvfrom(1024)
        print("Received: %s" % data)

if __name__ == "__main__":
    receiver = threading.Thread(target=recv_signal())
    receiver.start()g