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
  print len(datos)
 # losdatos = []
 # for i in range(6):
 #   losdatos.append(datos[0])
 #   losdatos.append(datos[1])
    
 # datos = losdatos
 # print len(datos)
  labels = []
  for delay in ['01','025']:
    for delayvar in ['2', '5']:
      for droprate in [ '0', '25', '50']:
        labels.append('d'+ delay +'var'+ delayvar +'drop'+ droprate)
        labels.append('d'+ delay +'var'+ delayvar +'drop'+ droprate)
   
  for i in range(len(datos)):
    if (i % 2 == 0):     
      plot_alfa(datos[i],labels[i])
    else:  
      plot_beta(datos[i],labels[i])
      
  # filtrar_basura(datos)

def parse_args():
  parser = argparse.ArgumentParser(description='Tp3.')
  parser.add_argument('datafile', type=str)
  args = vars(parser.parse_args())
  return args

def leer_entrada(args):
  experimentos = []
  datos = []
  datos_por_experimento = []
  i = -1
  with open(args.get('datafile')) as f:
    for line in f:
      if i == -1:
        cant_casos = int(line)
        i+=1
        continue
      if not re.match('^\s*#', line):
        if line == '\n':
          datos.append(datos_por_experimento)
          datos_por_experimento = []
          if i % cant_casos == cant_casos-1:
            experimentos.append(datos)
            datos = []
          i+=1
          continue
        if datos_por_experimento == []:
          pieces = line.split()
          datos_por_experimento.append((float(pieces[0].strip()),float(pieces[1].strip()),float(pieces[2].strip()),float(pieces[3].strip()),float(pieces[4].strip())))
          datos_por_experimento.append([])
          continue
        pieces = line.split()
        sampled, rtt = float(pieces[0].strip()), float(pieces[1].strip())
        datos_por_experimento[1].append((sampled,rtt))
  return experimentos

# def filtar_basura(datos):
#   for i in range(1,len(datos)):
#     sampled, rtt = datos[i]
def plot_alfa(muestras,name):
  f = plt.figure()
  labels = [str(e[0][0]) for e in muestras]
  for i in range(len(muestras)):
    sampleds = [sampled/rto for (sampled, rto) in muestras[i][1]]
    #rtos = [rto for (sampled, rto) in muestras[i][1]]
    plt.plot(range(1, len(sampleds)-1),sampleds[1:len(sampleds)-1],label=labels[i])

    
  plt.title("Relacion Sample/RTO para distintos Alpha", fontsize=18)
  plt.ylabel("Sampled/RTO", fontsize=18)
  plt.legend()
  #plt.legend(handler_map=()
  #plt.show()
  f.savefig('../graficos/alpha'+name)
  
def plot_beta(muestras,name=''):
  f = plt.figure()
  labels = [str(e[0][1]) for e in muestras]
  for i in range(len(muestras)):
    sampleds = [sampled/rto for (sampled, rto) in muestras[i][1]]
    #rtos = [rto for (sampled, rto) in muestras[i][1]]
    plt.plot(range(1, len(sampleds)-1),sampleds[1:len(sampleds)-1],label=labels[i])

    
  plt.title("Relacion Sample/RTO para distintos Beta", fontsize=18)
  plt.ylabel("Sampled/RTO", fontsize=18)
  plt.legend()
  #plt.legend(handler_map=()
  #plt.show()
  f.savefig('../graficos/beta'+name)


if __name__ == '__main__':
  main()
