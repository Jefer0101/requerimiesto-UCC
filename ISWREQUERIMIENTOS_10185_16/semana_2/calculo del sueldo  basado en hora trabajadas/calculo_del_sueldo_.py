

def validar_entrada(valor, tipo_entrada):
    try:
        numero = float(valor)
        if numero <= 0:
            print(f"error: El balor de {tipo_entrada} debe ser mayor a cero")
            return False, None
        return True, numero
    except ValueError:
        print(f"error: ingresa un valor valido {tipo_entrada}")
        return False, None

def calcular_sueldo(horas, pago_por_hora):
    return horas * pago_por_hora

def formatear_moneda(valor):
    return "${:,.2f}".format(valor)



print("\n_______ CALCULADORA  DE SUELDO SEMANAL _______")

while True:
        horas = input("\nIngrese las horas trabajadas en la semana: ")
        valido, horas_trabajadas = validar_entrada(horas, "horas trabajadas")
        if valido:
            break
    

while True:
        pago = input("Ingrese el pago por hora: ")
        valido, tarifa_hora = validar_entrada(pago, "pago por hora")
        if valido:
            break
    

sueldo_total = calcular_sueldo(horas_trabajadas, tarifa_hora)
    

print("\n _____Resumen de Pago Semanal______")
print(f"Horas trabajadas: {horas_trabajadas:.2f} horas")
print(f"Pago por hora: {formatear_moneda(tarifa_hora)}")
print(f"Sueldo total a recibir: {formatear_moneda(sueldo_total)}")

