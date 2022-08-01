admin = {"Admin" : 2022}
enfermera = {"Enfermera" : 2424, "Enfermero" : 2525}
pas = { 2424 : "Enfermera", 2525 : "Enfermero"}
paz = { 2022 : "Admin"}

prueba = {'Nombre': "Walter" , 'Apellido': "Coto", 'Estatura':1.8, 'Habitacion':"Premium", 'GastosTotales':3500}

print("Digite la clave y luego su contraseña: ")
usuario = input("")
constraseña = int(input(""))

if usuario.title() in admin:
    if constraseña in paz:
        print("La cuenta de usuario admin, pacientes para mostrar: {}".format(prueba))
elif usuario.title() in enfermera:
    if constraseña in pas:
        print("---- Piso&Medicina ----")

        piso = {"Estandar":25, "Premium":50}
        print("¿En que tipo de habitacion se quedo el paciente: Estandar o Premium?")
        pisoo = str(input("Habitacion de tipo: "))

        if pisoo.capitalize() in piso:
            '''print("su eleccion fue: {}".format(piso[pisoo.capitalize()]),pisoo.capitalize())'''
            dias = int(input("Ingresa los dias que estuviste dentro del Hospital: "))
            med = float(input("Ingresa el costo de la medicina durante tu estadia: "))
        
            ''' val = dias*piso[pisoo.capitalize()]
            total = val + med
            print("El total de la medicina mas el piso fue: ${}".format(total))'''
            print("El total de la medicina mas el piso fue: $",(piso[pisoo.capitalize()]*dias)+med)
        else:
            print("Opcion incorrecta.")

        print("---- Insumos ----")

        insumos = {"Jeringas":10, "Curitas":5, "Suerox":25, "Canalizacion":1000, "Cateters":200, "Gazas":20, "Herramientascirugia":10000, "Paracetamol":50, "SolucionSalina":200, "Morfina":250, "Ibuprofeno":50, 
        "Acetilsalicilico":25, "Tapentadol":1200, "PeptoBismol":200, "Inflamadol":60, "Ritonavir":4000, "Cefalaxina":200, "Dexametasona":300, "VickVaporub":200, "SolucionSalina":200, "Limpieza":500}
        J = int(input("Jeringas utilizadas: "))
        je = insumos["Jeringas"] * J
        C = int(input("Curitas utilizadas: "))
        cu = insumos["Curitas"] * C
        S = int(input("Suerox utilizadas: "))
        su = insumos["Suerox"] * S
        C_a = int(input("Canalizaciones requeridas por el paciente: "))
        ca = insumos["Canalizacion"] * C_a
        A = int(input("Cateters utilizadas: "))
        A_c = insumos["Cateters"] * A
        G = int(input("Gazas utilizadas: "))
        ga = insumos["Gazas"] * G
        H = int(input("Herramientas de cirugia utilizadas: "))
        he = insumos["Herramientascirugia"] * H
        P = int(input("Paracetamol requerido: "))
        Pa = insumos["Paracetamol"] * P
        
        
        
        
        
        
        
        insumo = je + cu + su + ca

        print("El total de los insumos que requirio el paciente fue: ${}".format(insumo))

        print("---- Doctor -----")

        doctores = {"Rodrigo":300, "Juan Pablo":1000}
        eleccion = input("Elija al doctor encargado entre Rodrigo ó Juan Pablo: ")

        if eleccion.title() in doctores:
            print("Doctor: ", eleccion.title(), " Costo: ${}".format(doctores[eleccion.title()]))
        else:
            print("Escribe un nombre valido de un doctor de este Hospital.")

        print("---- Total ----")

        print("El total de estos costos fueron: $",((piso[pisoo.capitalize()]*dias)+med) + insumo + doctores[eleccion.title()])
    else:
        print("Contraseña no valida")
else:
    print("Usuario no valido.")