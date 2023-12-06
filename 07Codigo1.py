#Complexidade 0(n log n)
def quadradoDosNumerosPassadosNoVetor(vetor):
    return sorted(x**2 for x in vetor)

vetor = [-8, 11, 0, 3, 10]
print("Vetor passado: ", vetor)
print("O quadrado dos numeros do vetor passado ordenado: ")
print(quadradoDosNumerosPassadosNoVetor(vetor))  
