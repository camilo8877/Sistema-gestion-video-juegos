videojuegos = {
    "VG001": {
        "nombre": "FIFA 26",
        "plataforma": "PlayStation 5",
        "precio": 250000,
        "cantidad": 15
    },


    "VG002": {
        "nombre": "Mario Kart 8 Deluxe",
        "plataforma": "GameCube",
        "precio":300000,
        "cantidad": 12
    },



    "VG003": {
        "nombre": "street fighter 6",
        "plataforma": "PlayStation 4",
        "precio": 350000,
        "cantidad": 20
    },

      "VG004": {
        "nombre": "halo infinite",
        "plataforma": "xbox one",
        "precio": 350000,
        "cantidad": 20
    },

      "VG005": {
        "nombre": "goldeneye 007",
        "plataforma": "Nintendo 64",
        "precio": 150000,
        "cantidad": 10
    },

     
      "VG006": {
        "nombre": "sanandreas",
        "plataforma": "playstation 3",
        "precio": 70000,
        "cantidad": 8
    },

      "VG007": {
        "nombre": "sanandreas",
        "plataforma": "playstation 3",
        "precio": 70000,
        "cantidad": 8
    },

    "VG008": {
        "nombre": "soccer 19",
        "plataforma": "playstation 1",
        "precio": 200000,
        "cantidad": 7
    },

    "VG009": {
        "nombre": "mortal kombat 11",
        "plataforma": "playstation 4",
        "precio": 300000,
        "cantidad": 9
    },

    "VG010": {
        "nombre": "tennis 2020",
        "plataforma": "playstation 3",
        "precio": 180000,
        "cantidad": 5
    },
}

historial_ventas = []

#Función agregar video juego
def agregar_videojuego():
    codigo = input("Ingrese el codigo del videojuego: ").strip().upper()
    if codigo in videojuegos:
        print("El codigo ya existe")
    else:

        nombre = input("Ingrese el nombre: ")
        plataforma = input("Ingrese la plataforma: ")
        precio = float(input("Ingrese el precio: "))
        cantidad = int(input("Ingrese la cantidad: "))

        videojuegos[codigo] = {
            "nombre": nombre,
            "plataforma": plataforma,
            "precio": precio,
            "cantidad": cantidad
        }

        print("Video juego agregado correctamente")  


#Función mostrar inventario
def mostrar_inventario():
        for codigo, datos in videojuegos.items():
            if datos["cantidad"] > 0:
              print(f"Codigo: {codigo}")
              print(f"Nombre: {datos['nombre']}")
              print(f"Plataforma: {datos['plataforma']}")
              print(f"Precio: {datos['precio']}")
              print(f"Cantidad: {datos['cantidad']}")
              print("------------------")
            else:
              print("El inventario esta vacio")
    

def buscar_videojuego():
    codigo = input("Ingrese el codigo del videojuego: ").strip().upper()
    if codigo in videojuegos:
        videojuego = videojuegos[codigo]
        print(f"Nombre: {videojuego['nombre']}")
        print(f"Plataforma: {videojuego['plataforma']}")
        print(f"Precio: {videojuego['precio']}")
        print(f"Cantidad: {videojuego['cantidad']}")
    else:
        print("Video juego no encontrado")

def actualizar_precio():
    codigo = input("Ingrese el codigo del videojuego: ").strip().upper()
    if codigo in videojuegos:
        nuevo_precio = float(input("Ingrese el nuevo precio: "))
        videojuegos[codigo]["precio"] = nuevo_precio
        print("Precio actualizado correctamente")
    else:
        print("Video juego no se encuentra en lista")

def registrar_venta():
    codigo = input("Ingrese el código del videojuego que desea comprar: ").strip().upper()

    # VALIDAR SI EXISTE
    if codigo in videojuegos:

        cantidad_vender = int(input("Ingrese la cantidad a vender: "))

        stock = videojuegos[codigo]["cantidad"]

        # VALIDAR INVENTARIO
        if cantidad_vender <= stock:

            precio = videojuegos[codigo]["precio"]
            nombre = videojuegos[codigo]["nombre"]

            # CALCULAR SUBTOTAL
            subtotal = precio * cantidad_vender
            descuento = 0

            #DESCUENTO DEL 10%
            if subtotal >= 100000:
                descuento = subtotal * 0.10
                

            # CALCULAR TOTAL
            total = subtotal-descuento
        
        
            # RESTAR INVENTARIO
            videojuegos[codigo]["cantidad"] -= cantidad_vender

            #GUARDAR HISTORIAL
            venta={
                "codigo": codigo,
                "cantidad": cantidad_vender,
                "precio": precio,
                "total": total}
            historial_ventas.append(venta)
            

            # MOSTRAR FACTURA
            print(f"""
                ======== FACTURA ========

                Videojuego: {nombre}
                Cantidad vendida: {cantidad_vender}
                Precio unitario: {precio}
                subtotal: {subtotal}
                descuento: {descuento}
                Total a pagar: {total}

                =========================
                """)
            print("Fue un gusto atenderlo, regrese pronto!!")
        else:
            print("No hay la cantidad suficiente en inventario")

    else:
        print("El videojuego no existe en inventario")

def mostrar_estadisticas():

    # TOTAL VIDEOJUEGOS
    total_videojuegos = len(videojuegos)

    # VALOR TOTAL INVENTARIO
    valor_total = 0

    # VARIABLES AUXILIARES
    videojuego_costoso = ""
    precio_mayor = 0

    videojuego_mayor_stock = ""
    mayor_cantidad = 0

    suma_precios = 0

    # RECORRER DICCIONARIO
    for codigo, datos in videojuegos.items():

        # VALOR TOTAL INVENTARIO
        valor_total += datos["precio"] * datos["cantidad"]

        # VIDEOJUEGO MAS COSTOSO
        if datos["precio"] > precio_mayor:

            precio_mayor = datos["precio"]
            videojuego_costoso = datos["nombre"]

        # VIDEOJUEGO CON MAYOR CANTIDAD
        if datos["cantidad"] > mayor_cantidad:

            mayor_cantidad = datos["cantidad"]
            videojuego_mayor_stock = datos["nombre"]

        # SUMA DE PRECIOS
        suma_precios += datos["precio"]

    # PROMEDIO
    promedio = suma_precios / total_videojuegos

    # MOSTRAR RESULTADOS
    print(f"""
            ======== ESTADISTICAS ========

            Total videojuegos registrados: {total_videojuegos}

            Valor total del inventario: {valor_total}

            Videojuego más costoso: {videojuego_costoso}

            Videojuego con mayor cantidad en inventario: {videojuego_mayor_stock} 
            
            Unidades disponibles: {mayor_cantidad}

            Promedio de precios: {promedio}

            ================================
    """)
def eliminar_videojuego():

    codigo = input("Ingrese el código del videojuego a eliminar: ").strip().upper()

    # VALIDAR SI EXISTE
    if codigo in videojuegos:

        del videojuegos[codigo]

        print("Videojuego eliminado correctamente")

    else:
        print("El videojuego no existe")

def buscar_por_plataforma():

    plataforma = input("Ingrese la plataforma: ").lower()

    encontrado = False

    for codigo, datos in videojuegos.items():

        if datos["plataforma"].lower() == plataforma:

            encontrado = True

            print(f"""
              Código: {codigo}
              Nombre: {datos["nombre"]}
              Precio: {datos["precio"]}
              Cantidad: {datos["cantidad"]}
      """)

    if encontrado == False:
        print("No se encontraron videojuegos")

def inventario_bajo():

    print("=== VIDEOJUEGOS CON INVENTARIO BAJO ===")

    for codigo, datos in videojuegos.items():

        if datos["cantidad"] < 2:

            print(f"""
              Código: {codigo}
              Nombre: {datos["nombre"]}
              Cantidad: {datos["cantidad"]}
           """)

def mostrar_historial():

    print("======= HISTORIAL =======")

    for venta in historial_ventas:

        print(f"""
          Código: {venta["codigo"]}
          Precio: {venta["precio"]}
          Cantidad: {venta["cantidad_vender"]}
          Total: {venta["total"]}
          """)

def videojuego_mas_vendido():

    ventas_totales = {}

    # SUMAR CANTIDADES VENDIDAS
    for venta in historial_ventas:

        nombre = venta["nombre"]
        cantidad = venta["cantidad"]

        if nombre in ventas_totales:

            ventas_totales[nombre] += cantidad

        else:
            ventas_totales[nombre] = cantidad

    # BUSCAR EL MAYOR
    mayor = 0
    juego_mas_vendido = ""

    for nombre, cantidad in ventas_totales.items():

        if cantidad > mayor:

            mayor = cantidad
            juego_mas_vendido = nombre

    print(f"""
       Videojuego más vendido:
       {juego_mas_vendido}

       Cantidad vendida:
       {mayor}
       """)

#Menú principal
def menu_principal():
   while True:
    print("""
      Elija alguna de las siguientes opciones:
      ===== TIENDA DE VIDEOJUEGOS =====
      1. Agregar videojuego
      2. Mostrar inventario
      3. Buscar videojuego por código
      4. Actualizar precio
      5. Registrar venta
      6. Mostrar estadísticas
      7. Eliminar videojuego
      8. Buscar video juego por plataforma
      9. Mostrar inventario bajo stock
      10. Mostrar historial
      11. Mostrar video juego más vendido
      12. Salir

     """)
    opcion=input("Seleccione una opcion (1-12): ")   
    #Opciones
    if opcion=="1":
        agregar_videojuego()
    elif opcion=="2":
        mostrar_inventario()
    elif opcion=="3":
        buscar_videojuego()
    elif opcion=="4":
        actualizar_precio()
    elif opcion=="5":
         registrar_venta()
    elif opcion=="6":
        mostrar_estadisticas()
    elif opcion=="7":
        eliminar_videojuego()
    elif opcion=="8":
        buscar_por_plataforma()
    elif opcion=="9":
        inventario_bajo()
    elif opcion=="10":
        mostrar_historial()
    elif opcion=="11":
        videojuego_mas_vendido()
    elif opcion=="12":
        print("Gracias por usar el programa")
        break
    else:
         print("Opcion no valida")

menu_principal()