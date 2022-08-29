listaEst= []
resp= "si"
while (resp.upper!="no"):
    tam =len(listaEst)
    print("Elementos guardados: ",tam)
    nombres= input("Escribe el nombre del estudiante: ")
    listaEst.append(nombres)
    resp=input("\nDesea agregar mas? Si-No:")

    for est in listaEst:
        print(est)
