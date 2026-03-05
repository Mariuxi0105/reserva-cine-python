# Programa para reservar un asiento en una sala de cine 3x4

# Crear matriz 3x4 inicializada en 0 (asientos libres)
asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# Mostrar estado inicial
print("Estado inicial de la sala:")
for i in range(3):
    for j in range(4):
        print(asientos[i][j], end=" ")
    print()

# Pedir datos al usuario
fila = int(input("Ingrese fila (0 a 2): "))
columna = int(input("Ingrese columna (0 a 3): "))

# Validar rango
if 0 <= fila <= 2 and 0 <= columna <= 3:
    if asientos[fila][columna] == 0:
        asientos[fila][columna] = 1
        print("Asiento reservado correctamente.")
    else:
        print("El asiento ya está reservado.")
else:
    print("Posición inválida.")

# Mostrar estado final
print("\nEstado actual de la sala:")
for i in range(3):
    for j in range(4):
        print(asientos[i][j], end=" ")
    print()
