# Predicción de Uso de Cartas - Clash Royale (Machine Learning)

## Descripción General
Este proyecto implementa un modelo de Machine Learning (Random Forest) para predecir el porcentaje de uso (`usage`) de una carta de Clash Royale en base a sus estadísticas. Es una adaptación del ejemplo de "Calidad de Agua".

El modelo toma en cuenta 4 variables (columnas) para realizar la predicción:
1. `elixirCost`: Costo de elixir de la carta.
2. `hitpoints`: Puntos de vida (0 para hechizos).
3. `rarity_num`: Nivel de rareza mapeado a números (1=Común a 5=Campeón).
4. `groupCard_num`: Si la carta invoca a múltiples tropas (1=Sí, 0=No).

## Estructura del Proyecto
* `clash_royale_cards.csv`: Dataset original con las estadísticas de las cartas.
* `trainer.py`: Script responsable de limpiar los datos, mapear valores categóricos y entrenar el modelo exportándolo a un archivo `.pkl`.
* `predict.py`: Contiene la función que recibe las 4 variables de una carta y devuelve la predicción usando el modelo guardado.
* `threads.py`: Archivo principal de ejecución que simula peticiones concurrentes (hilos) para predecir el uso de distintas cartas al mismo tiempo.

## Cómo ejecutar desde cero

1. **Instalar dependencias:**
   Asegúrate de tener instalado Python y las librerías necesarias. Puedes instalarlas ejecutando:
   `pip install pandas scikit-learn joblib`

2. **Entrenar el modelo:**
   Antes de predecir, necesitas generar el modelo. Ejecuta en tu terminal:
   `python trainer.py`
   *(Esto generará un archivo llamado `modelo_clash.pkl`)*

3. **Ejecutar las predicciones con Hilos:**
   Para ver el modelo en acción utilizando múltiples hilos, ejecuta:
   `python threads.py`
