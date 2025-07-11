def slice_simple():
    texto = "Awesome"
    longitud = len(texto)
    InicioTresLetras =int(longitud/2) - 1
    FinalTresLetras = InicioTresLetras + 3
    Antepenultima = longitud - 3
    print(texto[0:3].lower())
    print(texto[InicioTresLetras:FinalTresLetras].lower())
    print(f"{texto[0:4].lower()}{texto[Antepenultima:longitud].lower()}")
