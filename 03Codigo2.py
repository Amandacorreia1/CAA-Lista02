#Complexidade 0(n log n)
def soma(nums, X):
    nums = sorted([(num, i) for i, num in enumerate(nums)])
    esquerda, direita = 0, len(nums) - 1
    while esquerda < direita:
        soma = nums[esquerda][0] + nums[direita][0]
        if soma == X:
            return [nums[esquerda][1], nums[direita][1]]
        elif soma < X:
            esquerda += 1
        else:
            direita -= 1
    return []

print("\tOs indices dos numeros somados que da igual ao valor definido no X: ")
nums = [1, 7, 56, 19]
X = 20
print(soma(nums, X)) 
