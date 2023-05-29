import tkinter as tk
from tkinter import ttk
import random
import matplotlib.pyplot as plt

equipos = ["Real Madrid", "Barcelona", "Atlético de Madrid", "Sevilla", "Real Sociedad", "Villarreal", "Betis", "Athletic Bilbao", "Granada", "Valencia", "Levante", "Celta de Vigo", "Osasuna", "Getafe", "Cádiz", "Alavés", "Eibar", "Valladolid", "Elche", "Huesca"]

# Definir puntos iniciales
puntos_iniciales = {equipo: 0 for equipo in equipos}

#Variables globales
puntos = {}
goleadores = {}

# Definir jugadores por equipo
jugadores_por_equipo = {
    "Real Madrid": ["Cristiano Ronaldo", "Karim Benzema", "Gareth Bale"],
    "Barcelona": ["Lionel Messi", "Antoine Griezmann", "Philippe Coutinho"],
    "Atlético de Madrid": ["Luis Suárez", "João Félix", "Ángel Correa"],
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
        habilidad_local = equipos_habilidades[local]
        habilidad_visitante = equipos_habilidades[visitante]
        resultado_local = random.randint(0, 5)
        resultado_visitante = random.randint(0, 5)
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
        for i in range(0, len(equipos), 2):
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
    
    
    # Código de simulación de temporada aquí
    
    # Simulación de una temporada
    for jornada in range(1, 37):
        equipos = equipos[1:] + [equipos[0]]
        simular_jornada(jornada, equipos, puntos, goleadores)
    
    # Obtener los puntos de los equipos en una lista
    #puntos_equipos = [puntos[equipo] for equipo in equipos]
    puntos_equipos = list(puntos.values())


    # Actualizar la tabla de posiciones
    tabla_posiciones.delete(*tabla_posiciones.get_children())
    clasificacion = sorted(puntos.items(), key=lambda x: x[1], reverse=True)
    for i, (equipo, puntos) in enumerate(clasificacion):
        tabla_posiciones.insert('', 'end', iid=i, values=(i+1, equipo, puntos))

    # Actualizar la tabla de goleadores
    tabla_goleadores.delete(*tabla_goleadores.get_children())
    goleadores_ordenados = []
    for equipo, jugadores in goleadores.items():
        for jugador, goles in jugadores.items():
            goleadores_ordenados.append((equipo, jugador, goles))
    goleadores_ordenados = sorted(goleadores_ordenados, key=lambda x: x[2], reverse=True)
    for i, (equipo, jugador, goles) in enumerate(goleadores_ordenados):
        tabla_goleadores.insert('', 'end', iid=i, values=(equipo, jugador, goles))
    
    # Crear el histograma de los puntos
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(puntos_equipos)), puntos_equipos, align='center', edgecolor='black')
    plt.xticks(range(len(equipos)), equipos, rotation=90)
    plt.xlabel('Equipos')
    plt.ylabel('Puntos')
    plt.title('Distribución de puntos de los equipos')
    plt.grid(axis='y', alpha=0.5)
    plt.tight_layout()
    plt.show()

   


    

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
