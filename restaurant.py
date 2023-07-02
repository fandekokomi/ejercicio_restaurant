from funciones_restaurant import *
subtotal = 0
precio_margarita_arcoiris = 2990
precio_te_de_menta_afrutado = 1990
precio_jugo_festivo = 3990
precio_sushi_de_huevo_especial = 12500
precio_tentation_de_adeptus = 34990
precio_surtido_de_sashimi = 23990
precio_gelatina_de_menta = 5990
precio_pudin_de_orquidia_padisha = 4990
precio_natillas_de_rosa = 7990
cant_beb_1 = 0
cant_beb_2 = 0
cant_beb_3 = 0
cant_plat_1 = 0
cant_plat_2 = 0
cant_plat_3 = 0
cant_post_1 = 0
cant_post_2 = 0
cant_post_3 = 0
while True:
    os.system("cls")
    opcion = menu()
    if opcion == 1:
        os.system("cls")
        ver_restaurant()
        os.system("cls")
    elif opcion == 2:
        if 0 not in restaurante:
            print("Todas las mesas están llenas, por favor reserve en otro momento...")
            time.sleep(3)
            continue
        os.system("cls")
        reservacion()
        lcantbeb1.append(cant_beb_1)
        lcantbeb2.append(cant_beb_2)
        lcantbeb3.append(cant_beb_3)
        lcantplat1.append(cant_plat_1)
        lcantplat2.append(cant_plat_2)
        lcantplat3.append(cant_plat_3)
        lcantpost1.append(cant_post_1)
        lcantpost2.append(cant_post_2)
        lcantpost3.append(cant_post_3)
        lsubtotal.append(subtotal)
    elif opcion == 3:
        rut = vrut()
        if rut not in lruts:
            print("RUT NO EXISTE!")
            continue
        else:
            for x in range(len(lruts)):
                if rut == lruts[x]:
                    posicion = x
            cant_beb_1 = lcantbeb1[posicion]
            cant_beb_2 = lcantbeb2[posicion]
            cant_beb_3 = lcantbeb3[posicion]
            cant_plat_1 = lcantplat1[posicion]
            cant_plat_2 = lcantplat2[posicion]
            cant_plat_3 = lcantplat3[posicion]
            cant_post_1 = lcantpost1[posicion]
            cant_post_2 = lcantpost2[posicion]
            cant_post_3 = lcantpost3[posicion]
        while True:
            opc_carta = carta()
            if opc_carta == 1:
                while True:
                    bebestible = menubebestible()
                    if bebestible == 1:
                        cant_beb_1 += validar_cantidad()
                        subtotal += confirmacion(subtotal,precio_margarita_arcoiris,cant_beb_1)
                    elif bebestible == 2:
                        cant_beb_2 += validar_cantidad()
                        subtotal += confirmacion(subtotal,precio_te_de_menta_afrutado,cant_beb_1)
                    elif bebestible == 3:
                        cant_beb_3 += validar_cantidad()
                        subtotal += confirmacion(subtotal,precio_jugo_festivo,cant_beb_3)
                    else:
                        break
            elif opc_carta == 2:
                while True:
                    plato = menuplatos()
                    if plato == 1:
                        cant_plat_1 += validar_cantidad()
                        subtotal += confirmacion(subtotal,precio_sushi_de_huevo_especial,cant_plat_1)
                        lcantplat1[posicion] = cant_plat_1
                    elif plato == 2:
                        cant_plat_2 += validar_cantidad()
                        subtotal += confirmacion(subtotal,precio_tentation_de_adeptus,cant_plat_2)
                        lcantplat2[posicion] = cant_plat_2
                    elif plato == 3:
                        cant_plat_3 += validar_cantidad()
                        subtotal += confirmacion(subtotal,precio_surtido_de_sashimi,cant_plat_3)
                        lcantplat3[posicion] = cant_plat_3
                    else:
                        break
            elif opc_carta == 3:
                while True:
                    postre = menupostres()
                    if postre == 1:
                        cant_post_1 += validar_cantidad()
                        subtotal += confirmacion(subtotal,precio_gelatina_de_menta,cant_post_1)
                        lcantpost1[posicion] = cant_post_1
                    elif postre == 2:
                        cant_post_2 += validar_cantidad()
                        subtotal += confirmacion(subtotal,precio_pudin_de_orquidia_padisha,cant_post_2)
                        lcantpost2[posicion] = cant_post_2
                    elif postre == 3:
                        cant_post_3 += validar_cantidad()
                        subtotal += confirmacion(subtotal,precio_natillas_de_rosa,cant_post_3)
                        lcantpost3[posicion] = cant_post_3
                    else:
                        break
            elif opc_carta == 4:
                if cant_beb_1 > 0:
                    print(f"Cantidad de Margarita arcoiris pedido: {cant_beb_1}")
                if cant_beb_2 > 0:
                    print(f"Cantidad de Té de menta afrutado pedido: {cant_beb_2}")
                if cant_beb_3 > 0:
                    print(f"Cantidad de Jugo Festivo pedido: {cant_beb_3}")
                if cant_plat_1 > 0:
                    print(f"Cantidad de Sushi de Huevo Especial pedido: {cant_plat_1}")
                if cant_plat_2 > 0:
                    print(f"Cantidad de Tentación de Adeptus pedido: {cant_plat_2}")
                if cant_plat_3 > 0:
                    print(f"Cantidad de Surtido de Sashimi pedido: {cant_plat_3}")
                if cant_post_1 > 0:
                    print(f"Cantidad de Gelatina de menta pedido: {cant_post_1}")
                if cant_post_2 > 0:
                    print(f"Cantidad de Pudín de Orquídea Padishá pedido: {cant_post_2}")
                if cant_post_3 > 0:
                    print(f"Cantidad de Natillas de Rosa pedido: {cant_post_3}")
                print(f"El monto total de su pedido es ${subtotal}")
                print("Presione una tecla para continuar...")
                tecla.getch()
                lcantbeb1[posicion] = cant_beb_1
                lcantbeb2[posicion] = cant_beb_2
                lcantbeb3[posicion] = cant_beb_3
                lcantplat1[posicion] = cant_plat_1
                lcantplat2[posicion] = cant_plat_2
                lcantplat3[posicion] = cant_plat_3
                lcantpost1[posicion] = cant_post_1
                lcantpost2[posicion] = cant_post_2
                lcantpost3[posicion] = cant_post_3
                lsubtotal[posicion] = subtotal
                break
            else:
                cancelar = vcancelar()
                if cancelar == 1:
                    lcantbeb1[posicion] = 0
                    lcantbeb2[posicion] = 0
                    lcantbeb3[posicion] = 0
                    lcantplat1[posicion] = 0
                    lcantplat2[posicion] = 0
                    lcantplat3[posicion] = 0
                    lcantpost1[posicion] = 0
                    lcantpost2[posicion] = 0
                    lcantpost3[posicion] = 0
                    lsubtotal[posicion] = 0
                    print("Pedido cancelado exitosamente")
                    print("Presione una tecla para continuar...")
                    tecla.getch()
                    break
                else:
                    print("Su pedido no ha sido cancelado, presione una tecla para continuar...")
                    tecla.getch()
        subtotal = 0
        cant_beb_1 = 0
        cant_beb_2 = 0
        cant_beb_3 = 0
        cant_plat_1 = 0
        cant_plat_2 = 0
        cant_plat_3 = 0
        cant_post_1 = 0
        cant_post_2 = 0
        cant_post_3 = 0
    elif opcion == 4:
        rut = vrut()
        if rut in lruts:
            for x in range(len(lruts)):
                if rut == lruts[x]:
                    posicion = x
            nfila = lfilas[posicion]
            nmesa = lmesas[posicion]
            boleta(lsubtotal[posicion])
            restaurante[nfila-1][nmesa-1] = 0
            lcantbeb1.pop(posicion)
            lcantbeb2.pop(posicion)
            lcantbeb3.pop(posicion)
            lcantplat1.pop(posicion)
            lcantplat2.pop(posicion)
            lcantplat3.pop(posicion)
            lcantpost1.pop(posicion)
            lcantpost2.pop(posicion)
            lcantpost3.pop(posicion)
            lsubtotal.pop(posicion)
            lfilas.pop(posicion)
            lmesas.pop(posicion)
            lruts.pop(posicion)
            lnombres.pop(posicion)
            lcorreos.pop(posicion)
    elif opcion == 5:
        rut = vrut()
        if rut in lruts:
            for x in range(len(lruts)):
                if rut == lruts[x]:
                    posicion = x
            nfila = lfilas[posicion]
            nmesa = lmesas[posicion]
            restaurante[nfila-1][nmesa-1] = 0
            lcantbeb1.pop(posicion)
            lcantbeb2.pop(posicion)
            lcantbeb3.pop(posicion)
            lcantplat1.pop(posicion)
            lcantplat2.pop(posicion)
            lcantplat3.pop(posicion)
            lcantpost1.pop(posicion)
            lcantpost2.pop(posicion)
            lcantpost3.pop(posicion)
            lsubtotal.pop(posicion)
            lfilas.pop(posicion)
            lmesas.pop(posicion)
            lruts.pop(posicion)
            lnombres.pop(posicion)
            lcorreos.pop(posicion)
            print("Su reserva ha sido cancelada con éxito!")
            time.sleep(2)
    else:
        break