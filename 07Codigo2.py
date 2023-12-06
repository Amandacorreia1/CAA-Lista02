#Complexidade 0(n)
def quadradoDosNumeros(n):
    v = len(n)
    resultado = [0] * v
    esquerda, direita = 0, v - 1
    for i in range(v - 1, -1, -1):
        if abs(n[esquerda]) > abs(n[direita]):
            resultado[i] = n[esquerda] ** 2
            esquerda += 1
        else:
            resultado[i] = n[direita] ** 2
            direita -= 1
    return resultado

n = [-8, 10, 0, -3, 69]
print("Vetor passado: ", n)
print("O quadrado dos numeros do vetor passado ordenado: ", quadradoDosNumeros(n))  
