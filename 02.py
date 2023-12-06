def multiplicar_matrizes(A, B):
    tamanho = len(A)

    C = [[0 for _ in range(tamanho)] for _ in range(tamanho)]

    if tamanho == 1:
        C[0][0] = A[0][0] * B[0][0]
    else:
        tamanho //= 3
        A11, A12, A13, A21, A22, A23, A31, A32, A33 = dividir(A, tamanho)
        B11, B12, B13, B21, B22, B23, B31, B32, B33 = dividir(B, tamanho)
        
        C11 = soma_matrizes(multiplicar_matrizes(A11, B11), multiplicar_matrizes(A12, B21), multiplicar_matrizes(A13, B31))
        C12 = soma_matrizes(multiplicar_matrizes(A11, B12), multiplicar_matrizes(A12, B22), multiplicar_matrizes(A13, B32))
        C13 = soma_matrizes(multiplicar_matrizes(A11, B13), multiplicar_matrizes(A12, B23), multiplicar_matrizes(A13, B33))
        C21 = soma_matrizes(multiplicar_matrizes(A21, B11), multiplicar_matrizes(A22, B21), multiplicar_matrizes(A23, B31))
        C22 = soma_matrizes(multiplicar_matrizes(A21, B12), multiplicar_matrizes(A22, B22), multiplicar_matrizes(A23, B32))
        C23 = soma_matrizes(multiplicar_matrizes(A21, B13), multiplicar_matrizes(A22, B23), multiplicar_matrizes(A23, B33))
        C31 = soma_matrizes(multiplicar_matrizes(A31, B11), multiplicar_matrizes(A32, B21), multiplicar_matrizes(A33, B31))
        C32 = soma_matrizes(multiplicar_matrizes(A31, B12), multiplicar_matrizes(A32, B22), multiplicar_matrizes(A33, B32))
        C33 = soma_matrizes(multiplicar_matrizes(A31, B13), multiplicar_matrizes(A32, B23), multiplicar_matrizes(A33, B33))
        
        C = unir_matrizes(C11, C12, C13, C21, C22, C23, C31, C32, C33, tamanho)

    return C

def soma_matrizes(A, B, C):
    return [[A[i][j] + B[i][j] + C[i][j] for j in range(len(A))] for i in range(len(A))]


def extrair_submatriz(M, linha_inicio, linha_fim, coluna_inicio, coluna_fim):
    return [[M[i][j] for j in range(coluna_inicio, coluna_fim)] for i in range(linha_inicio, linha_fim)]

def dividir(M, tamanho):
    t2 = 2 * tamanho
    t3 = 3 * tamanho
    
    M11 = extrair_submatriz(M, 0, tamanho, 0, tamanho)
    M12 = extrair_submatriz(M, 0, tamanho, tamanho, t2)
    M13 = extrair_submatriz(M, 0, tamanho, t2, t3)
    
    M21 = extrair_submatriz(M, tamanho, t2, 0, tamanho)
    M22 = extrair_submatriz(M, tamanho, t2, tamanho, t2)
    M23 = extrair_submatriz(M, tamanho, t2, t2, t3)
    
    M31 = extrair_submatriz(M, t2, t3, 0, tamanho)
    M32 = extrair_submatriz(M, t2, t3, tamanho, t2)
    M33 = extrair_submatriz(M, t2, t3, t2, t3)
    
    return M11, M12, M13, M21, M22, M23, M31, M32, M33

def unir_matrizes(M11, M12, M13, M21, M22, M23, M31, M32, M33, tamanho):
    tam = 3 * tamanho
    M = [[0 for _ in range(tam)] for _ in range(tam)]

    for i in range(tamanho):
        for j in range(tamanho):
            M[i][j] = M11[i][j]
            M[i][j + tamanho] = M12[i][j]
            M[i][j + 2 * tamanho] = M13[i][j]
            M[i + tamanho][j] = M21[i][j]
            M[i + tamanho][j + tamanho] = M22[i][j]
            M[i + tamanho][j + 2 * tamanho] = M23[i][j]
            M[i + 2 * tamanho][j] = M31[i][j]
            M[i + 2 * tamanho][j + tamanho] = M32[i][j]
            M[i + 2 * tamanho][j + 2 * tamanho] = M33[i][j]
    return M


def imprimir_matriz(matriz, nome_matriz):
    print(f"\nMatriz {nome_matriz}:")
    for linha in matriz:
        print(linha)

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

matrizFinal = multiplicar_matrizes(A, B)

imprimir_matriz(A, "A")
imprimir_matriz(B, "B")
imprimir_matriz(matrizFinal, "C produto de A x B")
