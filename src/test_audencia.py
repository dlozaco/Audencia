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
    audiencias_gh_123 = filtrar_ediciones(audiencias_gh, [1, 2, 3])
    print("Audiencias de las tres primeras ediciones del programa Gran Hermano:")
    print(audiencias_gh_123)

if __name__ == '__main__':

    audiencias_gh = leer_audiencia('./data/GH.csv')
    audiencias_mc = leer_audiencia('./data/MasterChef.csv')

    # test_leer_audencia_gh(audiencias_gh)
    # test_leer_audencia_mc(audiencias_mc)
    # test_calcula_ediciones_gh(audiencias_gh)
    # test_calcula_ediciones_mc(audiencias_mc)
    test_filtrar_ediciones_gh(audiencias_gh)



