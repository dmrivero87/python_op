

class Alumno():
    def resultados (self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
               print("Nombre: ",self.nombre)
               print("Nota: ",self.nota)
  
    def resultado(self):
            if self.nota < 6:
                print("El alumno suspendió")
            else:
                print("El alumno aprobó")

alumno1=Alumno()
alumno2=Alumno()
alumno3=Alumno()

alumno1.resultados("Pablo",8)
alumno2.resultados("Fernando",4)
alumno3.resultados("Martina", 10)

alumno1.imprimir()
alumno1.resultado()
alumno2.imprimir()
alumno2.resultado()
alumno3.imprimir()
alumno3.resultado()