import csv
import statistics
from collections import namedtuple
from matplotlib import pyplot as plt

Audiencia = namedtuple('Audiencia', 'edicion, share')

def leer_audiencia(archivo)->list[Audiencia]:
    audiencia = list()

    with open(archivo, 'rt', encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=',')
        for edicion, share in lector:
            audiencia.append(Audiencia(int(edicion), float(share)))
    
    return audiencia

def calcula_ediciones(archivo:list[Audiencia])->int:
    ediciones = set()
    for edicion, share in archivo:
        ediciones.add(edicion)
    
    return len(ediciones)

def filtrar_ediciones(archivo:list[Audiencia], e:int)->list:
    e_list = list()
    for edicion, share in archivo:
        if edicion in e:
            e_list.append(Audiencia(int(edicion), float(share)))

    return e_list


