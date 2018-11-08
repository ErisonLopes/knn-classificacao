""" 
    Implementação do KNN
    Dataset: https://archive.ics.uci.edu/ml/datasets/Haberman's+Survival
    Descrição do Dataset: Sobrevivencia de pacientes submetidos a cirurgia de cancer de mama
"""
import math
from dist_euclidiana import dist_euclidiana

#Amostras
amostras = []

with open('haberman.data', 'r') as f:
    for linha in f.readlines():
        atrib = linha.replace('\n', '').split(',')
        amostras.append([
            int(atrib[0]), 
            int(atrib[1]),
            int(atrib[2]),
            int(atrib[3])
        ])

def info_dataset(amostras, verbose=True):
    if verbose:
        print('Total de amostras: %d' % len(amostras))
    rotulo1,rotulo2 = 0, 0
    for amostra in amostras:
        if amostra[-1] == 1:
            rotulo1 += 1
        else:
            rotulo2 += 1
    if verbose:
        print('Total rotulo 1: %d' % rotulo1)
        print('Total rotulo 2: %d' % rotulo2)
    
    return [len(amostras), rotulo1, rotulo2]


p = 0.6
_, rotulo1, rotulo2 = info_dataset(amostras, verbose=False)

treinamento, teste = [], []
max_rotulo1, max_rotulo2 = int(p * rotulo1), int(p * rotulo2)
total_rotulo1, total_rotulo2 = 0, 0
for amostra in amostras:
    if (total_rotulo1 + total_rotulo2) < (max_rotulo1 + max_rotulo2):
        treinamento.append(amostra)
        if amostra[-1] == 1 and total_rotulo1 < max_rotulo1:
            total_rotulo1 += 1
        else: total_rotulo2 += 1
    else:
        teste.append(amostra)

info_dataset(treinamento)

def knn(treinamento, nova_amostra, K):
    dicts, tam_treino = {}, len(treinamento)

    #Calcula a distancia euclidiana da nova amostra
    for i in range(tam_treino):
        d = dist_euclidiana(treinamento[i], nova_amostra)
        dicts[i] = d

    #Obtém a chaves dos k-vizinhos mais próximos
    k_vizinhos = sorted(dicts, key=dicts.get)[:K]

    #Votação Majoritária
    qtde_rotulo1, qtde_rotulo2 = 0, 0
    for i in k_vizinhos:
        if treinamento[i][-1] == 1:
            qtde_rotulo1 += 1
        else:
            qtde_rotulo2 += 1
    if qtde_rotulo1 > qtde_rotulo2:
        return 1
    else:
        return 2

print(teste[0])
print(knn(treinamento, teste[0], K=13))