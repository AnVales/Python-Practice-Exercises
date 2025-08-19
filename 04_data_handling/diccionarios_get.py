"""
Ejercicio de diccionarios en Python:
- Uso de diccionarios anidados
- Acceso seguro a valores con .get()
- Manejo de claves no disponibles
"""

estudiantes = {
    "Juan": {"matemáticas": 85, "biologia": 92, "literatura": 78},
    "Ana": {"matemáticas": 90, "biologia": 88},
    "Luis": {"literatura": 80, "biologia": 85}
}

# Ejemplo 1: Calificación de Juan en matemáticas
estudiante = "Juan"
materia = "matemáticas"
calificacion = estudiantes.get(estudiante, {}).get(materia, "No disponible")
print(f"La calificación de {estudiante} en {materia} es {calificacion}")

# Ejemplo 2: Calificación de Ana en literatura
estudiante = "Ana"
materia = "literatura"
calificacion = estudiantes.get(estudiante, {}).get(materia, "No disponible")
print(f"La calificación de {estudiante} en {materia} es {calificacion}")

# Ejemplo 3: Calificación de Luis en ciencia
estudiante = "Luis"
materia = "biologia"
calificacion = estudiantes.get(estudiante, {}).get(materia, "No disponible")
print(f"La calificación de {estudiante} en {materia} es {calificacion}")

# Ejemplo 4: Calificación de Luis en matemáticas (no disponible)
estudiante = "Luis"
materia = "matemáticas"
calificacion = estudiantes.get(estudiante, {}).get(materia, "No disponible")
print(f"La calificación de {estudiante} en {materia} es {calificacion}")