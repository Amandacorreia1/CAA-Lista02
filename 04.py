def majoritario(num):
    cont = 0
    c = None

    for num in num:
        if cont == 0:
            c = num
        cont += (1 if num == c else -1)

    return c

num = [2,2,1,1,1,2,2,1,1,1,3,3,4,4,4,4,4,4,4,4,4,4,5]
print("\t\t\tO numero majoritario eh: ",majoritario(num))
