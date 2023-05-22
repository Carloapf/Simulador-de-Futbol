import tkinter as tk
from tkinter import ttk
import random
import matplotlib.pyplot as plt

equipos = ["Real Madrid", "Barcelona", "Atlético de Madrid", "Sevilla", "Real Sociedad", "Villarreal", "Betis", "Athletic Bilbao", "Granada", "Valencia", "Levante", "Celta de Vigo", "Osasuna", "Getafe", "Cádiz", "Alavés", "Eibar", "Valladolid", "Elche", "Huesca"]
puntos_iniciales = {equipo: 0 for equipo in equipos}

def iniciar_simulacion():
    habilidades = [85, 100, 80, 77, 75, 73, 71, 70, 68, 65, 63, 60, 58, 56, 54, 52, 50, 48, 46, 44]
    equipos_habilidades = dict(zip(equipos, habilidades))
    puntos = puntos_iniciales

    def simular_partido(local, visitante):
        habilidad_local = equipos_habilidades[local]
        habilidad_visitante = equipos_habilidades[visitante]
        goles_local = random.randint(0, min(habilidad_local, 5))
        goles_visitante = random.randint(0, min(habilidad_visitante, 5))
        return goles_local, goles_visitante

    def simular_jornada(jornada, equipos, puntos):
        print("Jornada", jornada)
        partidos = []
        for i in range(0, len(equipos), 2):
            local = equipos[i]
            visitante = equipos[i+1]
            goles_local, goles_visitante = simular_partido(local, visitante)
            partidos.append((local, visitante, goles_local, goles_visitante))
            if goles_local > goles_visitante:
                puntos[local] += 3
            elif goles_local < goles_visitante:
                puntos[visitante] += 3
            else:
                puntos[local] += 1
                puntos[visitante] += 1
        for partido in partidos:
            print(partido[0], partido[2], "-", partido[3], partido[1])
        print()

    def simular_temporada(equipos, puntos):
        for jornada in range(1, 39):
            random.shuffle(equipos)
            simular_jornada(jornada, equipos, puntos)

        clasificacion = sorted(puntos.items(), key=lambda x: x[1], reverse=True)
        print("Clasificación final:")
        for i, equipo in enumerate(clasificacion):
            print(i+1, equipo[0], equipo[1], "puntos")

        tabla.delete(*tabla.get_children())
        for i, equipo in enumerate(clasificacion):
            tabla.insert('', 'end', iid=i, values=(i+1, equipo[0], equipo[1]))

        equipos_grafica = [equipo for equipo, _ in clasificacion]
        puntos_grafica = [puntos for _, puntos in clasificacion]

        plt.bar(equipos_grafica, puntos_grafica)
        plt.xlabel('Equipos')
        plt.ylabel('Puntos')
        plt.title('Puntos obtenidos por equipo')
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()

    simular_temporada(equipos, puntos_iniciales)

ventana = tk.Tk()
ventana.title("Simulador de Temporada de Fútbol")
ventana.geometry("400x300")

etiqueta_titulo = tk.Label(ventana, text="Simulador de Temporada de Fútbol")
etiqueta_titulo.pack(pady=20)

boton_iniciar = tk.Button(ventana, text="Iniciar Simulación", command=iniciar_simulacion)
boton_iniciar.pack(pady=10)

tabla = ttk.Treeview(ventana, columns=('Posición', 'Equipo', 'Puntos'))
tabla.heading('Posición', text='Posición')
tabla.heading('Equipo', text='Equipo')
tabla.heading('Puntos', text='Puntos')
tabla.column('Posición', width=80, anchor='center')
tabla.column('Equipo', width=200)
tabla.column('Puntos', width=100, anchor='center')
tabla.pack(pady=20)

ventana.mainloop()
