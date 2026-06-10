import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

print("1. Cargando los archivos de Kaggle...")
df_results = pd.read_csv('results.csv')
df_shootouts = pd.read_csv('shootouts.csv')
# (Nota: goalscorers.csv lo dejamos listo en la carpeta para futuras métricas de jugadores)

# Limpieza básica
df_results = df_results.dropna(subset=['home_score', 'away_score'])

print("2. Fusión de Datos (Data Merging) con Penales...")
# Unimos los resultados principales con la tabla de penales usando la fecha y los equipos
df_completo = pd.merge(df_results, df_shootouts, on=['date', 'home_team', 'away_team'], how='left')

def determinar_resultado_real(fila):
    # Evaluamos quién ganó en los 90 minutos
    if fila['home_score'] > fila['away_score']:
        return 1 # Gana Local
    elif fila['home_score'] < fila['away_score']:
        return 2 # Gana Visita
    else:
        # Si empataron, la Inteligencia Artificial revisa si hubo tanda de penales
        if pd.notna(fila['winner']):
            if fila['winner'] == fila['home_team']:
                return 1 # Gana Local (en penales)
            else:
                return 2 # Gana Visita (en penales)
        return 0 # Empate definitivo (sin penales)

df_completo['resultado'] = df_completo.apply(determinar_resultado_real, axis=1)

print("3. Creando el Segundo Objetivo (Predicción de Goles - Over/Under)...")
# Calculamos la suma total de goles por partido
df_completo['total_goles'] = df_completo['home_score'] + df_completo['away_score']
# Si hubo más de 2 goles = 1 (Over), si hubo 2 o menos = 0 (Under)
df_completo['mas_de_2_goles'] = (df_completo['total_goles'] > 2.5).astype(int)

print("4. Convirtiendo países a números (IDs)...")
encoder = LabelEncoder()
todos_los_equipos = pd.concat([df_completo['home_team'], df_completo['away_team']])
encoder.fit(todos_los_equipos)

df_completo['equipo_local_id'] = encoder.transform(df_completo['home_team'])
df_completo['equipo_visita_id'] = encoder.transform(df_completo['away_team'])

print("5. Entrenando MOTOR 1 (Quién ganará el partido)...")
X = df_completo[['equipo_local_id', 'equipo_visita_id']]
y_ganador = df_completo['resultado']
modelo_ganador = RandomForestClassifier(n_estimators=100, random_state=42)
modelo_ganador.fit(X, y_ganador)

print("6. Entrenando MOTOR 2 (Cantidad de goles)...")
y_goles = df_completo['mas_de_2_goles']
modelo_goles = RandomForestClassifier(n_estimators=100, random_state=42)
modelo_goles.fit(X, y_goles)

print("7. Guardando ambos cerebros artificiales...")
# Ahora guardamos dos modelos separados y el diccionario
joblib.dump(modelo_ganador, 'modelo_ganador.pkl')
joblib.dump(modelo_goles, 'modelo_goles.pkl')
joblib.dump(encoder, 'encoder_equipos.pkl')

print("¡Éxito absoluto! Tu sistema ahora es capaz de predecir el ganador y la cantidad de goles.")