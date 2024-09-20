nombre_vend=str
ventas_mensuales=str
ganancias_comision=float

nombre_vend=input("Hola! Dime tu nombre! ")

ventas_mensuales=input(f"Cuánto vendiste este mes {nombre_vend}? $")

ganancias_comision=0
ganancias_comision=float(ventas_mensuales)*13/100

print(f"¡Genial {nombre_vend}! Este mes ganaste ${round(ganancias_comision,2)} por comisiones de venta")