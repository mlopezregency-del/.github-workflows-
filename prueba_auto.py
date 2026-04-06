from datetime import datetime
import os

ahora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
mensaje = f"Extracción de prueba realizada exitosamente a las: {ahora}\n"

with open("log_ejecucion.txt", "a") as f:
    f.write(mensaje)

print("Proceso finalizado correctamente.")
