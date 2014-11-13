#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import ptc
from tp3_config import SERVER_IP, SERVER_PORT, TRANSFER_DATA, TRANSFER_CHUNK_SIZE
import time
import argparse

def parse_args():
  parser = argparse.ArgumentParser(description='.',
    epilog='')
  parser.add_argument('port', type=int,
    help = '')
  parser.add_argument('drop-rate', type=float,
    help = '')
  parser.add_argument('delay', type=float,
    help = '')
  parser.add_argument('delay-var', type=float,
    help = '')
  args = vars(parser.parse_args())
  return args

def main():
    if os.geteuid() != 0:
        exit("You need to have root privileges to run this script.\nPlease try again using 'sudo'. Exiting.")

    args = parse_args()
    with ptc.Socket() as server_sock:
        server_sock.bind((SERVER_IP, args.get('port')))
        server_sock.listen()
        server_sock.accept(timeout = 30)
        server_sock.protocol.set_ack_drop_rate(args.get('drop-rate'))
        server_sock.protocol.set_ack_delay(args.get('delay'), args.get('delay-var'))
        data_received = ''
        while len(data_received) < len(TRANSFER_DATA):
          data_received += server_sock.recv(TRANSFER_CHUNK_SIZE)

if __name__ == '__main__':
    main()