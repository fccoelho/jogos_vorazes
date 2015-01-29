#coding:utf8

import pylab as P
import numpy as np

def carrega_dados(file_name):
    with open(file_name) as f:
        nomes = f.readline().strip().split(',')

    dados = np.genfromtxt(file_name, delimiter=',', skip_header=1)
    print (nomes, dados.size)

if __name__ == "__main__":
    carrega_dados("comida.csv")