#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import ptc
from tp3_config import SERVER_IP, SERVER_PORT, TRANSFER_DATA, TRANSFER_CHUNK_SIZE
import time

def main():
    if os.geteuid() != 0:
        exit("You need to have root privileges to run this script.\nPlease try again using 'sudo'. Exiting.")

    with ptc.Socket() as server_sock:
        server_sock.bind((SERVER_IP, SERVER_PORT))
        server_sock.listen()
        server_sock.accept(timeout = 30)
        data_index = 0
        while data_index < len(TRANSFER_DATA):
          chunk_size = min(len(TRANSFER_DATA) - data_index, TRANSFER_CHUNK_SIZE)
          chunk = TRANSFER_DATA[data_index : data_index + chunk_size]
          server_sock.send(chunk)
          data_index = data_index + chunk_size
          print data_index, ' out of ', len(TRANSFER_DATA), 'bytes sent.\r',
        print ''
        time.sleep(0.5)

if __name__ == '__main__':
    main()