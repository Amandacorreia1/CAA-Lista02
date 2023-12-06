def decompor_vetor(S, piv, p, r):
    q1 = p - 1
    q2 = p - 1
    for j in range(p, r+1):
        if S[j] < piv:
            q1 += 1
            q2 += 1
            S[q1], S[j] = S[j], S[q1]
            if q1 != q2:
                S[q2], S[j] = S[j], S[q2]
        elif S[j] == piv:
            q2 += 1
            S[q2], S[j] = S[j], S[q2]
    return q1, q2


S = [9, 12, 3, 5, 7, 10, 11, 8, 6]
piv = 6
p = 0
r = len(S) - 1
q1, q2 = decompor_vetor(S, piv, p, r)
print("Vetor:", S) 
print("Os indices dos numeros que separam o vetor em tres subvetores: ")
print("q1:", q1)  
print("q2:", q2) 
