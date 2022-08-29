#sumar los elementos de un arreglo
arreglo = []
cant = int (input("Dime cuantos #: "))
cont =0
while (cont <cant ) :
    num=int(input("dime un #: "))
    arreglo.append(num)
    cont+=1

    suma =0
    for num in arreglo:
        suma +=num
    print("la suma es :",suma )
