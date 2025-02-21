


def validar_entrada(valor):
    try:
        numero = float(valor)
        if numero <= 0:
            print("error: el valor debe ser mayor a cero")
            return False
        return True
    except ValueError:
        print("error:  ingresa un múmero válido")
        return False

def convertir_a_galones(litros):
   return litros / 3.785

def calcular_pago(galones, precio_por_galon):
   return galones * precio_por_galon


print("\n_______CALCULADORA DE PRODUCION DE LECHE :) ______")
    
while True:
    litros = input("\ningrese la cantidad de litros producidos: ")
    if validar_entrada(litros):
        litros = float(litros)
        break
    
while True:
    precio = input("Ingrese el precio por galón (en $): ")
    if validar_entrada(precio):
        precio = float(precio)
        break
    
galones = convertir_a_galones(litros)
pago_total = calcular_pago(galones, precio)
    
print("\n_______ Resultados _______")
print(f"Litros producidos: {litros:.2f} litros")
print(f"Equibalente en galones: {galones:.2f} galones")
print(f"Precio por galón: ${precio:.2f}")
print(f"Pago total a recibir: ${pago_total:.2f}")

