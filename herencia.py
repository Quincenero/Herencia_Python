class Persona:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
    
    def saludar(self):
        print(f"Hola mi nombre es: {self.nombre} {self.apellido} con DNI {self.dni}")
        
        
class Alumno(Persona):
    def __init__(self, nombre, apellido, dni, turno):
        super().__init__(nombre, apellido, dni)
        self.turno = turno
        
    def inscribirse(self):
        print("Me inscribi en un curso de la Agencia de Aprendizaje")


class Docente(Persona):
    def __init__(self, nombre, apellido, dni, CUIT):
        super().__init__(nombre, apellido, dni)
        self.CUIT = CUIT
    
    def tomar_curso(self):
        print("Tome un curso como docente en Python Avanzado y Django")
        
# Alumno        
alumno1 = Alumno("Carlos", "Lopez", 1234, "Noche")
alumno1.saludar()
alumno1.inscribirse()

# Docente
docente1 = Docente("Maria", "Del Cerro", 5678, 1111)
docente1.saludar()
docente1.tomar_curso()
