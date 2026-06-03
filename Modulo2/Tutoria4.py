#cristian creara

# #listas
# mi_lista = [1, 2, 3, 4, 5]

# #conjuntos
# mi_conjunto = {1, 2, 3, 4, 5}


# #tuplas
# mi_tupla = (1, 2, 3, 4, 5)

# #diccionarios
# mi_diccionario = {"clave1": "valor1", "clave2": "valor2"}

#buscar el tipo de dato
#in = ayuda a verificar si existe el dato dentro de la estructura /true o un false

#index = ayuda a encontrar la posición de un elemento dentro de una estructura

#count = ayuda a contar cuántas veces aparece un elemento dentro de una estructura

#next = ayuda a iterar sobre una estructura de datos, como una lista o un diccionario, 
# y obtener el siguiente elemento en la secuencia.

#indice = a[4] = 5

# []
# {}
# ()

def resolver_puente_1(tiempo_personas):
    
    import heapq
    
    personas = list(tiempo_personas.keys())
    
    heap = [(0, 0, frozenset(personas), [])]  # (tiempo_total, personas_en_puente, personas_que_ya_cruzaron)
    visitados = {}
    
    while heap:
        tiempo, lado, inicio, pasos = heapq.heappop(heap)
        
        estado = (lado, inicio)
        
        if estado in visitados and visitados[estado] <= tiempo:
            continue
        visitados[estado] = tiempo
        
        if len(inicio) == 0: # si cruzaron todos
            return tiempo, pasos
        
        destino = frozenset(p for p in personas if p not in inicio)
        
        if lado == 0:  # cruzan 1 o 2 personas
            candidatos = list(inicio)
            for i in range(len(candidatos)):
                for j in range(i, len(candidatos)):
                    grupo = [candidatos[i], candidatos[j]]
                    costo = max(tiempo_personas[p] for p in grupo)
                    nuevo_inicio = inicio - frozenset(grupo)
                    nuevo_tiempo = tiempo + costo
                    desc = f"Cruzan {grupo[0]} + {grupo[1]} -> ({costo} min)" if i != j else f"Cruza {grupo[0]} -> ({costo} min)"
                    heapq.heappush(heap, (nuevo_tiempo, 1, nuevo_inicio, pasos + [desc]))
                    
        else:  # regresa 1 persona
            for p in destino:
                costo = tiempo_personas[p]
                nuevo_inicio = inicio | frozenset([p])
                nuevo_tiempo = tiempo + costo
                heapq.heappush(heap, (nuevo_tiempo, 0, nuevo_inicio, pasos + [f"Regresa {p} -> ({costo} min)"]))
        
    return float("inf"), []  # si no se encuentra solución
    
tiempo_personas = {
    "Niño": 1,
    "Padre": 2,
    "Madre": 5,
    "Abuelo": 7
}

limite = 15 

tiempo_total, pasos = resolver_puente_1(tiempo_personas)

print ("---- solucion optima ----")
for i, paso in enumerate(pasos, 1):
    print(f"Viaje {i}: {paso}")
print(f"Tiempo total: {tiempo_total} minutos")
print(f"¿Cumple con el límite de {limite} minutos? {'Sí' if tiempo_total <= limite else 'No'}")
