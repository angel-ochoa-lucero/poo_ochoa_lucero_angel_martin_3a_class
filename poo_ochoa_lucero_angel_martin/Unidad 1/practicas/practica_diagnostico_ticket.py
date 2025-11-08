# Practica de diagnostico_ Ochoa Lucero Angel Martin
# Simulador de ticket de venta
# Objetivo: Aplicar funciones, bucles, condiciones

# Lista y variables
total_compra = 0
productos = ["Ropero", "base de cama", "Tocador"]
precios = [300, 450, 250]
cantidades = []

# Función para calcular el total
def calcular_total(cantidades, precios):
    total = 0
    for i in range(len(cantidades)):
        total += cantidades[i] * precios[i]
    return total

# Función para aplicar descuento
def aplicar_descuento(total):
    # Descuento del 10% si el total es mayor o igual a $200
    if total >= 200:
        descuento = total * 0.10
        total_con_descuento = total - descuento
        return total_con_descuento, descuento
    else:
        return total, 0

# Menú de usuario
print("..:::Bienvenido a Muebles Troncozo:::..")
nombre = input("Ingresa tu nombre: ")

print("\n--- Selecciona tu pedido ---")
for i in range(len(productos)):
    print(f"{i+1}. {productos[i]} - ${precios[i]}")
    try:
        cantidad = int(input(f"¿Cuántos {productos[i]} quieres? "))
        cantidades.append(cantidad)
    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número entero.")
        cantidades.append(0) # Asume 0 si la entrada es incorrecta

# Calcular el total sin descuento
total_sin_descuento = calcular_total(cantidades, precios)

# Aplicar el descuento si es aplicable
total_con_descuento, descuento_aplicado = aplicar_descuento(total_sin_descuento)

# Impresión del ticket de venta
print("\n--- Ticket de Venta ---")
print(f"Nombre del cliente: {nombre}")
print("-----------------------")
for i in range(len(productos)):
    if cantidades[i] > 0:
        subtotal = cantidades[i] * precios[i]
        print(f"{productos[i]} x{cantidades[i]} = ${subtotal}")

print("-----------------------")
print(f"Subtotal: ${total_sin_descuento:.2f}")

if descuento_aplicado > 0:
    print(f"Descuento (10%): -${descuento_aplicado:.2f}")
    print(f"Total a pagar: ${total_con_descuento:.2f}")
else:
    print(f"Total a pagar: ${total_sin_descuento:.2f}")

print("\n¡Gracias por tu compra!")