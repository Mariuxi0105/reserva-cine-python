asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

f = int(input("Ingrese fila (0 a 2): "))
c = int(input("Ingrese columna (0 a 3): "))

# Validación de disponibilidad
if 0 <= f <= 2 and 0 <= c <= 3:
    if asientos[f][c] == 0:
        asientos[f][c] = 1
        print("Asiento reservado con éxito.")
    else:
        print("El asiento ya está ocupado.")
else:
    print("Error: Coordenadas fuera de rango.")

print("\nEstado de la sala:")
for i in range(3):
    for j in range(4):
        print(asientos[i][j], end=" ")
    print()
