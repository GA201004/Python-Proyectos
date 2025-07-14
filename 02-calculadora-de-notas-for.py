calificacion=0
contador=int(input("Introduzca cantidad de notas: "))


for i in range(contador):
    nota = float(input("Introduzca la calificación de la nota: "))
    calificacion += nota

print("El promedio de tus notas es:", calificacion/contador)
