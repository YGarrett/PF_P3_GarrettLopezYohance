import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# 1. Cargar los datos (Asegúrate de que tu CSV se llame así)
df = pd.read_csv('clash_royale_cards.csv')

# 2. Preprocesamiento de datos
# Llenar los hitpoints vacíos (como los hechizos) con 0
df['hitpoints'] = df['hitpoints'].fillna(0)

# Convertir rareza a valores numéricos
rarity_map = {'common': 1, 'rare': 2, 'epic': 3, 'legendary': 4, 'champion': 5}
df['rarity_num'] = df['rarity'].map(rarity_map)

# Convertir booleanos (groupCard) a 0 y 1
df['groupCard_num'] = df['groupCard'].astype(int)

# 3. Definir variables independientes (X) y dependiente (y)
X = df[['elixirCost', 'hitpoints', 'rarity_num', 'groupCard_num']]
y = df['usage']

# 4. Dividir en datos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Entrenar el modelo
print("Entrenando el modelo...")
modelo = RandomForestRegressor(random_state=42)
modelo.fit(X_train, y_train)

# 6. Guardar el modelo entrenado
joblib.dump(modelo, 'modelo_clash.pkl')
print("Modelo guardado exitosamente como 'modelo_clash.pkl'")