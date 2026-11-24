# Pedimos el tamaño del archivo en megabytes.
tamano_mb = float(input("Introduce el tamaño del archivo en MB: "))

# Pedimos la velocidad de internet en megabits por segundo.
velocidad_mbps = float(input("Introduce la velocidad de internet en Mbps: "))

# Convertimos megabytes a megabits (1 byte equivale a 8 bits).
tamano_megabits = tamano_mb * 8

# Calculamos el tiempo dividiendo el tamaño por la velocidad.
if tamano_mb < 0 or velocidad_mbps <= 0:
    print("El tamaño no puede ser negativo y la velocidad debe ser mayor que cero.")
else:
    tiempo_segundos = tamano_megabits / velocidad_mbps
    minutos = int(tiempo_segundos // 60)
    segundos = int(tiempo_segundos % 60)
    print(f"El archivo tardará aproximadamente {tiempo_segundos:.2f} segundos en descargarse.")
    print(f"Eso equivale a {minutos} minutos y {segundos} segundos.")
