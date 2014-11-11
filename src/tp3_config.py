#!/usr/bin/env python
# -*- coding: utf-8 -*-

SERVER_IP = '127.0.0.1'
SERVER_PORT = 6677
TRANSFER_DATA = 'abcdefghijklmnopqrstuvxyz' * 1000
TRANSFER_CHUNK_SIZE = 100

TEST_RTO_PARAMS = \
  [(0.125, 0.25),
  (0.300, 0.25),
  (0.425, 0.25),
  (0.125, 0.25),
  (0.125, 0.50),
  (0.125, 0.75),
]