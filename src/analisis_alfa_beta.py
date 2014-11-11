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
  plot_alfa_beta(datos)
  # filtrar_basura(datos)

def parse_args():
  parser = argparse.ArgumentParser(description='Tp3.')
  parser.add_argument('datafile', type=str)
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
        sampled, rtt = float(pieces[0].strip()), float(pieces[1].strip())
        datos_por_alfa_beta.append((sampled,rtt))
  return datos

# def filtar_basura(datos):
#   for i in range(1,len(datos)):
#     sampled, rtt = datos[i]

def plot_alfa_beta(muestras):
  f = plt.figure()

  for i in range(len(muestras)):
    alfa, beta = muestras[i][0]
    sampleds = [sampled for (sampled, rto) in muestras[i]]
    rtos = [rto for (sampled, rto) in muestras[i]]
    for j in range(1, len(sampleds)):
      plt.plot(rtos[j] / sampleds[j],'rx',markersize=30)

      if(i == 4 or i == len(muestras) - 1):
        plt.title("ALPHA O BETA" + str(i), fontsize=18)
        plt.ylabel("Tiempo (ms)", fontsize=18)
        plt.show()
        f.savefig('alpha' + str(i))
        f = plt.figure()

if __name__ == '__main__':
  main()