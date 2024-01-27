print("Bienvenido al sistema de edicion de libros en formato papel y digital: ")
print("1.Calcular extension de un libro \n")
print("2.Calcular costo de edicion de un libro formato papel \n")
print("3.Calculadora de cantidad de bytes \n")
print("4.Calcular costo de edicion de un libro formato digital \n")
print("0.Finalizar \n")

operacion = int(input("Ingrese algun numero para hacer alguna operacion: "))

if operacion == 1:
    import calcular_Extension as extension
elif operacion == 2:
    import calcular_Costo_Edicion as costoEdicion
elif operacion == 3:
    import calcular_Cantidad_de_Bytes as cantidadBytes
elif operacion == 4:
    import calcular_Costo_de_Edicion_Digital as costoEdicionDigital
elif operacion == 0:
    print("Gracias por utilizar nuestro programa!")
else:
    print("Error, ingrese un valor entre 0 y 5.")