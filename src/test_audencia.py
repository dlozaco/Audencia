from audiencia import *

def test_leer_audencia_gh(audiencia:list[Audiencia]):
    print('\n------------------------')
    print('Audiencia de Gran Hermano')
    print('------------------------')
    print(audiencia[:20])

def test_leer_audencia_mc(audiencia:list[Audiencia]):
    print('\n------------------------')
    print('Audiencia de MasterChef')
    print('------------------------')
    print(audiencia[:20])

def test_calcula_ediciones_gh(audiencia:list[Audiencia]):
    ediciones_gh = calcula_ediciones(audiencia)
    print(f'\nNumero de ediciones de Gran Hermano: {ediciones_gh}')

def test_calcula_ediciones_mc(audiencia:list[Audiencia]):
    ediciones_mc = calcula_ediciones(audiencia)
    print(f'Numero de ediciones de MasterChef: {ediciones_mc}')

def test_filtrar_ediciones_gh(audiencia:list[Audiencia]):
    audiencias_gh_123 = filtrar_ediciones(audiencia, [1, 2, 3])
    print("Audiencias de las tres primeras ediciones del programa Gran Hermano:")
    print(audiencias_gh_123)

def test_filtrar_ediciones_mc(audiencia:list[Audiencia]):
    audiencias_mc_123 = filtrar_ediciones(audiencia, [1, 2, 3])
    print("\nAudiencias de las tres primeras ediciones del programa MasterChef:")
    print(audiencias_mc_123)

def test_agrupa_por_ediciones_gh(edicion:dict):
    d_gh = agrupa_por_ediciones(edicion)
    print("Agrupación por ediciones de las audiencias del programa Gran Hermano:")
    print(d_gh)

def test_agrupa_por_ediciones_mc(edicion:dict):
    d_gh = agrupa_por_ediciones(edicion)
    print("\nAgrupación por ediciones de las audiencias del programa MasterChef:")
    print(d_gh)

def test_media_por_ediciones_gh(archivo:list[Audiencia]):
    media_gh = media_por_ediciones(archivo)
    print("Media de audiencias por ediciones del programa Gran Hermano:")
    print(media_gh)

def test_media_por_ediciones_mc(archivo:list[Audiencia]):
    media_mc = media_por_ediciones(archivo)
    print("\nMedia de audiencias por ediciones del programa MasterChef:")
    print(media_mc)

if __name__ == '__main__':

    audiencias_gh = leer_audiencia('./data/GH.csv')
    audiencias_mc = leer_audiencia('./data/MasterChef.csv')
    
    # test_leer_audencia_gh(audiencias_gh)
    # test_leer_audencia_mc(audiencias_mc)
    # test_calcula_ediciones_gh(audiencias_gh)
    # test_calcula_ediciones_mc(audiencias_mc)
    # test_filtrar_ediciones_gh(audiencias_gh)
    # test_filtrar_ediciones_mc(audiencias_mc)
    # test_agrupa_por_ediciones_gh(audiencias_gh)
    # test_agrupa_por_ediciones_mc(audiencias_mc)
    test_media_por_ediciones_gh(audiencias_gh)
    test_media_por_ediciones_mc(audiencias_mc)



