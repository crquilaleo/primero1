def opcion():
    opci=int(input("Selecciona una opcion segun su numero.\n1.Grabar.\n2.Buscar.\n3.Imprimir.\n4.Salir.\n:"))
    if opci==1 or opci==2 or opci==3 or opci==4:
        if opci ==1:
            grabar()
        if opci ==2:
            buscar()
        if opci ==3:
            imprimir()
        if opci==4:
            salir()
    else:
        print("Ingresa una opcion valida.")
        return opcion()
vehiculos={}
def grabar():
    tipo=input("Ingrese el tipo de vehiculo\n:")
    patente=input("Ingrese la patente\n:")
    while True:
        marca=input("Ingrese la marca\n:")
        if len(marca)<6:
            print("El nombre es muy corto, intentelo de nuevo")
        else:
            break
    while True:
        precio=int(input("Ingrese el precio\n:"))
        if precio<5000000:
            print("El precio es muy bajo intentalo de nuevo")
        else:
            break
    multa=int(input("Ingrese el valor de la multa\n:"))
    an_vigentes=input("Ingresa el precio de las anotaciones vigentes\n:")
    fecha_multa=input("Ingrese fecha de la multa\n:")
    fecha_registro=input("Ingrese la fecha del registro del vehiculo\n:")
    nombre=input("Ingresa el nombre y apellido del dueño\n:")
    vehiculos[patente]={
        "TIPO" : tipo,
        "PATENTE": patente,
        "MARCA": marca,
        "PRECIO":precio,
        "MULTA": multa,
        "ANOTACIONES_VIGENTES" : an_vigentes,
        "FECHA_MULTA" : fecha_multa,
        "FECHA_REGISTRO" :fecha_registro,
        "NOMBRE" : nombre
    }
    print("Se ha grabado")
    print(vehiculos)
    con=int(input("¿Quiere hacer algo mas? 1=SI 2=NO\n:"))
    if con ==1:
        print("Perfecto")
        opcion()
    else:
        print("Adios")    
def buscar():
    patente=input("Ingrese la patente para buscar los datos\n:")
    if patente in vehiculos:
        ve=vehiculos[patente]
        print(ve)
    else:
        print("Ingrese una patente registrada")
    con=int(input("¿Quiere hacer algo mas? 1=SI 2=NO\n:"))
    if con ==1:
        print("Perfecto")
        opcion()
    else:
        print("Adios")

def imprimir():
    patente=input("Ingrese el numero de patente para imprimir el cerfificado\n:")
    if patente in vehiculos:
        ve=vehiculos[patente]
        print("CERTIFICADO AUTO SEGURO ")
        print("TIPO:",ve["TIPO"])
        print("PATENTE:",ve["PATENTE"])
        print("MARCA:",ve["MARCA"])
        print("PRECIO:",ve["PRECIO"])
        print("MULTA:",ve["MULTA"])
        print("ANOTACIONES_VIGENTES",ve["ANOTACIONES_VIGENTES"])
        print("FECHA_MULTA:",ve["FECHA_MULTA"])
        print("FECHA_REGISTRO",ve["FECHA_REGISTRO"])
        print("NOMBRE:",ve["NOMBRE"])
    else:
        print("La patente es incorrecta, intentelo de nuevo")
    con=int(input("¿Quiere hacer algo mas? 1=SI 2=NO\n:"))
    if con ==1:
        print("Perfecto")
        opcion()
    else:
        print("Adios") 
def salir():
    con=int(input("¿Esta seguro de que quiere salir? 1=SI 2=NO\n:"))
    if con ==1:
        print("Hasta luego")
    else:
        print("Redirigiendo...")
        opcion()
opcion()