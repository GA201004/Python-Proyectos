calificacion=0
contador=int(input("Introduzca cantidad de notas: "))
i=0

while i < (contador):
    nota = float(input("Introduzca la calificación de la nota: "))
    calificacion += nota
    i+=1

print("El promedio de tus notas es:", calificacion/contador)
