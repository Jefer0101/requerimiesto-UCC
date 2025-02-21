
def validar_dimensiones(dimension: float, nombre: str) -> bool:
   
    if dimension <= 0:
        raise ValueError(
            f"Error: {nombre} debe ser un valor pocitivo y  mayor que cero  "
        )
    return True

def calcular_area_terreno(base_mayor: float, base_menor: float, altura: float) -> dict:
    for dim, nombre in [(base_mayor, "Base mayor (B)"), 
                       (base_menor, "base  menor (A)"), 
                       (altura, "Altura (C)")]:
        validar_dimensiones(dim, nombre)
    
    area_rectangulo = base_menor * altura
    
    area_triangulo = ((base_mayor - base_menor) * altura) / 2
    
    area_total = area_rectangulo + area_triangulo
    return {
        "area_rectangulo": area_rectangulo,
        "area_triangulo": area_triangulo,
        "area_total": area_total
    }

print("\n______Calculadora de area de Terreno_______ ")
print("__" * 15)
    
base_mayor = float(input("\nIngrese la base mayor (B): "))
base_menor = float(input("Ingrese la base menor (A): "))
altura = float(input("Ingrese la altura (C): "))
    
resultados = calcular_area_terreno(base_mayor, base_menor, altura)
print("\nResultados:")
print("____" * 15)
print(f"Área del rectángulo: {resultados['area_rectangulo']:.2f}")
print(f"Área del triángulo: {resultados['area_triangulo']:.2f}")
print(f"Área total del terreno: {resultados['area_total']:.2f}")
        
    
