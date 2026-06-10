Sistema de Predicción de Fútbol (Dispatch & AI)
Este proyecto es una plataforma integral para el análisis y predicción de resultados de partidos de fútbol. Utiliza una arquitectura de microservicios que combina el poder de procesamiento de datos de Python con la robustez de un backend en Java y una interfaz moderna en React.

🚀 Arquitectura del Proyecto
El sistema está dividido en tres módulos principales:

backend-java: Gestiona la lógica de negocio, usuarios y persistencia de datos (Spring Boot).

frontend-prediccion: Interfaz de usuario interactiva donde se consultan las predicciones (React).

ml-python: Motor de Inteligencia Artificial que procesa estadísticas y genera pronósticos (FastAPI).

🛠️ Tecnologías Utilizadas
Backend: Java, Spring Boot, H2 Database.

Frontend: React, JavaScript, CSS.

IA/ML: Python, Scikit-learn, Joblib.

Comunicación: API RESTful.

⚙️ Instrucciones de Instalación y Configuración
1. Requisitos Previos
Tener instalado Java 17+ y Maven.

Tener instalado Node.js (v18+) para el frontend.

Tener Python 3.10+ instalado.

2. Configuración de Modelos (Importante)
Debido a que los modelos de entrenamiento (.pkl) superan los 100MB, no se incluyen en este repositorio. Para ejecutar el sistema, realiza lo siguiente:

Descarga tus archivos modelo_ganador.pkl, modelo_futbol.pkl y modelo_goles.pkl.

Colócalos dentro de la carpeta ml-python/.

3. Ejecución
Backend: Navega a backend-java y ejecuta mvn spring-boot:run.

Frontend: Navega a frontend-prediccion, ejecuta npm install y luego npm start.

IA API: Navega a ml-python y ejecuta uvicorn main:app --reload.

🤝 Contribuciones
Este proyecto fue desarrollado por Gianfranco Salazar Espino (@gsalarzare). Si deseas contribuir o reportar un error, por favor abre un Issue en el repositorio.
