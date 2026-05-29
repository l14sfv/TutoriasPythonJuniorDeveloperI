# #Open api
# #archivo yaml o en un archivo json
# #swagger

from fastapi import FastAPI

app = FastAPI(title="Ejmplo api", version="0.1")

# @app.get("/saludo")

# @app.get("/saludo/{nombre}")

# @app.post("/saludo")

# @app.put("/saludo/{nombre}")

# @app.delete("/saludo/{nombre}")

# #HTTPS://localhost:8000/saludo
# #HTTPS://localhost:8000/saludo/juan

# #HTTPS://localhost:8000/saludo/juan
# #HTTPS://localhost:8000/saludo/juan

# #cuentas bloqueadas
# #while 
# #Mientras (el PIN sea incorrecto):
# #      volver a pedir PIN


# #Mientras (el personaje esté dentro de la zona de veneno):
#      # Restar 5 puntos de salud

# #Mientras (condicion):
#    # bloque de instrucciones
# """
# contador = 1

# while contador <= 3:
    
#     print(contador)
#     contador += 1


# opcion = ""

# while opcion != "salir":
#     opcion = input("Escriba una opcion: ")
#     print("Elegiste: ", opcion)


# print("otras instrucciones")
# print("otras instrucciones")
# print("otras instrucciones")



# contador = 0
# password = "admin123"
# passIngresado = ""

# while (passIngresado != password) and (contador < 3):
#     passIngresado = input("Ingrese el password: ")
#     contador += 1
#     print(f"ha intentado {contador} veces")

#     if contador == 3:
#         print("cuenta bloqueada!")
        

# if(contador < 3 ):
#     print("accediendo al sistema...")

# """
# contador = 0
# while True:
#     contador+= 1
#     print(contador)
#     if contador == 3:
#         break
    
# #for
# """
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)
# print(10)

# x = 1
# print(x)
# x+= 1
# print(x)
# x+= 1
# print(x)
# x+= 1
# print(x)
# x+= 1
# print(x)
# x+= 1
# print(x)
# x+= 1
# print(x)
# x+= 1
# print(x)
# x+= 1
# print(x)

# frase = "hola como estás?"

# for x in [1,2,3,4,5,6,7,8,9,10]:
#     print(f"{x} {frase}")



# for letra in "HOLA":
#     print(letra)



# frutas = ["manzana", "pera", "piña", "uva"]

# for f in frutas:
#     print(f"yo como {f}")


# for numero in range(2, 20, 3):
#     print(numero)

# """

# for numero in range(9, 0, -1):
#                   #(inicio  fin      incremento )
#     print(numero)
# print("despegue")


# #encryptacion de mensajes
# mensaje = "hola mundo"
# mensajeEncriptado = ""
# for letra in mensaje:
#     if letra == "a":
#         mensajeEncriptado += "4"
# #     elif letra == "e":
# #         mensajeEncriptado += "3"
# #     elif letra == "i":
# #         mensajeEncriptado += "1"
# #     elif letra == "o":
# #         mensajeEncriptado += "0"
# #     else:
# #         mensajeEncriptado += letra
        
# # print(mensajeEncriptado)

# # ##encriptar https
# # import bycrypt

# # contrasena = "admin123"
# # encriptacion = bycript.hashpw(contrasena.encode("utf-8"), bycrypt.gensalt())
# # print(encriptacion)

# # contrasena_ingresada = "admin123"

# # if bycrypt.checkpw(contrasena_ingresada.encode("utf-8"), encriptacion):
# #     print("contrasena correcta")
# # else:    print("contrasena incorrecta")

# # Ejercicio: “Menú de comandos de consola”
# # Simula un mini‑sistema donde el usuario ingresa un comando 
# # (por ejemplo: login, register, exit), y el programa usa match-case para decidir qué hacer.

# while True:
#     print("\n--- Menú ---")
#     print("1. login")
#     print("2. register")
#     print("3. logout")
#     print("4. exit")
#     comando = input("\nIngresa un comando (texto o número): ").strip()

#     match comando:
#         case "login" | "1" | "entrar":
#             print("Entrando al sistema...")
#         case "register" | "2" | "registro":
#             print("Abriendo pantalla de registro...")
#         case "logout" | "3" | "salir":
#             print("Cerrando tu sesión...")
#         case "exit" | "4" | "salir":
#             print("Saliendo de la app...")
#             break
#         case _:
#             print("Comando no reconocido")
            
# #funciones

# def pedir_dato(comando):
#     match comando:
#         case "login" | "1" | "entrar":
#             print("Entrando al sistema...")
#         case "register" | "2" | "registro":
#             print("Abriendo pantalla de registro...")
#         case "logout" | "3" | "salir":
#             print("Cerrando tu sesión...")
#         case "exit" | "4" | "salir":
#             print("Saliendo de la app...")
#         case _:
#             print("Comando no reconocido")
            
# while True:
#     print("\n--- Menú ---")
#     print("1. login")
#     print("2. register")
#     print("3. logout")
#     print("4. exit")
#     comando = input("\nIngresa un comando (texto o número): ").strip()
    
#     pedir_dato(comando)
    
#     if comando in ["exit", "4", "salir"]:
#         break
    
# while True:
#     comando = input("\nIngresa un comando (texto o número): ").strip()
    
#     if comando in ["exit", "4", "salir"]:
#         print("Saliendo de la app...")
#         break
    
#     pedir_dato(comando)
    
texto = "   Hola Mundo   "
print(texto)
print(texto.strip())