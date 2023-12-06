def mesclarVetor(nums1, m, nums2, n):
    
    for i in range(n):
        nums1[m + i] = nums2[i]
   
    nums1.sort()

# Exemplo da questao 
#Entrada:
#nums1 = [1,2,3,0,0,0], m = 3,
#nums2 = [2,5,6], n = 3
#Saída: [1,2,2,3,5,6]

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
mesclarVetor(nums1, m, nums2, n)
print("Os vetorse mesclados",nums1)  
