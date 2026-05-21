import json
from datetime import datetime

ruta_json = "../data/usuarios.json"
ruta_log = "../logs/auditoria.txt"

try:
    with open(ruta_json, "r") as archivo:
        usuarios = json.load(archivo)
except Exception as e:
    print("Error al leer JSON:", e)
    exit()

id_ingresado = input("Ingrese ID de tarjeta: ")

estado = "DENEGADO"
mensaje = ""
nombre = ""

for usuario in usuarios:
    if usuario["id_tarjeta"] == id_ingresado:
        nombre = usuario["nombre_empleado"]

        if usuario.get("activo", True):
            estado = "PERMITIDO"
            mensaje = "CERRADURA ABIERTA por 5 segundos"
        else:
            estado = "INACTIVO"
            mensaje = "ACCESO BLOQUEADO - Usuario inactivo"
        break

if estado == "DENEGADO":
    mensaje = "ALARMA ACTIVADA - Intento no autorizado"

print(mensaje)

fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(ruta_log, "a") as log:
    log.write(f"{fecha} - {estado} - ID: {id_ingresado} - {nombre}\n")