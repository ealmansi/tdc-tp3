#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import ptc
from tp3_config import SERVER_IP, SERVER_PORT, TRANSFER_DATA, TRANSFER_CHUNK_SIZE, TEST_RTO_PARAMS
import time

def receive_data(client_sock, ack_drop_rate = None, ack_delay = None, ack_delay_var = 0):
    client_sock.protocol.set_ack_drop_rate(ack_drop_rate)
    client_sock.protocol.set_ack_delay(ack_delay,ack_delay_var)
    data_received = ''
    while len(data_received) < len(TRANSFER_DATA):
      chunk_size = min(len(TRANSFER_DATA) - len(data_received), TRANSFER_CHUNK_SIZE)
      data_received += client_sock.recv(chunk_size)
    #   print len(data_received), ' out of ', len(TRANSFER_DATA), 'bytes received.\r',
    # print ''

def main():
    if os.geteuid() != 0:
        exit("You need to have root privileges to run this script.\nPlease try again using 'sudo'. Exiting.")
    port = SERVER_PORT
    for (_,_,delay,delay_var,drop) in TEST_RTO_PARAMS:
        with ptc.Socket() as client_sock:
            print 'Client socket open.'
            client_sock.connect((SERVER_IP, port), timeout = 30)
            port = port + 1
            receive_data(client_sock, drop, delay,delay_var)
            time.sleep(1)
        print 'Client socket closed.'

if __name__ == '__main__':
    main()
