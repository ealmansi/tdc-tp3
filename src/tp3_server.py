#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import ptc
from tp3_config import SERVER_IP, SERVER_PORT, TRANSFER_DATA, TRANSFER_CHUNK_SIZE, TEST_RTO_PARAMS
import time

def send_data(server_sock, alpha, beta):
  server_sock.protocol.set_rto_estimation_parameters(alpha, beta)
  data_index = 0
  while data_index < len(TRANSFER_DATA):
    chunk_size = min(len(TRANSFER_DATA) - data_index, TRANSFER_CHUNK_SIZE)
    chunk = TRANSFER_DATA[data_index : data_index + chunk_size]
    server_sock.send(chunk)
    data_index = data_index + chunk_size
  #   print data_index, ' out of ', len(TRANSFER_DATA), 'bytes sent.\r',
  # print ''

def main():
    if os.geteuid() != 0:
        exit("You need to have root privileges to run this script.\nPlease try again using 'sudo'. Exiting.")
    print 5
    port = SERVER_PORT
    for (alpha, beta,_,_,_) in TEST_RTO_PARAMS:
        with ptc.Socket() as server_sock:
            #print 'Server socket open.'
            server_sock.bind((SERVER_IP, port))
            port = port + 1
            server_sock.listen()
            server_sock.accept(timeout = 30)
            print '%f %f' % (alpha, beta)
            send_data(server_sock, alpha, beta)
        #print 'Server socket closed.'
        print ''
if __name__ == '__main__':
    main()
