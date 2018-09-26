#!/bin/sh

if [-e "comida.csv"]
then
    rm comida.csv
    rm reputacao.csv
    rm recompensa.csv
fi

touch comida.csv
touch reputacao.csv
touch recompensa.csv

pypy simulador.py