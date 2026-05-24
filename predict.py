import joblib
import pandas as pd
import warnings
warnings.filterwarnings("ignore", category=UserWarning) # Ocultar warnings de sklearn

def predecir_uso(elixir, hitpoints, rarity_num, group_card):
    """
    Recibe las 4 variables y retorna la predicción de uso.
    Rareza: 1=Común, 2=Especial, 3=Épica, 4=Legendaria, 5=Campeón
    Grupo: 0=Falso, 1=Verdadero
    """
    try:
        # Cargar el modelo
        modelo = joblib.load('modelo_clash.pkl')
        
        # Crear un DataFrame con los datos de entrada
        datos = pd.DataFrame([[elixir, hitpoints, rarity_num, group_card]], 
                             columns=['elixirCost', 'hitpoints', 'rarity_num', 'groupCard_num'])
        
        # Predecir
        prediccion = modelo.predict(datos)
        return prediccion[0]
    except FileNotFoundError:
        return "Error: No se encontró el modelo. Ejecuta trainer.py primero."