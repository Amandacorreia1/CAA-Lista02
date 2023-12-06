#Complexidade 0(n²)
def soma(n, X):
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            if n[i] + n[j] == X:
                return [i, j]
    return []


print("\tOs indices dos numeros somados que da igual ao valor definido no X: ")
numeros = [3,2,4]
X = 7
print(soma(numeros, X))  
