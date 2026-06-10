from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import time
import joblib  # Asumo que usas joblib o pickle para cargar tus .pkl
import pandas as pd # Asumo que tus modelos leen DataFrames (si usas numpy, puedes adaptarlo)

# 1. INICIALIZAR LA APLICACIÓN Y MODELOS
app = FastAPI(title="Motor de Predicción de Fútbol IA")

print("Cargando cerebros matemáticos...")
try:
    # Asegúrate de que estos nombres coincidan con los archivos de tu carpeta
    modelo_ganador = joblib.load("modelo_ganador.pkl")
    modelo_goles = joblib.load("modelo_goles.pkl")
    print("✅ Modelos cargados correctamente.")
except Exception as e:
    print(f"⚠️ Advertencia: No se pudieron cargar los modelos .pkl. Error: {e}")

# 2. CONFIGURACIÓN DE LA API DE SOFASCORE
API_KEY = "0b4d9548e2mshe02db975955b101p12d246jsn58a4ba9cbc12" # <--- ¡Pega tu llave real aquí!
HEADERS = {
    "x-rapidapi-host": "sofascore-api4.p.rapidapi.com",
    "x-rapidapi-key": API_KEY
}

# 3. DEFINIR LO QUE JAVA NOS VA A ENVIAR (LOS IDs)
class SolicitudPrediccion(BaseModel):
    id_local: str
    id_visita: str

# 4. LA FUNCIÓN EXTRACTORA (Tus "Ojos" en internet)
def analizar_equipo(equipo_id):
    url = f"https://sofascore-api4.p.rapidapi.com/teams/{equipo_id}/events/last/0"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        return None

    datos = response.json()
    partidos = datos.get('events', [])

    if len(partidos) == 0:
        return None

    goles_anotados = 0
    goles_recibidos = 0
    partidos_validos = 0
    nombre_equipo = "Desconocido"

    for partido in partidos:
        try:
            es_local = str(partido['homeTeam']['id']) == str(equipo_id)
            if es_local:
                nombre_equipo = partido['homeTeam']['name']
                goles_anotados += partido['homeScore']['current']
                goles_recibidos += partido['awayScore']['current']
            else:
                nombre_equipo = partido['awayTeam']['name']
                goles_anotados += partido['awayScore']['current']
                goles_recibidos += partido['homeScore']['current']
            partidos_validos += 1
        except KeyError:
            continue

    if partidos_validos == 0:
        return None

    return {
        "nombre": nombre_equipo,
        "promedio_anotados": round(goles_anotados / partidos_validos, 2),
        "promedio_recibidos": round(goles_recibidos / partidos_validos, 2)
    }

# 5. EL ENDPOINT PRINCIPAL (El "Cerebro")
@app.post("/predecir")
def predecir_partido(solicitud: SolicitudPrediccion):
    print(f"\n📡 Petición recibida para Local ID: {solicitud.id_local} vs Visita ID: {solicitud.id_visita}")

    # --- FASE 1: EXTRACCIÓN DE DATOS EN VIVO ---
    stats_local = analizar_equipo(solicitud.id_local)
    time.sleep(1.5) # Pausa de seguridad para SofaScore
    stats_visita = analizar_equipo(solicitud.id_visita)

    if not stats_local or not stats_visita:
        raise HTTPException(status_code=400, detail="No se pudieron obtener datos suficientes de SofaScore para estos equipos.")

    # --- FASE 2: PREPARAR LOS DATOS PARA LA IA ---
    # Creamos el formato exacto que tus modelos .pkl aprendieron a leer
    datos_para_modelo = pd.DataFrame([{
        "goles_anotados_local": stats_local['promedio_anotados'],
        "goles_recibidos_local": stats_local['promedio_recibidos'],
        "goles_anotados_visita": stats_visita['promedio_anotados'],
        "goles_recibidos_visita": stats_visita['promedio_recibidos']
    }])

    # --- FASE 3: LA PREDICCIÓN MATEMÁTICA ---
    try:
        # Aquí la magia: Le pasamos los datos frescos a los modelos
        prediccion_ganador = modelo_ganador.predict(datos_para_modelo)[0]
        prediccion_goles = modelo_goles.predict(datos_para_modelo)[0]
    except Exception as e:
        # Si falla porque el modelo aún no está conectado, simulamos una respuesta
        print(f"⚠️ Error al usar los modelos .pkl: {e}. Enviando predicción calculada a mano.")
        fuerza_local = stats_local['promedio_anotados'] - stats_local['promedio_recibidos']
        fuerza_visita = stats_visita['promedio_anotados'] - stats_visita['promedio_recibidos']

        prediccion_ganador = "Gana Local" if fuerza_local > fuerza_visita else "Gana Visita"
        prediccion_goles = "Más de 2.5 Goles" if (stats_local['promedio_anotados'] + stats_visita['promedio_anotados']) > 2.5 else "Menos de 2.5 Goles"

    # --- FASE 4: DEVOLVER EL RESULTADO A JAVA (O Postman) ---
    return {
        "equipo_local": stats_local['nombre'],
        "equipo_visita": stats_visita['nombre'],
        "estadisticas_usadas": {
            "local": stats_local,
            "visita": stats_visita
        },
        "prediccion_final": {
            "ganador": prediccion_ganador,
            "cantidad_goles": prediccion_goles
        }
    }