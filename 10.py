def buscaBinaria(num, alvo):
    es, di = 0, len(num) - 1
    while es <= di:
        meio = (es + di) // 2
        if num[meio] == alvo:
            return meio
        elif num[meio] < alvo:
            es = meio + 1
        else:
            di = meio - 1
    return es

num = [0, 6, 5 ,89 ,75]
print("Vetor passadp: ", num)
alvo = 89
print("O numero alvo que voce deseja saber a sua posicao no vetor ordenado: ", alvo)
print("O índice onde esta o alvo dentro do vetor passado." ,buscaBinaria(num, alvo))  
