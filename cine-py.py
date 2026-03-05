# 1. Crear matriz 3x4 inicializada en 0
asientos = [[0 for _ in range(4)] for _ in range(3)]

def mostrar_sala(matriz):
    print("\nEstado actual de la sala:")
    for i in range(3):
        for j in range(4):
            print(matriz[i][j], end=" ")
        print() # Salto de línea por fila
    print("-" * 25)

# --- PASO 1: Mostrar asientos disponibles al inicio ---
mostrar_sala(asientos)

# --- PASO 2: Pedir datos al usuario ---
fila = int(input("Ingrese fila (0 a 2): "))
columna = int(input("Ingrese columna (0 a 3): "))

# --- PASO 3: Marcar reserva y mostrar resultado final ---
if 0 <= fila <= 2 and 0 <= columna <= 3:
    asientos[fila][columna] = 1
    print("\nAsiento reservado correctamente.")
    mostrar_sala(asientos)
else:
    print("\nError: Ubicación inválida.")


