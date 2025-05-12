class Estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre= nombre
        self.edad = edad
        self.grado = grado

nombre = input("Ingrese el nombre del alumno : ")
edad = input("ingrese su edad : ")
grado = input("ingrese el grado : ")

estudiante = Estudiante(nombre,edad,grado)

print(f"""
      DATOS DEL ESTUDIANTE : \n\n
      Nombre : {estudiante.nombre}\n
      Edad : {estudiante.edad}\n
      Grado : {estudiante.grado}\n
  """)

estudiar =input()
if (estudiar.lower =="estudiar"):
    estudiante.estudiar()

