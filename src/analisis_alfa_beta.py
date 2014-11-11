#!/usr/bin/env python

import numpy #para zscore
import matplotlib.pyplot as plt
import sys
import argparse
import re
import os

def main():
	args = parse_args()
	datos = leer_entrada(args)

def parse_args():
  parser = argparse.ArgumentParser(description='Tp3.')
  parser.add_argument('datafile', type=str,
    help = 'data file path')
  args = vars(parser.parse_args())
  return args

def leer_entrada(args):
  datos = []
  datos_por_alfa_beta = []
  i = 1
  with open(args.get('datafile')) as f:
    for line in f:
      if not re.match('^\s*#', line):
        if line == '\n':
          datos.append(datos_por_alfa_beta)
          datos_por_alfa_beta = []
          continue
        pieces = line.split()
        sampled, rtt = int(pieces[0].strip()), int(pieces[1].strip())
        datos_por_alfa_beta.append((sampled,rtt))
  return datos


if __name__ == '__main__':
  main()