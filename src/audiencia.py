import csv
import statistics
from collections import namedtuple
from matplotlib import pyplot as plt

Audiencia = namedtuple('Audiencia', 'edicion, share')

def leer_audiencia(archivo):
    audiencia = list()

    with open(archivo, 'rt', encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=',')
        for edicion, share in lector:
            audiencia.append(Audiencia(int(edicion), float(share)))
    
    return audiencia


