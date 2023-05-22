import tkinter as tk
from tkinter import ttk
import random
import matplotlib.pyplot as plt

equipos = ["Real Madrid", "Barcelona", "Atlético de Madrid", "Sevilla", "Real Sociedad", "Villarreal", "Betis", "Athletic Bilbao", "Granada", "Valencia", "Levante", "Celta de Vigo", "Osasuna", "Getafe", "Cádiz", "Alavés", "Eibar", "Valladolid", "Elche", "Huesca"]
# Definir puntos iniciales
puntos_iniciales = {equipo: 0 for equipo in equipos}

# Función para iniciar la simulación al presionar el botón
def iniciar_simulacion(equipos, puntos_iniciales):
    # Aquí colocarías el código para iniciar la simulación de la temporada de fútbol
    equipos = equipos
    puntos = puntos_iniciales
    # Definir equipos y sus habilidades
    
    habilidades = [85, 100, 80, 77, 75, 73, 71, 70, 68, 65, 63, 60, 58, 56, 54, 52, 50, 48, 46, 44]
    equipos_habilidades = dict(zip(equipos, habilidades))

    

    # Definir la función para simular un partido
    def simular_partido(local, visitante):
        habilidad_local = equipos_habilidades[local]
        habilidad_visitante = equipos_habilidades[visitante]
        resultado_local = random.randint(0, habilidad_local)
        resultado_visitante = random.randint(0, habilidad_visitante)
        if resultado_local > resultado_visitante:
            return local
        elif resultado_local < resultado_visitante:
            return visitante
        else:
            return "Empate"

    # Definir la función para simular una jornada
    def simular_jornada(jornada, equipos, puntos):
        print("Jornada", jornada)
        partidos = []
        for i in range(0, len(equipos), 2):
            local = equipos[i]
            visitante = equipos[i+1]
            resultado = simular_partido(local, visitante)
            partidos.append((local, visitante, resultado))
            if resultado == local:
                puntos[local] += 3
            elif resultado == visitante:
                puntos[visitante] += 3
            else:
                puntos[local] += 1
                puntos[visitante] += 1
        for partido in partidos:
            print(partido[0], partido[2], partido[1])
        print()

    # Definir la función para simular toda la temporada
    def simular_temporada(equipos, puntos):
        for jornada in range(1, 39):
            random.shuffle(equipos)
            simular_jornada(jornada, equipos, puntos)

        # Ordenar por puntos y mostrar la clasificación final
        clasificacion = sorted(puntos.items(), key=lambda x: x[1], reverse=True)
        print("Clasificación final:")
        for i, equipo in enumerate(clasificacion):
            print(i+1, equipo[0], equipo[1], "puntos")
             # Actualizar la tabla de posiciones
        for i, equipo in enumerate(clasificacion):
            tabla.item(i, values=(i+1, equipo[0],equipo[1]))
         # Crear la gráfica de barras
        equipos_grafica = [equipo for equipo, _ in clasificacion]
        puntos_grafica = [puntos for _, puntos in clasificacion]

        plt.bar(equipos_grafica, puntos_grafica)
        plt.xlabel('Equipos')
        plt.ylabel('Puntos')
        plt.title('Puntos obtenidos por equipo')
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()

    # Ejecutar la simulación de la temporada
    simular_temporada(equipos, puntos_iniciales)

    #for i in range(len(equipos)):
     #   tabla.item(i, values=(i+1, equipos[i], puntos[i]))



# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Simulador de Temporada de Fútbol")
ventana.geometry("400x300")

# Etiqueta de título
etiqueta_titulo = tk.Label(ventana, text="Simulador de Temporada de Fútbol")
etiqueta_titulo.pack(pady=20)

# Botón para iniciar la simulación
boton_iniciar = tk.Button(ventana, text="Iniciar Simulación", command=lambda: iniciar_simulacion(equipos, puntos_iniciales))
boton_iniciar.pack(pady=10)


# Crear tabla de posiciones
tabla = ttk.Treeview(ventana, columns=('Posición', 'Equipo', 'Puntos'))
tabla.heading('Posición', text='Posición')
tabla.heading('Equipo', text='Equipo')
tabla.heading('Puntos', text='Puntos')
tabla.column('Posición', width=80, anchor='center')
tabla.column('Equipo', width=200)
tabla.column('Puntos', width=100, anchor='center')

# Insertar datos de ejemplo en la tabla (puedes reemplazarlos con tus propios datos)
#equipos = ['-' for _ in range(len(equipos))]
puntos = [0 for _ in range(len(equipos))]
for i in range(len(equipos)):
    tabla.insert('', 'end', iid=i, values=(i+1, equipos[i], puntos[i]))
    tabla.pack(pady=20)

# Resultados de la simulación
#etiqueta_resultados = tk.Label(ventana, text="Resultados de la Simulación:")
#etiqueta_resultados.pack()

# Aquí puedes agregar widgets adicionales, como tablas o gráficos, para mostrar los resultados de la simulación.

# Ejecutar el bucle principal de la ventana
ventana.mainloop()



