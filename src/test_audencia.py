from audiencia import *

def test_leer_audencia_gh(audiencia:list[Audiencia]):
    print('\n------------------------')
    print('Audiencia de Gran Hermano')
    print('------------------------')
    print(audiencia[:20])

def test_leer_audencia_mc(audiencia:list[Audiencia]):
    print('\n------------------------')
    print('Audiencia de Master Chef')
    print('------------------------')
    print(audiencia[:20])


if __name__ == '__main__':
    
    audiencias_gh = leer_audiencia('./data/GH.csv')
    audiencias_mc = leer_audiencia('./data/MasterChef.csv')

    test_leer_audencia_gh(audiencias_gh)
    test_leer_audencia_mc(audiencias_mc)



