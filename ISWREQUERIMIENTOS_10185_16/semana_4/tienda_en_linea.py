productos = []
categorias = set()


def agregar_producto(id, nombre, precio, categoria):
    producto = {
        "id": id,
        "nombre": nombre,
        "precio": precio,
        "categoria": categoria
    }
    productos.append(producto)
    categorias.add(categoria)
    print(f"producto '{nombre}' agregado correctamente")
    return producto

def buscar_por_categoria(categoria):
    return [p for p in productos if p["categoria"] == categoria]

def formatear_producto(producto):
    return f"{producto['nombre']} - ${producto['precio']} - {producto['categoria']}"

def mostrar_todos_productos():    #interfaz de usuario 
    if not productos:
        print("no hay productos registrados.")
        return
    
    print("\n-- listado de productos --")
    for i, producto in enumerate(productos, 1):
        print(f"{i}. {formatear_producto(producto)}")

def mostrar_productos_por_categoria():
    if not categorias:
        print("no hay categorías disponibles.")
        return
    print("\n-- categorías disponibles --") #muetras las categotias disponibles 
    lista_categorias = list(categorias)
    for i, cat in enumerate(lista_categorias, 1):
        print(f"{i}. {cat}")
    
    try:
        seleccion = int(input("\nseleccione una categoría: "))
        if 1 <= seleccion <= len(lista_categorias):
            categoria_elegida = lista_categorias[seleccion-1]
            productos_filtrados = buscar_por_categoria(categoria_elegida)
            
            print(f"\n-- productos en '{categoria_elegida}' --")
            if productos_filtrados:
                for i, p in enumerate(productos_filtrados, 1):
                    print(f"{i}. {formatear_producto(p)}")
            else:
                print(f"no hay productos en la categoría '{categoria_elegida}'")
        else:
            print("selección fuera de rango.")
    except ValueError:
        print("por favor ingrese un número válido.")

def agregar_nuevo_producto():
    try:
        print("\n-- agregar nuevo producto --")
        id = input("id del producto: ")
        nombre = input("nombre del producto: ")
        
        precio_texto = input("precio del producto: ") #validacion de productos 
        precio = float(precio_texto)
        
        categoria = input("categoría del producto: ")
        
        agregar_producto(id, nombre, precio, categoria) #agregar un producto 
    except ValueError:
        print("error: verifique que el precio sea un número válido.")

def mostrar_menu_principal():      #menu innteractivo 
    while True:
        print("\n" + "--" * 17)
        print(" sistema de gestión de productos")
        print("--" * 17)
        print("1. ver todos los productos")
        print("2. ver productos por categoría")
        print("3. agregar nuevo producto")
        print("4. salir")
        
        try:
            opcion = int(input("\nseleccione una opción: "))
            
            if opcion == 1:
                mostrar_todos_productos()
            elif opcion == 2:
                mostrar_productos_por_categoria()
            elif opcion == 3:
                agregar_nuevo_producto()
            elif opcion == 4:
                print("¡hasta pronto!")
                break
            else:
                print("opción no válida. intente de nuevo.")
        except ValueError:
            print("por favor ingrese un número válido.")

def cargar_datos_ejemplo(): #carga prueba 
    agregar_producto("001", "bisicleta elctrica",870.900, "electrónicos")
    agregar_producto("002", "teclado gemer ", 70, "periféricos")
    agregar_producto("003", "monitor gamer ", 399.00, "periféricos")
    agregar_producto("004", "audifonos gamer ", 912.901, "periféricos")
    agregar_producto("005", "celelares", 608.00, "electrónicos")
    print("--ejemplo--")


def iniciar_programa():
    cargar_datos_ejemplo()
    mostrar_menu_principal()

if __name__ == "__main__":
    iniciar_programa()