import os
import time
import msvcrt as tecla
from numpy import *
restaurante = zeros((3,3), int)
lnombres = []
lruts = []
lcorreos = []
lfilas = []
lmesas = []
lcantbeb1 = []
lcantbeb2 = []
lcantbeb3 = []
lcantplat1 = []
lcantplat2 = []
lcantplat3 = []
lcantpost1 = []
lcantpost2 = []
lcantpost3 = []
lsubtotal = []
lista_codigos_de_descuento = ["GENSHINGIFT","28092020","EmergencyFood"]
def confirmacion(subtotal:int,precio:int,cantidad:int):
    while True:
        try:
            confirmacion = int(input("¿Está seguro?\n (1. Sí 2. No): "))
            if confirmacion == 1:
                subtotal += (precio * cantidad)
                print("Presione una tecla para continuar...")
                tecla.getch()
                return subtotal
            elif confirmacion == 2:
                return
            else:
                print("¡ERROR!, ¡OPCIÓN FUERA DE RANGO!") 
        except:
            print("¡ERROR! ¡DEBE INGRESAR UN NÚMERO ENTERO!")
def validar_cantidad():
    while True:
        try:
            cantidad = int(input("¿Cuantas desea?: "))
            if cantidad > 0:
                return cantidad
            else:
                print("¡ERROR!, ¡COMPRE AL MENOS UN PRODUCTO!")
        except:
            print("¡ERROR!, ¡DEBE INGRESAR UN NÚMERO ENTERO!")
def vopcion(min:int,max:int):
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
            if opcion >= min and opcion <= max:
                return opcion
            else:
                print("¡ERROR! ¡DEBE INGRESE UNA OPCIÓN VÁLIDA!")
        except:
            print("¡ERROR!, ¡DEBE INGRESAR UN NÚMERO ENTERO!")
def menu():
    print("""Menú
    1. Ver restaurant
    2. Reservar mesa
    3. Carta
    4. Pagar
    5. Cancelar
    6. Salir""")
    opcion = vopcion(1,6)
    return opcion
def ver_restaurant():
    print("\tRESTAURANT\n")   
    print("Capacidad de mesas fila 1: 2 Personas")
    print("Capacidad de mesas fila 2: 4 Personas")
    print("Capacidad de mesas fila 3: 6 Personas\n")
    print(" "*7+" Mesas")     
    print(" "*8+"1 2 3")
    for x in range(3):
        print("Fila",x+1,end=": ")
        for y in range(3):
            print(restaurante[x][y], end=" ")
        print()
    print("\nPresione una tecla para continuar...")
    tecla.getch()
def vrut():
    while True:
        try:
            rut = int(input("Ingrese su RUT sin puntos ni dígito verificador: "))
            if rut > 1000000 and rut < 99999999:
                return rut
            else:
                print("¡ERROR! ¡INGRESE UN RUT VÁLIDO!")
        except:
            print("¡ERROR! ¡DEBE INGRESAR UN NÚMERO ENTERO!")
def vnombre():
    while True:
        nombre = input("Ingrese su nombre: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha():
            return nombre
        else:
            print("¡ERROR! ¡EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")
def vcorreo():
    while True:
        correo = input("Ingrese su correo: ")
        if "@" in correo:
            return correo
        else:
            print("¡ERROR! ¡INGRESE UN CORREO VÁLIDO!")
def vpersonas(min:int,max:int):
    while True:
        try:
            personas = int(input("¿Cuantas personas van a asistir?: "))
            if personas >= min and personas <= max:
                return personas
            else:
                print(f"¡ERROR! ¡DEBEN ASISTIR ENTRE ({min}) HASTA ({max}) PERSONAS!")
        except:
            print("¡ERROR! ¡DEBE INGRESAR UN NÚMERO ENTERO!")
def vfila(min:int,max:int):
    while True:
        try:
            fila = int(input(f"Ingrese número de fila ({min},{max}):"))
            if fila >= min and fila <= max:
                return fila
            else:
                print("ERROR! FILA INCORRECTA")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO POSITIVO!")
def vmesa(min:int,max:int):
    while True:
        try:
            mesa = int(input(f"Ingrese número de mesa ({min},{max}): "))
            if mesa >= min and mesa <= max:
                return mesa
            else:
                print("ERROR! FILA INCORRECTA")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO POSITIVO!")
def mesas_disponibles(min_range:int,max_range:int,min_fila:int,max_fila:int):
    while True:
        print("Estas son las mesas disponibles: ")
        print(" "*1+" Mesas")
        print(" "*8+"1 2 3")
        for x in range(min_range,max_range):
            print("Fila",x+1,end=": ")
            for y in range(3):
                print(restaurante[x][y], end=" ")
            print()
        print("\nPresione una tecla para continuar...")
        tecla.getch()
        fila = vfila(min_fila,max_fila)
        mesa = vmesa(1,3)
        if restaurante[fila-1][mesa-1] == 0:
            restaurante[fila-1][mesa-1] = 1
            print("Mesa reservada con exito!")
            lfilas.append(fila)
            lmesas.append(mesa)
            time.sleep(3)
            return
        else:
            print("Mesa ocupada! escoja otra.")
def reservacion():
    rut = vrut()
    nombre = vnombre()
    correo = vcorreo()
    personas = vpersonas(1,6)
    if personas == 1 or personas == 2:
        mesas_disponibles(0,3,1,3)
    elif personas == 3 or personas == 4:
        mesas_disponibles(1,3,2,3)
    else:
        mesas_disponibles(2,3,3,3)
    lruts.append(rut)
    lnombres.append(nombre)
    lcorreos.append(correo)
def carta():
    print("1. Bebestibles")
    print("2. Platos")
    print("3. Postres")
    print("4. Pedir")
    print("5. Cancelar")
    opcion = vopcion(1,5)
    return opcion
def validarbeb(min:int,max:int):
    while True:
        try:
            bebestible = int(input("¿Qué bebestible desea?: "))
            if bebestible >= min and bebestible <= max:
                return bebestible
        except:
            print("¡ERROR! ¡INGRESE UN NÚMERO ENTERO!")
def menubebestible():
    print("\tBEBESTIBLES\n")
    print("1. Margarita Arcoíris ($2.990)")
    print("2. Té De Menta Afrutado ($1.990)")
    print("3. Jugo Festivo ($3.990)")
    print("4. Volver atras")
    bebestible = validarbeb(1,4)
    return bebestible
def validarplatos(min:int,max:int):
    while True:
        try:
            plato = int(input("¿Qué plato desea?: "))
            if plato >= min and plato <= max:
                return plato
        except:
            print("¡ERROR! ¡INGRESE UN NÚMERO ENTERO!")
def menuplatos():
        print("\tPLATOS\n")
        print("1. Sushi De Huevo Especial ($12.500)")
        print("2. Tentación De Adeptus ($34.990)")
        print("3. Surtido De Sashimi ($23.990)")
        print("4. Volver atras")
        plato = validarplatos(1,4)
        return plato
def validarpostre(min:int,max:int):
    while True:
        try:
            postre = int(input("¿Qué postre desea?: "))
            if postre >= min and postre <= max:
                return postre
        except:
            print("¡ERROR! ¡INGRESE UN NÚMERO ENTERO!")
def menupostres():
    print("\tPOSTRES\n")
    print("1. Gelatina De Menta ($5.990)")
    print("2. Pudín De Orquídia Padishá ($4.990)")
    print("3. Natillas De Rosa ($7.990)")
    print("4. Volver atras")
    postre = validarpostre(1,4)
    return postre
def vcancelar():
    while True:
        try:
            cancelar = int(input("¿Está seguro que desea cancelar la compra?\n (1. Sí 2. No)\n"))
            if cancelar in (1,2):
                return cancelar
            else:
                print("¡ERROR!, ¡OPCIÓN FUERA DE RANGO!")
        except:
            print("¡ERROR!, ¡DEBE INGRESAR UN NÚMERO ENTERO!")
def validar_descuento():
    while True:
        tiene_descuento = input("Tiene descuento? (SI/NO): ")
        if tiene_descuento.upper() == "SI":
            cod_descuento = input("Ingrese su codigo de descuento: ")
            if cod_descuento in lista_codigos_de_descuento:
                return True
            else:
                print("Su codigo no se encuentra en nuestros registros...")
                time.sleep(2)
        elif tiene_descuento.upper() == "NO":
            return
        else:
            print("Ingrese una opción valida entre (SI O NO)!!!")
def boleta(subtotal:int):
    iva = subtotal * 0.19
    vdescuento = validar_descuento()
    if vdescuento == True:
        descuento = subtotal * 0.20
        total = (subtotal+iva) - descuento
    else:
        descuento = 0
        total = subtotal+iva
    print(f"""\tBOLETA: 
    SUBTOTAL:      ${subtotal}
    IVA(19%):      ${iva}
    DESCUENTO:     ${descuento}
    TOTAL:         ${total}""")
    print("\n Gracias por su visita!")
    print("\n Presione una tecla para continuar...")
    tecla.getch()