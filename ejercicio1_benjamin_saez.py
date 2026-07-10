#benjamin saez

recorridos= {
    'R001': ['Santiago', 'Valparaiso', 120, 'normal', 'dia', True],
    'R002' : ['Santiago','Concepçion', 500, 'cama', 'noche', True],
    'R003': ['La serena','Coquimbo', 15, 'normal', 'dia', False],
    'R004': ['Temuco', 'Valdivia', 165, 'semi-cama','dia', True],
    'R005':['Iquique', 'Arica', 310, 'cama ', 'noche', False],
    'R006': ['Santiago', ' Rancagua', 90, 'normal','dia', True]
}
venta= {


    'R001': [7990,20],
    'R002': [25990, 0],
    'R003': [1990, 35],
    'R004': [12990, 8],
    'R005': [18990, 3],
    "R006": [4990,12]
}

    


def leer_opcion():
    print("***MENU PRINCIPAL***")
    print("1.- Asientos por ciudad de origen\n 2.- Busqueda de recorridos por rango de precio\n3.-Actualizar precio de recorrido\n4.-Agregar recorrido\n5.-Eliminar recorrido\n 6.- Salir")
    try:


        Opcion=int(input("Ingrese una opcion: "))
        if 1<= Opcion <=6:
            return Opcion
        else:
            print("Error: Debe seleccionar una opcion valida")
            return 0
    except ValueError:
        print("Error: Debe de ingresar un numero entero")
    except ZeroDivisionError:
        print("Error: Debe de ingresar un numero mayor a cero")


def asientos_origen(origen, dicc_recorrido, dicc_venta):
    total_asientos=0
    for clave in dicc_recorrido:
        if dicc_recorrido[clave][0].lower() == origen.lower():
            total_asientos+=dicc_venta[clave][1]
    if total_asientos >0:
        print(f"El total de asientos son: {total_asientos}")
    else:
        print("No hay asientos disponibles")
def  busqueda_precio(p_min, p_max, dicc_venta, dicc_recorrido):
    lista_precio=[]
    for i in dicc_venta:
        a=dicc_venta[i][0]
        b= dicc_venta[i][1]
        origen=dicc_recorrido[i][0]
        destino=dicc_recorrido[i][1]
        if a>= p_min and a <= p_max and b != 0:
            texto=f"{origen}-{destino}-{i}"
            lista_precio.append(texto)
    if len(lista_precio) > 0:
        lista_precio.sort()
        print(f"La lista de precios que condicen son: {lista_precio}  ")
    else:
        print("No hay recorridos en ese rango de precios")


def buscar_codigo(codigo, dicc_venta):
    for clave in dicc_venta:

        if clave.lower() == codigo.strip().lower():
            return True
        
    return False


def actualizar_precio(codigo, nuevo_precio, dicc_venta):
    if codigo in dicc_venta:
        dicc_venta[codigo][0]= nuevo_precio
        return True
    else:
        return False

def agregar_recorrido(codigo,origen,destino,distancia,tipo_bus,servicio,tiene_wifi,precio,asientos, dicc_recorrido,dicc_venta):
   
    if  validacion_codigo(codigo, venta):
        print("Error: ese codigo ya existe")
        return
    if not validacion_origen(origen):
        print("Error")
        return
    if not validacion_destino(destino):
        print("Error:")
        return
    



def validacion_codigo(codigo, dicc_venta):
    for i in dicc_venta:
        if i.lower().strip() == codigo.lower().strip():
            return True
        else:
            return False
def validacion_origen(origen):
    if origen.strip() != "":
        return True
    return False
def validacion_destino(destino):
    if destino.strip() !="":
        return True
    return False
def validacion_distancia(distancia):
    if distancia > 0:
        return True
    return False
def validacion_tipo_bus(tipo_bus):
    if tipo_bus.lower().strip() == "normal".lower().strip() or  "semi-cama".lower().strip() or "cama".lower().strip():
        return True
    return False
def validacion_servicio(servicio):
    if servicio.lower().strip() == "dia".lower().strip() or "noche".lower().strip():
        return True
    return False
def validacion_wifi(wifi):
    if wifi == "s".strip().lower() or "n".strip().lower():
        return True
    return False
def validar_precio(precio):
    if precio >0:
        return True
    return False
def validacion_asientos(asientos):
    if asientos >0:
        return True
    return False





while True:
    opcion=leer_opcion()
    if opcion==6:
        print("Programa finalizado")
        break
    if opcion ==1:
        ciudad_origen=str(input("Ingrese la ciudad de origen: ")).strip().lower()
        asientos_origen(ciudad_origen,recorridos,venta)
    if opcion ==2:
        try:

            minimo=int(input("Ingrese el precio mininmo: "))
            maximo=int(input("Ingrese el precio maximo: "))
        except ValueError:
            print("Debe ingresar valores enteros")
            continue
        busqueda_precio(minimo,maximo,venta,recorridos)
    if opcion == 3:
        while True:

            codigo_recorrido=str(input("Ingrese el codigo del recorrido: ")).strip()
            buscar_codigo(codigo_recorrido,venta)
            
        
            try:

                precio=int(input("Ingrese el nuevo precio: "))
                valor_total=actualizar_precio(buscar_codigo, precio, venta)
            except ValueError:
                print("Ingrese un numero entero")
            except ZeroDivisionError:
                print("Ingrese un numero mayor a 0")
            if valor_total:
                print("Precio Actualizado")
            else:

                print("Error: Ese codigo no existe")
            repuesta=str(input("Desea actualizar otro precio? (s/n): "))
            if repuesta != "s":
                break

    if opcion == 4:
         codigo=str(input("Ingrese el codigo: "))
         codigo_validado=validacion_codigo(codigo, venta)
         origen=str(input("Ingrese el origen: "))
         origen_valido=validacion_origen(origen)
         destino=str(input("Ingrese el destino: "))
         destino_valido=validacion_destino(destino)
         try:
             distancia=int(input("Ingrese la distancia (km): "))
             distancia_validada=validacion_distancia(distancia)
       

         except ValueError:
             print("Error: Debe de ser un numero entero")
         tipo_bus=str(input("Ingrese el tipo de bus: "))
         bus_validado=validacion_tipo_bus(tipo_bus)
         servicio=str(input("Ingrese el servicio (dia/noche): "))
         servicio_validado=validacion_servicio(servicio)
         wifi=str(input("Tiene Wifi? (s/n): "))
         wifi_validado=validacion_wifi(wifi)
         try:
             
            precio=int(input("Ingrese el precio: "))
            precio_validado=validar_precio(precio)

         except ValueError:
             print("Ingrese un valor entero")
         asientos=int(input("Ingrese asientos: "))
         validar_asientos= valdiar_asientos(asientos)
         agregar_recorrido(codigo_validado,origen_valido,destino_valido, distancia_validada, bus_validado,servicio_validado,wifi_validado,precio_validado,validar_asientos)




             



        

            






           
        
    