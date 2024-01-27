def calcular_Extension(cantidadDeCaracteres:int)->str:
    if(cantidadDeCaracteres > 1000000):
        return "Largo"
    elif(cantidadDeCaracteres < 150000):
        return "Breve"
    else:
        return "Normal"
    
def calcular_Costo_Edicion(costo:int,cantidadDeCaracteres:int)->int:
    if(calcular_Extension(cantidadDeCaracteres) == "Normal"):
        return costo
    elif(calcular_Extension(cantidadDeCaracteres) == "Largo"):
        return costo*2
    elif(calcular_Extension(cantidadDeCaracteres) == "Breve"):
        return round(costo/2)

def calcular_Costo_de_Edicion_Digital(costo:int)->int:
    return costo*10

def calcular_Cantidad_de_Bytes(cantidadDeCaracteres:int,cantidadDeIlustraciones:int)->int:
    return cantidadDeCaracteres + (cantidadDeIlustraciones * 1000)

