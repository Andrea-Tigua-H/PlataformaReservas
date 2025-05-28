#      Integrantes:
#Tigua Holguin Nicole Andrea
#Mite Reyes Maira Alejandra
#Rodriguez Llamuca Alexandro Steven
#Viteri Roca Helen Adriana


from src.espacio import Espacio

# Clase Sala_Estudio:
# Representa una sala de estudio en la universidad. Hereda de Espacio.
class Sala_Estudio(Espacio):
    def validar_disponibilidad(self, hora):
        return super().validar_disponibilidad(hora) # Utiliza la validacion definida en la superclase.

# Pruebas individuales para Sala_Estudio
if __name__ == "__main__":
    sala = Sala_Estudio(nombre= "Sala D", capacidad= 12, horario_disponible= [("10:00", "15:00")])
    print("Prueba 1 - Disponible a las 12:00 :", sala.validar_disponibilidad("12:00"))
    print("Prueba 2 - Disponible a las 18:00 :", sala.validar_disponibilidad("18:00"))