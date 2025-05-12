class Celular():
    def __init__(self,marca,modelo,camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def llamar(self):
        print(f"Esta llamando desde {self.modelo}")

    def mostrar_camara(self):
        print(f"La resolucion de tu camara es de : {self.camara}")

     

celular1= Celular("Samsung","A32","48PM")
print(celular1.camara)







celular1.llamar()
celular1.mostrar_camara()








    