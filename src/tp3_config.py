#!/usr/bin/env python
# -*- coding: utf-8 -*-

SERVER_IP = '127.0.0.1'
SERVER_PORT = 6677
TRANSFER_DATA = 'abcdefghijklmnopqrstuvxyz' * 1000
TRANSFER_CHUNK_SIZE = 100

TEST_RTO_PARAMS = \
  [(0, 0.25),
  (0.125, 0.25),
  (0.4, 0.25),
  (0.8, 0.25),
  (1, 0.25),
  (0.125,0),
  (0.125, 0.25),
  (0.125, 0.5),
  (0.125, 0.8),
  (0.125, 1)
]