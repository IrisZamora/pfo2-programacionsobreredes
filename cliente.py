import requests

def registrar_usuario():
    usuario = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")

    datos = {
        "usuario": usuario,
        "contraseña": contraseña
    }

    respuesta = requests.post("http://127.0.0.1:5000/registro", json=datos)
    print("Respuesta del servidor:", respuesta.json())

def login():
    usuario = input("Usuario: ")
    contraseña = input("Contraseña: ")

    datos = {
        "usuario": usuario,
        "contraseña": contraseña
    }

    respuesta = requests.post("http://127.0.0.1:5000/login", json=datos)
    print("Respuesta del servidor:", respuesta.json())

def ver_tareas():
    respuesta = requests.get("http://127.0.0.1:5000/tareas")
    print("Respuesta del servidor:", respuesta.text)

# Menú simple
while True:
    print("\n--- Cliente de la API ---")
    print("1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Ver tareas")
    print("4. Salir")

    opcion = input("Elegí una opción: ")

    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        login()
    elif opcion == "3":
        ver_tareas()
    elif opcion == "4":
        break
    else:
        print("Opción inválida")
