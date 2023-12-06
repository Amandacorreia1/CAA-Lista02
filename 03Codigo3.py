#Complexidade 0(n).
def soma(n, X):
    dict_numeros = {}
    for i, num in enumerate(n):
        complemento = X - num
        if complemento in dict_numeros:
            return [dict_numeros[complemento], i]
        dict_numeros[num] = i
    return []

print("\tOs indices dos numeros somados que da igual ao valor definido no X: ")
numeros = [2,8,14,25]
X = 27
print(soma(numeros, X))  

