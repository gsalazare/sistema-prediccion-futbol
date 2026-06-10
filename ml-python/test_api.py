import requests
import time

# Tus credenciales
API_KEY = "0b4d9548e2mshe02db975955b101p12d246jsn58a4ba9cbc12"
HEADERS = {
    "x-rapidapi-host": "sofascore-api4.p.rapidapi.com",
    "x-rapidapi-key": API_KEY
}

# ⚽ Asegúrate de usar IDs reales que hayas encontrado con el buscador
ID_LOCAL = "2302" # Sporting Cristal
ID_VISITA = "3202" # <--- ¡CÁMBIA ESTO POR UN ID REAL! (Ej. Universitario, Alianza, Boca...)

def analizar_equipo(equipo_id):
    url = f"https://sofascore-api4.p.rapidapi.com/teams/{equipo_id}/events/last/0"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        print(f"⚠️ Error HTTP {response.status_code} para el ID {equipo_id}: {response.text}")
        return None

    datos = response.json()
    partidos = datos.get('events', [])

    # 🔍 LOS RAYOS X: Verificamos si SofaScore nos mandó datos vacíos
    if len(partidos) == 0:
        print(f"⚠️ ¡Alerta! El ID {equipo_id} no tiene ningún partido registrado en SofaScore.")
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
        "promedio_recibidos": round(goles_recibidos / partidos_validos, 2),
        "partidos_analizados": partidos_validos
    }

print("🤖 Extrayendo datos frescos y calculando métricas...\n")

stats_local = analizar_equipo(ID_LOCAL)

print("⏳ Pausando 2 segundos para respetar los límites del servidor...")
time.sleep(2)

stats_visita = analizar_equipo(ID_VISITA)

if stats_local and stats_visita:
    print(f"\n📊 ANÁLISIS PRE-PARTIDO: {stats_local['nombre']} vs {stats_visita['nombre']}")
    print("-" * 60)
    print(f"🏟️ LOCAL ({stats_local['nombre']} - Últimos {stats_local['partidos_analizados']} partidos):")
    print(f"   ➤ Promedio de goles a favor:  {stats_local['promedio_anotados']} por partido")
    print(f"   ➤ Promedio de goles en contra: {stats_local['promedio_recibidos']} por partido\n")

    print(f"✈️ VISITA ({stats_visita['nombre']} - Últimos {stats_visita['partidos_analizados']} partidos):")
    print(f"   ➤ Promedio de goles a favor:  {stats_visita['promedio_anotados']} por partido")
    print(f"   ➤ Promedio de goles en contra: {stats_visita['promedio_recibidos']} por partido")
    print("-" * 60)

    fuerza_local = stats_local['promedio_anotados'] - stats_local['promedio_recibidos']
    fuerza_visita = stats_visita['promedio_anotados'] - stats_visita['promedio_recibidos']

    print("🏆 CONCLUSIÓN MATEMÁTICA INICIAL:")
    if fuerza_local > fuerza_visita:
        print(f"   El momentum estadístico favorece al LOCAL ({stats_local['nombre']}).")
    elif fuerza_visita > fuerza_local:
        print(f"   El momentum estadístico favorece a la VISITA ({stats_visita['nombre']}).")
    else:
        print("   Fuerzas extremadamente parejas. Alta probabilidad de partido cerrado/empate.")
else:
    print("\n❌ Análisis abortado por falta de datos en alguno de los equipos.")