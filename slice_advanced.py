def slice_advanced():
    palabra = input("ingresar una palabra de mas de 5 caracteres   (puede contener numeros y simbolos): ")
    i = 6
    longitud = len (palabra)
    if longitud > 5:
        output = palabra[4]
        while (i<longitud):
            output = output + palabra[i]
            i = i + 2
        print(output)
    else:
        print("error")
