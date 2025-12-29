from functools import reduce

nombres = list(map(str.strip, input("Ingrese los nombres de los estudiantes: ").split(",")))

notas = list(map(float, input("Ingrese la nota de cada estudiante: ").split(",")))

aprueba = lambda nota: "-->APROBADO" if nota >= 70 else "-->REPROBADO"

estudiantes = list(zip(nombres, notas))

resultado = list(map(lambda e: (e[0], e[1], aprueba(e[1])), estudiantes))

aprobados = list(filter(lambda e: e[1] >= 70, estudiantes))

reprobados = list(filter(lambda e: e[1] < 70, estudiantes))

promedio = reduce(lambda x, y: x + y, notas) / len(notas)

print("Resultados finales:", resultado)
print("Los estudiantes que aprobaron son:", aprobados)
print ("Los estudiantes que reprobados son:", reprobados)
print("El promedio general de todo el curso es de:", promedio)
