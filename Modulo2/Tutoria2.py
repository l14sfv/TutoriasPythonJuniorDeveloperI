# #calculadora
# def suma(a, b):
#     return a + b

# def resta(a, b):
#     return a - b

# def multiplicacion(a, b):
#     return a * b

# def division(a, b):
#     if a == 0 or b == 0:
#         return "Error: División por cero"
#     return a / b

# def calculadora(a, b, operacion):
#     if operacion == "suma":
#         return suma(a, b)
#     elif operacion == "resta":
#         return resta(a, b)
#     elif operacion == "multiplicacion":
#         return multiplicacion(a, b)
#     elif operacion == "division":
#         return division(a, b)
#     else:
#         return "Operación no válida"
    
# def main():
#     a = float(input("Ingrese el primer número: "))
#     b = float(input("Ingrese el segundo número: "))
#     operacion = input("Ingrese la operación (suma, resta, multiplicacion, division): ")
#     resultado = calculadora(a, b, operacion)
#     print(f"El resultado de la {operacion} es: {resultado}")
    
# main()

#descripciones
#def = define una función
#class = define una clase
#lamba = función anónima, es decir, una función sin nombre que se puede definir en una sola línea de código.

# def doble (x):
#     return x * 2

# doble = lambda x: x * 2

# def multiplicador (x):
#     return lambda y: x * y

# por3 = multiplicador(3)

# ejemplo de LOGIN

contrasena_inicial = "1234"
usuario_inicial = "admin"

def ingresar (usuario, contrasena):
    if usuario == usuario_inicial and contrasena == contrasena_inicial:
        return print("Ingreso exitoso")
    else:
        return print("Usuario o contraseña incorrectos")

usuario_ingresado = input("Ingrese su usuario: ")
contrasena_ingresada = input("Ingrese su contraseña: ")

resultado = ingresar(usuario_ingresado, contrasena_ingresada)

# ingresar(usuario_ingresado, contrasena_ingresada)