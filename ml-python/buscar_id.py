import joblib

# 1. Cargar el traductor que creó el modelo
encoder = joblib.load('encoder_equipos.pkl')

# 2. Lista de países que queremos buscar (en inglés)
paises_a_buscar = ['Peru', 'Argentina', 'Brazil', 'France', 'Chile', 'Colombia']

print("--- IDs para usar en Postman ---")
for pais in paises_a_buscar:
    try:
        # Busca el país y obtiene su ID
        id_pais = encoder.transform([pais])[0]
        print(f'"{pais}": {id_pais}')
    except Exception as e:
        print(f'No se encontró el país: {pais}. Revisa cómo está escrito.')