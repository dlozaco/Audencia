import csv
import statistics
from collections import namedtuple
from matplotlib import pyplot as plt

Audiencia = namedtuple('Audiencia', 'edicion, share')

def leer_audiencia(archivo:str)->list[Audiencia]:
    audiencia = list()

    with open(archivo, 'rt', encoding='utf-8') as f:
        lector = csv.reader(f, delimiter=',')
        for edicion, share in lector:
            audiencia.append(Audiencia(int(edicion), float(share)))
    
    return audiencia

def calcula_ediciones(archivo:str)->int:
    
    ediciones = set()
    for edicion, share in archivo:
        ediciones.add(edicion)
    
    return len(ediciones)

def filtrar_ediciones(archivo:str, e:int)->list:#e de edicion
    res = list()
    for edicion, share in archivo:
        if edicion in e:
            res.append((int(edicion), float(share)))

    return res

def agrupa_por_ediciones(archivo:str):
    res = dict()
    for edicion, share in archivo:
        if edicion in res:
            res[edicion].append(share)
        else:
            res[edicion] = [share]
    return res

def media_por_ediciones(archivo:str)->list[Audiencia]:
    medias = dict()
    lista = agrupa_por_ediciones(archivo)
    for edicion, lista_shares in lista.items():
        medias[edicion] = sum(lista_shares)/len(lista_shares)
    return medias


