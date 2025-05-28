from src.laboratorio import Laboratorio
from src.sala_estudio import Sala_Estudio
from src.auditorio import Auditorio

if __name__ == "__main__":
    lab = Laboratorio(nombre="Lab Computo", capacidad=25, horario_disponible= [("08:00", "16:00")])
    sala = Sala_Estudio(nombre="Sala B", capacidad=20, horario_disponible= [("10:00", "15:00")])
    aud = Auditorio(nombre="Auditorio 1", capacidad=100, horario_disponible= [("14:00", "16:00")])

    print(lab)
    print(sala)
    print(aud)

    print("¿Esta disponible el Laboratorio a las 10:00?", lab.validar_disponibilidad("10:00"))
    print("¿Esta disponible la Sala de estudio a las 16:00?", sala.validar_disponibilidad("16:00"))
    print("¿Esta disponible el Auditorio a las 12:00?", aud.validar_disponibilidad("12:00"))