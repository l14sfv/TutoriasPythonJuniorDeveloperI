#print("python", "java", edad, sep=" -")

ejemplo = "carro"
cart = "moto"
numero = 5
ejem = True

#tipos de impresion
print(ejemplo)
print(ejemplo,          cart)
print(ejemplo, cart, numero, sep="-")

print("python", "java", numero, sep=" - ")

print(f"python - {cart} - {ejem} java {ejemplo}")

print(f"Suma: {5 - 7}")

#ejercicios
#1
# solicitar un nombre, despues mostrarlo en un print
# solicite nombre, aparte apellido, luego solicite 3 notas, despues imprima el nombre completo y el promedio de las notas

nombre = input("Ingrese su nombre: ")
print("Hola ", nombre)

#separadores SEP, \n, END, 

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))
nota3 = float(input("Ingrese la nota 3: "))
promedio = (nota1 + nota2 + nota3) / 3

print(f"Hola {nombre} {apellido},\nTus notas fueron {nota1}, {nota2} y {nota3}\ntu promedio es: {promedio:.2f}")
print("Hola", nombre, apellido, sep=" - ", end=".\n")
print("Tus notas fueron", nota1, nota2, nota3, "tu promedio es:", promedio)
print("Hola", nombre, apellido, sep=" - ", end=".\n")
print("Tus notas fueron" + str(nota1) + ", " + str(nota2) + " y " + str(nota3) + ", tu promedio es:" + str(promedio))