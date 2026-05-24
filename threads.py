import threading
import time
from predict import predecir_uso

def tarea_prediccion(id_hilo, nombre_carta, elixir, hp, rareza, grupo):
    print(f"[Hilo {id_hilo}] Analizando carta: {nombre_carta}...")
    # Simulamos un pequeño retraso de procesamiento
    time.sleep(1) 
    
    # Llamamos a la función del archivo predict.py
    uso_estimado = predecir_uso(elixir, hp, rareza, grupo)
    
    if isinstance(uso_estimado, str):
        print(f"[Hilo {id_hilo}] {uso_estimado}")
    else:
        print(f"[Hilo {id_hilo}] RESULTADO -> {nombre_carta}: Predicción de uso = {uso_estimado:.2f}%")

# Datos de prueba (Nombre, Elixir, HP, Rareza Numérica, EsGrupo)
datos_prueba = [
    ("Gigante Noble (Simulado)", 6, 3100, 1, 0),
    ("Duendes (Simulado)", 2, 200, 1, 1),
    ("Mega Caballero (Simulado)", 7, 4000, 4, 0),
    ("Bola de Fuego (Simulado)", 4, 0, 2, 0)
]

print("--- INICIANDO PREDICCIONES POR HILOS ---")
hilos = []

# Crear y lanzar los hilos
for i, datos in enumerate(datos_prueba):
    hilo = threading.Thread(target=tarea_prediccion, args=(i+1, *datos))
    hilos.append(hilo)
    hilo.start()

# Esperar a que todos los hilos terminen
for hilo in hilos:
    hilo.join()

print("--- TODAS LAS PREDICCIONES FINALIZARON ---")