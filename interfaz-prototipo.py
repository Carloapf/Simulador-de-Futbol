import tkinter as tk
from tkinter import ttk
import random
import matplotlib.pyplot as plt
import sys
import os
import numpy as np
import pandas as pd
import seaborn as sns

#Obtenemos informacion de la base de datos
laliga=pd.read_csv('C:\\Users\\carlo\\Documents\\codigos\\python\\proyecto\\LaLiga_Matches_1995-2021.csv')
laliga.head()
laliga.shape

laliga20_21=laliga[laliga['Season']=='2020-21'].drop(['Season'],axis=1)
laliga19_20=laliga[laliga['Season']=='2019-20'].drop(['Season'],axis=1)
laliga18_19=laliga[laliga['Season']=='2018-19'].drop(['Season'],axis=1)
laliga17_18=laliga[laliga['Season']=='2017-18'].drop(['Season'],axis=1)
laliga16_17=laliga[laliga['Season']=='2016-17'].drop(['Season'],axis=1)

class StdoutRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, message):
        self.text_widget.insert("end", message)
        self.text_widget.see("end")

equipos = ["Real Madrid", "Barcelona", "Atlético de Madrid", "Sevilla", "Real Sociedad", "Villarreal", "Betis", "Athletic Bilbao", "Granada", "Valencia", "Levante", "Celta de Vigo", "Osasuna", "Getafe", "Cádiz", "Alavés", "Eibar", "Valladolid", "Elche", "Huesca"]

# Definir puntos iniciales
puntos_iniciales = {equipo: 0 for equipo in equipos}

#Variables globales
puntos = {}
goleadores = {}

# Definir jugadores por equipo
jugadores_por_equipo = {
    "Real Madrid": ["Vinicius", "Karim Benzema", "Rodrygo"],
    "Barcelona": ["Robert Lewandowski", "Dembele", "Raphinha"],
    "Atlético de Madrid": ["Memphis", "João Félix", "Ángel Correa"],
    "Sevilla":["Tecatito","Youssef En-Nesyri","Suso"],
    "Real Sociedad":["Kubo","Mikel Oyarzabal","Carlos Fernadez"],
    "Villarreal": ["Gerard Moreno","Manu Trigeros","Yeremi Pino"],
    "Betis": ["Joaquin","Borja Iglesias","Willian Jose"], 
    "Athletic Bilbao": ["Raul Garcia","Nico Williams","Iñaki Williams"], 
    "Granada": ["Alberto Soro","Antonio Puertas","Ruben Rochina"], 
    "Valencia": ["Fran Perez", "Marcos Andre", "Edinson Cavani"], 
    "Levante": ["Roberto Soldado", "Mohamed Bouldini", "Jorge Frutos"], 
    "Celta de Vigo": ["Iago Aspas", "Carles Perez", "Goncalo Paciencia"], 
    "Osasuna": ["Abde Ezzalzouli", "Ruben Garcia", "Chimy Avila"], 
    "Getafe": ["Portu", "Borja Mayoral", "Jaime Mata"], 
    "Cádiz": ["Alvaro Negredo", "Ruben Sobrino", "Anthony Lozano"],
    "Alavés": ["Miguel de la Fuente", "Luis Roja", "Jason"], 
    "Eibar": ["Jon Bautista", "José Corpas", "Gustavo Blanco Leschuk"], 
    "Valladolid": ["Gonzalo Plata", "Kenedy", "Sergio Leon"], 
    "Elche": ["Alex Collado", "Ezequiel Ponce", "Josan"], 
    "Huesca":["Abou Kante", "Jose Angel Carrillo", "Patrick Soko"]
}

# Definir goleadores por equipo
goleadores = {equipo: {jugador: 0 for jugador in jugadores} for equipo, jugadores in jugadores_por_equipo.items()}

# Función para iniciar la simulación al presionar el botón
def iniciar_simulacion():
    # Aquí colocarías el código para iniciar la simulación de la temporada de fútbol
    global goleadores
    equipos = list(puntos_iniciales.keys())
    puntos = dict(puntos_iniciales)
    goleadores = {equipo: {jugador: 0 for jugador in jugadores_por_equipo[equipo]} for equipo in equipos}

    # Definir habilidades de los equipos y jugadores
    habilidades = [85, 100, 80, 77, 75, 73, 71, 70, 68, 65, 63, 60, 58, 56, 54, 52, 50, 48, 46, 44]
    equipos_habilidades = dict(zip(equipos, habilidades))

    def simular_partido(local, visitante):
        #habilidad_local = equipos_habilidades[local]
        #habilidad_visitante = equipos_habilidades[visitante]

        habilidad_local = random.randint(0, equipos_habilidades[local])
        habilidad_visitante = random.randint(0, equipos_habilidades[visitante])
        diff = 0

        if (habilidad_local + 8) > habilidad_visitante:
            resultado_local = random.randint(1, 5)
            diff = random.randint(1,3)
            resultado_visitante = resultado_local - diff
            if resultado_visitante < 0:
                resultado_visitante = max(resultado_visitante, 0)

        elif (habilidad_visitante + 8) > habilidad_local:
            resultado_visitante = random.randint(1, 5)
            diff = random.randint(1,3)
            resultado_local = resultado_visitante - diff
            if resultado_local < 0:
                 resultado_local = max(resultado_local, 0)
        elif (habilidad_local):
            diff = random.randint(0,3)
            resultado_local, resultado_visitante = diff

        #resultado_local = random.randint(0, 5)
        #resultado_visitante = random.randint(0, 5)
        #print(resultado_local,"y",resultado_visitante)
        if resultado_local > resultado_visitante:
            return local, resultado_local, resultado_visitante
        elif resultado_local < resultado_visitante:
            return visitante, resultado_local, resultado_visitante
        else:
            return "Empate" ,resultado_local, resultado_visitante
        
    def simular_jornada(jornada, equipos, puntos, goleadores):
        print("Jornada", jornada)
        partidos = []
        e =[]
        for i in range(0, len(equipos), 2):
            equipo_local = equipos[i]
            equipo_visitante = equipos[i+1]


            partido = laliga[(laliga['HomeTeam'] == equipo_local) & (laliga['AwayTeam'] == equipo_visitante)]

            try:
                if partido['FTHG'].values[0] > partido['FTAG'].values[0]:
                    res = equipo_local
                elif partido['FTHG'].values[0] < partido['FTAG'].values[0]:
                    res = equipo_visitante
                else:
                    res = "Empate"
            except:
                error = e
            
            

            local = equipos[i]
            visitante = equipos[i+1]
            resultado, goles_local, goles_visitante = simular_partido(local, visitante)
            partidos.append((local, visitante, resultado))
            if resultado == local:
                puntos[local] += 3
                for _ in range(3):
                    goleador_local = random.choice(jugadores_por_equipo[local])
                    goleadores[local][goleador_local] += 1
            elif resultado == visitante:
                puntos[visitante] += 3
                for _ in range(3):
                    goleador_visitante = random.choice(jugadores_por_equipo[visitante])
                    goleadores[visitante][goleador_visitante] += 1
            else:
                puntos[local] += 1
                puntos[visitante] += 1
                for _ in range(3):
                    goleador_local = random.choice(jugadores_por_equipo[local])
                    goleador_visitante = random.choice(jugadores_por_equipo[visitante])
                    goleadores[local][goleador_local] += 1
                    goleadores[visitante][goleador_visitante] += 1
       
            print(local, goles_local, goles_visitante, visitante)
        print()
        equipos = [partido[0] if partido[2] == partido[0] else partido[1] if partido[2] == partido[1] else partido[0] for partido in partidos]

    
    
    # Código de simulación de temporada aquí
    
    # Simulación de una temporada
    for jornada in range(1, 37):
        equipos = equipos[1:] + [equipos[0]]
        simular_jornada(jornada, equipos, puntos, goleadores)
    
    # Determinar el equipo campeón
    campeon = max(puntos, key=puntos.get)

    #puntos_equipos = list(puntos.values())
    puntos_equipos = [puntos[equipo] for equipo in equipos]
    puntos_equipos = sorted(puntos_equipos, reverse=True)
    nombres_equipos = [equipo for equipo, _ in sorted(puntos.items(), key=lambda x: x[1], reverse=True)]

    # Obtener el índice de la fila del campeón
    indice_campeon = nombres_equipos.index(campeon)

    # Actualizar la tabla de posiciones
    tabla_posiciones.delete(*tabla_posiciones.get_children())
    clasificacion = sorted(puntos.items(), key=lambda x: x[1], reverse=True)
    for i, (equipo, puntos) in enumerate(clasificacion):
        etiqueta = (i+1, equipo, puntos)
        tags = ('campeon', 'top4', 'normal') if i == 0 else ('top4', 'normal') if 1 <= i <= 3 else ('normal',)
        #tags = ('campeon', 'top4', 'normal') if i < 4 else ('normal',)
        tabla_posiciones.insert('', 'end', iid=i, values=etiqueta, tags=tags)
        
        # Resaltar la fila del campeón
        tabla_posiciones.tag_configure('campeon', background='yellow')
        tabla_posiciones.tag_configure('top4', background='cyan')
        tabla_posiciones.tag_configure('normal', background='white')

    
    
    # Actualizar la tabla de goleadores
    tabla_goleadores.delete(*tabla_goleadores.get_children())
    goleadores_ordenados = []
    for equipo, jugadores in goleadores.items():
        for jugador, goles in jugadores.items():
            goleadores_ordenados.append((equipo, jugador, goles))
    goleadores_ordenados = sorted(goleadores_ordenados, key=lambda x: x[2], reverse=True)
    for i, (equipo, jugador, goles) in enumerate(goleadores_ordenados):
        tabla_goleadores.insert('', 'end', iid=i, values=(equipo, jugador, goles))
    # Obtener los puntos de los equipos en una lista
    
    

    # Crear el histograma de los puntos
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(puntos_equipos)), puntos_equipos, align='center', edgecolor='black')
    plt.xticks(range(len(puntos_equipos)), nombres_equipos, rotation=90)
    plt.xlabel('Equipos')
    plt.ylabel('Puntos')
    plt.title('Distribución de puntos de los equipos')
    plt.grid(axis='y', alpha=0.5)
    plt.tight_layout()
    plt.show()

   


# Crear una ventana secundaria para mostrar la salida de la consola
ventana_secundaria = tk.Toplevel()
ventana_secundaria.title("Consola")
ventana_secundaria.geometry("800x600")

# Crear un widget de texto para mostrar la salida de la consola
texto_consola = tk.Text(ventana_secundaria)
texto_consola.pack()

# Redirigir la salida de la consola al widget de texto
sys.stdout = StdoutRedirector(texto_consola)


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Simulador de Temporada de Fútbol")
ventana.geometry("800x800")

# Etiqueta de título
etiqueta_titulo = tk.Label(ventana, text="Simulador de Temporada de Fútbol")
etiqueta_titulo.pack(pady=20)

# Botón para iniciar la simulación
boton_iniciar = tk.Button(ventana, text="Iniciar Simulación", command=iniciar_simulacion)
boton_iniciar.pack(pady=10)

# Crear tabla de posiciones
tabla_posiciones = ttk.Treeview(ventana, columns=('Posición', 'Equipo', 'Puntos'))
tabla_posiciones.heading('Posición', text='Posición')
tabla_posiciones.heading('Equipo', text='Equipo')
tabla_posiciones.heading('Puntos', text='Puntos')
tabla_posiciones.column('Posición', width=80, anchor='center')
tabla_posiciones.column('Equipo', width=200)
tabla_posiciones.column('Puntos', width=100, anchor='center')
tabla_posiciones.pack(pady=20)

# Crear tabla de goleadores
tabla_goleadores = ttk.Treeview(ventana, columns=('Equipo', 'Jugador', 'Goles'))
tabla_goleadores.heading('Equipo', text='Equipo')
tabla_goleadores.heading('Jugador', text='Jugador')
tabla_goleadores.heading('Goles', text='Goles')
tabla_goleadores.column('Equipo', width=200)
tabla_goleadores.column('Jugador', width=200)
tabla_goleadores.column('Goles', width=80, anchor='center')
tabla_goleadores.pack(pady=20)



# Ejecutar la ventana principal
ventana.mainloop()

# Mostrar la ventana secundaria
ventana_secundaria.mainloop()