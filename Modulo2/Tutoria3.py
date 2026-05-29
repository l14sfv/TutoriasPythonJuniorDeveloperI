#funciones
#def
def saludar(nombre):
    return "Saludos a " + nombre

saludar("Alice")

def sumar(a, b):
    return a + b

#lambda

doble = lambda x: x * 2
suma = lambda a, b: a + b

#sorted, map, filter

#CICLOS
# for = se utiliza para iterar sobre una secuencia (como una lista, tupla, diccionario, conjunto o cadena) y ejecutar un bloque de código para cada elemento de la secuencia.
# while = se utiliza para ejecutar un bloque de código mientras una condición sea verdadera. La sintaxis básica es: while condición: bloque de código. El bloque de código se ejecutará repetidamente hasta que la condición deje de ser verdadera. Es importante asegurarse de que la condición eventualmente se vuelva falsa para evitar un bucle infinito.
# do-while = no existe en Python, pero se puede simular utilizando un bucle while con una condición que siempre sea verdadera y luego utilizando una declaración break para salir del bucle después de la primera iteración. Por ejemplo:

#rango
for i in range(10):
    print(i)
    
# listas [manzana, pera, naranja]
frutas = ["manzana", "pera", "naranja"]
for fruta in frutas:
    print(fruta) #imprime la segunda letra de cada fruta
    
#contadores
for n in range(0, 10, 2):
    print(n) #imprime 0, 3, 6, 9
    
#while
contador = 0
while contador < -20:
    print(contador)
    contador -= 1 #contador
    
#do-while simulado
while True:
    numero = int(input("Ingrese un número positivo: "))
    
    #condicion
    if numero > 0:
        print("Número válido")
        break
#CONDICIONALES
# if = se utiliza para ejecutar un bloque de código si una condición es verdadera. La sintaxis básica es: if condición: bloque de código. Si la condición es verdadera, se ejecutará el bloque de código. Si la condición es falsa, se omitirá el bloque de código y se continuará con el resto del programa.
# elif = se utiliza para agregar condiciones adicionales a una declaración if. La sintaxis básica es
# else = se utiliza para ejecutar un bloque de código si todas las condiciones anteriores en una declaración if-elif son falsas. La sintaxis básica es: else: bloque de código. Si ninguna de las condiciones anteriores es verdadera, se ejecutará el bloque de código dentro del else.

# if = si
# elif = si no, pero
# else = si no

opin = input("¿Te gusta Python? (si/no): 1,2,3")

if opin == "1":
    print("¡Genial! Python es un lenguaje de programación muy popular.")
elif opin == "2":
    print("¡Vaya! Python no es para todos, pero hay muchos otros lenguajes de programación que podrían interesarte.")
elif opin == "3":
    print("mas o menos.")
else:
    print("Respuesta no válida. Por favor, responde con 'si' o 'no'.")

#match-case
opinion = input("¿Te gusta Python? (si/no): 1,2,3")

match opinion:
    case "1":
        print("¡Genial! Python es un lenguaje de programación muy popular.")
    case "2":
        print("¡Vaya! Python no es para todos, pero hay muchos otros lenguajes de programación que podrían interesarte.")
    case "3":
        print("mas o menos.")
    case _:
        print("Respuesta no válida. Por favor, responde con 'si' o 'no'.")

#ejercicio
Nombres = ["Ana", "Sebastian", "Luis", "Fernanda"]
for Nombre in Nombres:
    if len( Nombre) > 5:
        print(Nombre)
        
#base de datos con parametros establecidos, como buscarlos, desde una BD

datos = ("SELECT * FROM usuarios")

for dato in datos:
    if dato[1] == "Luis":
        print(dato)
        break
    
#JWT = JSON Web Token, es un estándar abierto (RFC 7519) que define un formato compacto y autónomo para transmitir información de forma segura entre partes como un objeto JSON. Se utiliza comúnmente para la autenticación y autorización en aplicaciones web. Un JWT consta de tres partes: el encabezado, el cuerpo y la firma. 
# El encabezado contiene información sobre el tipo de token y el algoritmo de firma utilizado. El cuerpo contiene las declaraciones (claims) que representan la información que se desea transmitir, como el usuario autenticado o los permisos asociados. La firma se utiliza para verificar la integridad del token y garantizar que no haya sido modificado por terceros.

#algoritmo = "HS256" #algoritmo de firma
#algoritmo = "RS256" #algoritmo de firma asimétrica, utiliza una clave pública y una clave privada para la firma y verificación del token. La clave privada se utiliza para firmar el token, mientras que la clave pública se utiliza para verificar la firma. Este algoritmo es más seguro que el algoritmo simétrico (HS256) ya que no requiere compartir una clave secreta entre el emisor y el receptor del token.
#algoritmo = "ES256" #algoritmo de firma asimétrica, utiliza una clave pública y una clave privada para la firma y verificación del token. La clave privada se utiliza para firmar el token, mientras que la clave pública se utiliza para verificar la firma. Este algoritmo es más seguro que el algoritmo simétrico (HS256) ya que no requiere compartir una clave secreta entre el emisor y el receptor del token. Además, ES256 utiliza curvas elípticas para la generación de claves, lo que proporciona un nivel adicional de seguridad en comparación con otros algoritmos de firma asimétrica.
#algoritmo = "RSASHA256" #algoritmo de firma asimétrica, utiliza una clave pública y una clave privada para la firma y verificación del token. La clave privada se utiliza para firmar el token, mientras que la clave pública se utiliza para verificar la firma. Este algoritmo es más seguro que el algoritmo simétrico (HS256) ya que no requiere compartir una clave secreta entre el emisor y el receptor del token. Además, RSA es un algoritmo de cifrado de clave pública ampliamente utilizado en criptografía, lo que lo hace una opción popular para la firma de tokens JWT.

#sub = subject - sujeto
#exp = expiracion
#iat = issued at - emitido en
#iss = issuer - emisor
#role = rol del usuario, como admin, user, etc.

import jwt
from datetime import datetime, timedelta

SECRET_KEY = "mi_clave_secreta"

#generacion del token - despues del login
payload = {
    "sub": "1234567890",
    "username": "luis",
    "name": "John Doe",
    "iat": datetime.utcnow(),
    "exp": datetime.utcnow() + timedelta(hours=1)
}

token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

# verificacion del token - en cada solicitud protegida
try:
    decoded_payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    print(f"Usuario: {decoded_payload['username']}")
except jwt.ExpiredSignatureError:
    print("Token expirado")
except jwt.InvalidTokenError:
    print("Token inválido")

#HTTP = Hypertext Transfer Protocol, es un protocolo de comunicación utilizado para la transferencia de información en la World Wide Web. Es el protocolo subyacente que permite la comunicación entre los navegadores web y los servidores web. HTTP define cómo se formatean y transmiten los mensajes entre el cliente (navegador) y el servidor, así como las acciones que se pueden realizar con esos mensajes, como solicitar recursos, enviar datos o recibir respuestas. HTTP utiliza métodos como GET, POST, PUT, DELETE, entre otros, para indicar la acción que se desea realizar en el servidor.
#no los cifra, solo viajan en texto plano, lo que significa que pueden ser interceptados y 
# leídos por terceros si no se utiliza una capa de seguridad adicional como HTTPS.

#HTTPS = HTTP Secure, es una versión segura del protocolo HTTP que utiliza el protocolo SSL/TLS para encriptar la comunicación entre el cliente y el servidor. Esto garantiza que los datos transmitidos no puedan ser interceptados o modificados por terceros.
#cifrada, lo que significa que los datos transmitidos entre el cliente y el servidor están protegidos contra la interceptación y la manipulación por parte de terceros. HTTPS utiliza certificados digitales para autenticar la identidad del servidor y establecer una conexión segura. Es especialmente importante utilizar HTTPS en sitios web que manejan información sensible, como contraseñas, datos personales o transacciones financieras, para proteger la privacidad y la seguridad de los usuarios.
#ssl/tls = SSL (Secure Sockets Layer) y TLS (Transport Layer Security) son protocolos criptográficos que se utilizan para asegurar la comunicación en redes, especialmente en Internet. SSL fue el protocolo original desarrollado por Netscape en la década de 1990, pero ha sido reemplazado por TLS debido a vulnerabilidades de seguridad en SSL. TLS es una versión mejorada y más segura de SSL, y es ampliamente utilizado para proteger la privacidad y la integridad de los datos transmitidos entre clientes y servidores en la web. Ambos protocolos utilizan certificados digitales para autenticar la identidad del servidor y establecer una conexión segura.
