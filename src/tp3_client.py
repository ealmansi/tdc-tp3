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
  parser.add_argument('alpha', type=float,
    help = '')
  parser.add_argument('beta', type=float,
    help = '')
  args = vars(parser.parse_args())
  return args

def main():
    if os.geteuid() != 0:
        exit("You need to have root privileges to run this script.\nPlease try again using 'sudo'. Exiting.")

    args = parse_args()
    with ptc.Socket() as client_sock:
        client_sock.connect((SERVER_IP, args.get('port')), timeout = 30)
        client_sock.protocol.set_rto_estimation_parameters(args.get('alpha'), args.get('beta'))
        data_index = 0
        while data_index < len(TRANSFER_DATA):
          chunk_size = min(len(TRANSFER_DATA) - data_index, TRANSFER_CHUNK_SIZE)
          chunk = TRANSFER_DATA[data_index : data_index + chunk_size]
          client_sock.send(chunk)
          data_index = data_index + chunk_size

if __name__ == '__main__':
    main()