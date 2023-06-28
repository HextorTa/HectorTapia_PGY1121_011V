from datetime import datetime

vehiculos = []

def mostrar_menu():
    print("----- Menú Principal -----")
    print("1. Grabar")
    print("2. Buscar")
    print("3. Imprimir certificados")
    print("4. Salir")

def grabar_vehiculo():
    tipos_validos = ['Auto', 'Camioneta', 'Furgón']
    while True:
        tipo = input("Ingrese el tipo de vehículo (Auto, Camioneta, Furgón) o presione 'x' para volver al menú principal: ") 
        if tipo.lower() == 'x':
            return  
        elif tipo in tipos_validos:
            break
        else:
            print("Tipo de Vehiculo no encontrado")
            
    patente = ""
    while not validar_patente(patente):    
        patente = input("Ingrese la patente del vehículo: ")
        if not validar_patente(patente):
            print("La patente ingresada es incorrecta.")   
            
    marca = ""
    while not validar_marca(marca):
        marca = input("Ingrese la marca del vehículo: ")
        if not validar_marca(marca):
            print("La marca ingresada es incorrecta. Ingrese una marca válida de al menos 2 caracteres o máximo 15 caracteres.")   
            
    modelo = ""
    while not (2 <= len(modelo) <= 15):
        modelo = input("Ingrese el modelo del vehículo: ")
        if len(modelo) < 2:
            print("El modelo tiene muy pocas características. Ingrese al menos 2 caracteres.")
        elif len(modelo) > 15:
            print("El modelo sobrepasa las características permitidas. Ingrese máximo 15 caracteres.")
            
    color = ""
    colores_permitidos = ['rojo', 'azul', 'verde', 'morado', 'negro']
    while color not in colores_permitidos:
        color = input("Ingrese el color del vehículo (rojo, azul, verde, morado, negro): ")
        if color not in colores_permitidos:
            print("Color no encontrado o no válido. Por favor, ingrese un color válido.")

    combustible = ""
    while combustible not in ['Gasolina', 'Petróleo']:
        combustible = input("Ingrese el tipo de combustible (Gasolina o Petróleo): ")
        if combustible not in ['Gasolina', 'Petróleo']:
            print("Tipo de combustible no encontrado. Ingrese un tipo de combustible válido.")
        
    año = None
    while año is None or not (1990 <= año <= 2023):
        try:
            año = int(input("Ingrese el año del vehículo (1990 hasta 2023): "))
            if not (1990 <= año <= 2023):
                print("El año ingresado está fuera del rango válido.")
        except ValueError:
            print("El valor ingresado no es un año válido. Ingrese un valor numérico.")

        
    precio = 0
    while precio <= 4_999_999:
        try:
            precio = float(input("Ingrese el precio del vehículo: "))
            if precio <= 4_999_999:
                print("El precio ingresado es menor o igual a 4,999,999. Ingrese un precio mayor.")
        except ValueError:
            print("El valor ingresado no es un precio válido. Ingrese un valor numérico.")
     
    multas = []
    opcion_multas = ""
    while opcion_multas.lower() != "n":
        opcion_multas = input("¿Desea agregar una multa al vehículo? (s/n): ")

        if opcion_multas.lower() == "s":
            monto = 0
            while monto <= 999:
                try:
                    monto = float(input("Ingrese el monto de la multa (debe ser mayor a $1000): "))
                    if monto <= 999:
                        print("El monto debe ser mayor a $1000. Ingrese un valor válido.")
                except ValueError:
                    print("El valor ingresado no es un número válido. Ingrese un valor numérico.")

            fecha_multa = ""
            while not fecha_multa:
                fecha_multa = input("Ingrese la fecha de la multa (01/01/1990 a la actualidad): ")
                try:
                    datetime.strptime(fecha_multa, "%d/%m/%Y")
                except ValueError:
                    print("Formato de fecha incorrecto. Ingrese la fecha en el formato DD/MM/YYYY.")
                    fecha_multa = ""

            multa = {
                "N° Multa": len(multas) + 1,  
                "Monto": monto,
                "Fecha": fecha_multa
            }
            multas.append(multa)
        
    fecha_registro = ""
    fecha_actual = datetime.now()
    while not fecha_registro:
        fecha_registro = input("Ingrese la fecha de registro del vehículo (01/01/1990 a la actualidad): ")
        try:
            fecha_registro = datetime.strptime(fecha_registro, "%d/%m/%Y")
            if fecha_registro < datetime(1990, 1, 1) or fecha_registro > fecha_actual:
                print("Fecha de registro inválida. Debe ser entre el 01/01/1990 y la fecha actual.")
                fecha_registro = ""
        except ValueError:
            print("Formato de fecha incorrecto. Ingrese la fecha en el formato DD/MM/YYYY.")
            fecha_registro = ""
            
    nombre_dueño = ""
    while not validar_nombre_dueño(nombre_dueño):
        nombre_dueño = input("Ingrese el nombre y apellido del dueño: ")
        if not validar_nombre_dueño(nombre_dueño):
            print("El nombre ingresado es incorrecto. Asegúrese de no incluir números o signos.")

            
    rut_dueño = ""
    while not validar_rut(rut_dueño):
        rut_dueño = input("Ingrese el RUT del dueño (se puede poner . y - la k reemplácelo por un 1): ")
        if not validar_rut(rut_dueño):
            print("RUT inválido. Por favor, ingrese un RUT con las caracteristicas validas")
    
    vehiculo = {
        "Tipo": tipo.upper(),
        "Patente": patente,
        "Marca": marca.upper(),
        "Modelo": modelo.upper(),
        "Color": color.upper(),
        "Combustible": combustible.upper(),
        "Año": año,
        "Precio": precio,
        "Multas": multas,
        "Fec. Reg.": fecha_registro,
        "Nombre del Dueño": nombre_dueño.upper(),
        "RUT del Dueño": rut_dueño
    }

    vehiculos.append(vehiculo)
    print("Vehículo registrado exitosamente.")

def buscar_vehiculo():
    patente_buscar = input("Ingrese la patente del vehículo a buscar: ")
    for vehiculo in vehiculos:
        if vehiculo["Patente"] == patente_buscar:
            print("┌───────────────────────────────────────────────────────┐")
            print("│                                                       │")
            print("│               Información del Vehículo                │")
            print("│                                                       │")
            print("├───────────────────────────────────────────────────────┤")
            for key, value in vehiculo.items():
                if key == "Multas":
                    if value:
                        print("├─────────────────────── Multas ────────────────────────┤")
                        for multa in value:
                            print(f"│ Monto:{multa['Monto']:10}       Fecha: {multa['Fecha']:20}    │")
                        print("├───────────────────────────────────────────────────────┤")
                else:
                    print(f"│ {key:<16}: {str(value):<36}│")
            print("└───────────────────────────────────────────────────────┘")
            return
    print("No se encontró ningún vehículo con la patente ingresada.")
    
def imprimir_certificados():
    while True:
        print("----- Certificados -----")
        print("1. Emisión de contaminantes")
        print("2. Anotaciones vigentes")
        print("3. Multas")
        print("4. Volver al menú principal")
        
        opcion_certificado = input("Ingrese la opción del certificado a imprimir: ")
        
        if opcion_certificado == "1":
            print("Certificado de Emisión de Contaminantes")
            patente_buscar = input("Ingrese la patente del vehículo: ")
            
            for vehiculo in vehiculos:
                if vehiculo["Patente"] == patente_buscar:
                    print("┌─────────────────────────┬───────────────────┐")
                    print("│NOMBRE DEL PROPIETARIO   │RUT                │")
                    print("│{:<25}│{:<19}│".format(vehiculo['Nombre del Dueño'], vehiculo['RUT del Dueño']))
                    print("├─────────────────────────┼───────────────────┤")
                    print("│TIPO DE VEHICULO         │AÑO                │")
                    print("│{:<25}│{:<19}│".format(vehiculo['Tipo'], vehiculo['Año']))
                    print("├─────────────────────────┼───────────────────┤")
                    print("│MARCA                    │COLOR              │")
                    print("│{:<25}│{:<19}│".format(vehiculo['Marca'], vehiculo['Color']))
                    print("├─────────────────────────┼───────────────────┤")
                    print("│MODELO                   │SELLO              │")
                    print("│{:<25}│{:<19}│".format(vehiculo['Modelo'],'Verde'))
                    print("├─────────────────────────┴───────────────────┤")
                    print("│N° CHASIS / VIN                              │")
                    print("│KL1JJ52628K963666                            │")
                    print("├─────────────────────────────────────────────┤")
                    print("│N° MOTOR                                     │")
                    print("│1505579                                      │")                                                                 
                    print("└─────────────────────────────────────────────┘")
                    return
            else:
                print("No se encontró ningún vehículo con la patente ingresada.")
            return    
        elif opcion_certificado == "2":
            print("Certificado de Anotaciones Vigentes")
            patente_buscar = input("Ingrese la patente del vehículo: ")
            
            for vehiculo in vehiculos:
                if vehiculo["Patente"] == patente_buscar:
                    print("┌─────────────────────────────────────────────────────────────────────────────────┐")
                    print("│                       CERTIFICADO DE ANOTACIONES VIGENTES                       │")
                    print("├─────────────────────────────────────────────────────────────────────────────────┤")
                    print("│ Inscripcion:          BRGG. 95-9                                                │")  
                    print("│ DATOS DEL VEHICULO                                                              │")
                    print("│ Tipo de vehiculo:     {:<12} Año: {:<40}│".format(vehiculo['Tipo'], vehiculo['Año']))
                    print("│ Marca:                {:<58}│".format(vehiculo['Marca']))
                    print("│ Modelo:               {:<58}│".format(vehiculo['Modelo']))
                    print("│ Nro. Motor:           150557                                                    │")
                    print("│ Nro. Chasis:          KL1JJ52628K963666                                         │")
                    print("│ Color:                {:<58}│".format(vehiculo['Color']))
                    print("│ Combustible:          {:<58}│".format(vehiculo['Combustible']))
                    print("│ FEV:                  (NO INFORMADO)                                            │")
                    print("│ Instit. aseg.:        Seguro XYZ                                                │")
                    print("│ Numero poliza:        183,445                                                   │")
                    print("│ Fec. ven. pol.:       01/01/2025                                                │")
                    print("│ DATOS DEL PROPIETARIO                                                           │")
                    print("│ Nombre:               {:<58}│".format(vehiculo['Nombre del Dueño']))
                    print("│ R.U.T:                {:<58}│".format(vehiculo['RUT del Dueño']))
                    print("│ Fec. Adquisicion:     {:<58}│".format(str(vehiculo['Fec. Reg.']).ljust(58)))
                    print("│ repertorio:           (NO INFORMADO)                                            │")
                    print("│ numero:               XXXX                              de fecha: 01/01/2025    │")
                    print("│ Sr. usuario: Corrobore la exactitud de los datos identificatorios del vehiculo  │")
                    print("│                                                                                 │")
                    print("└─────────────────────────────────────────────────────────────────────────────────┘")
                    return
            else:
                print("No se encontró ningún vehículo con la patente ingresada.")
            return
        elif opcion_certificado == "3":
            patente_buscar = input("Ingrese la patente del vehículo: ")
            multas_encontradas = False  # Variable para indicar si se encontraron multas

            for vehiculo in vehiculos:
             if vehiculo["Patente"] == patente_buscar:
                    if "Multas" in vehiculo and vehiculo["Multas"]:
                        multas_encontradas = True  # Hay multas encontradas

                        print("┌───────────────────────────────────────┐")
                        print("│         CERTIFICADO DE MULTAS         │")
                        print("├───────────────────────────────────────┤")
                        print("│ Patente del vehículo: {:<16}│".format(vehiculo["Patente"]))
                        print("│ Nombre del propietario: {:<14}│".format(vehiculo["Nombre del Dueño"]))
                        print("│ RUT del propietario: {:<17}│".format(vehiculo["RUT del Dueño"]))
                        print("│ Número de multas: {:<20}│".format(len(vehiculo["Multas"])))
                        print("│ Multas:                               │")

                        for i, multa in enumerate(vehiculo["Multas"], 1):
                            print("│  ┌─────────────────────────────────┐  │")
                            print("│  │          Multa", i, "               │  │")
                            print("│  ├─────────────────────────────────┤  │")
                            print("│  │ N° Multa: {:<22}│{:<2}│".format(multa["N° Multa"], ""))
                            print("│  │ Monto: {:<25}│{:<2}│".format(multa["Monto"], ""))
                            print("│  │ Fecha: {:<25}│{:<2}│".format(multa["Fecha"], ""))
                            print("│  └─────────────────────────────────┘  │")
                            
                        print("└───────────────────────────────────────┘")
                        break  

            if not multas_encontradas:
                print("No se encontraron multas para el vehículo con la patente especificada.")
            return    
        
        elif opcion_certificado == "4":
            return       
        else:
            print("Opción no válida. Por favor, ingrese una opción válida.")

def validar_marca(marca):
    return len(marca) >= 2 and len(marca) <= 15 and marca.isalpha()

def validar_patente(patente):

    return len(patente) == 6 and (patente[:2].isalpha() and patente[2:].isdigit() or patente[:4].isalpha() and patente[4:].isdigit())
    
def validar_nombre_dueño(nombre):
    if len(nombre) < 3 or len(nombre) > 15:
        return False

    if not nombre.replace(' ', '').isalpha():
        return False

    return True

def validar_rut(rut):
    rut = rut.replace(".", "").replace("-", "")
    if len(rut) != 9 or not rut[:-1].isdigit():
        return False

    verificador = rut[-1].lower()
    rut = rut[:-1]

    multiplicador = 2
    suma = 0
    for digito in reversed(rut):
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador == 8:
            multiplicador = 2

    resto = suma % 11
    digito_verificador = 11 - resto
    if digito_verificador == 10:
        digito_verificador = "k"
    elif digito_verificador == 11:
        digito_verificador = 0

    return str(digito_verificador) == verificador


while True:
    mostrar_menu()
    opcion = input("Ingrese la opción deseada: ")

    if opcion == "1":
        grabar_vehiculo()
    elif opcion == "2":
        buscar_vehiculo()
    elif opcion == "3":
        imprimir_certificados()
    elif opcion == "4":
        print("Gracias por utilizar el programa.")
        print("Hector Tapia")
        print("Version 1.0")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")



