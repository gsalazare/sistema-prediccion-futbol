# ⚽ Sports Prediction IA (Dispatch & Analysis System)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Java](https://img.shields.io/badge/Java-17-blue.svg)](https://www.oracle.com/java/)
[![Python](https://img.shields.io/badge/Python-3.10-green.svg)](https://www.python.org/)

---

## 🏗️ Arquitectura del Sistema
Plataforma de ingeniería de software para la predicción de resultados deportivos mediante la integración de **IA**, servicios **Backend Java** y una interfaz en **React**.

| Módulo | Tecnología | Responsabilidad |
| :--- | :--- | :--- |
| **Backend API** | Java (Spring Boot) | Orquestación y persistencia |
| **Prediction Engine** | Python (FastAPI) | Procesamiento de modelos `.pkl` |
| **Frontend UI** | React | Interfaz de usuario dinámica |

[Imagen del diagrama de arquitectura de microservicios]

---

## 🔌 API Endpoints
El sistema expone los siguientes endpoints principales para la comunicación entre servicios:

- **GET** `/api/v1/predict` : Retorna la predicción calculada por el motor de IA.
- **POST** `/api/v1/dispatch` : Registra una nueva solicitud de despacho/análisis.
- **GET** `/api/v1/history` : Obtiene el historial de predicciones almacenadas en la base de datos H2.

---

## 🚀 Guía de Instalación

### 1. Requisitos de Entorno
* [Java JDK 17+](https://adoptium.net/) | [Maven](https://maven.apache.org/)
* [Python 3.10+](https://www.python.org/)
* [Node.js v18+](https://nodejs.org/)

### 2. Configuración de Modelos (IA)
Para habilitar las predicciones, coloca tus archivos de pesos en la carpeta `/ml-python/`:
- `modelo_ganador.pkl`
- `modelo_futbol.pkl`
- `modelo_goles.pkl`

> **Nota:** Estos archivos no se encuentran en el repositorio por exceder el límite de 100MB de GitHub.

### 3. Ejecución de Servicios
Levanta los servicios en el siguiente orden para asegurar la conectividad:

```bash
# 1. IA Engine
cd ml-python && uvicorn main:app --reload

# 2. Core Backend
cd backend-java && mvn spring-boot:run

# 3. Web Client
cd frontend-prediccion && npm install && npm start
```
---
## 💡 Stack Tecnológico
Para la construcción y mantenimiento de este sistema, se han seleccionado las siguientes tecnologías:

- **Persistence:** Base de datos H2 (In-Memory) para almacenamiento temporal eficiente.
- **API:** Arquitectura basada en endpoints RESTful para la comunicación entre servicios.
- **ML:** Scikit-learn para el entrenamiento e inferencia de los modelos de predicción.
- **UI:** Componentes funcionales en React para una experiencia de usuario interactiva.

---

## 👨‍💻 Autor

**Gianfranco Salazar Espino**

- [GitHub Profile](https://github.com/gsalarzare)

> *Este proyecto fue desarrollado bajo una arquitectura orientada a la eficiencia en el procesamiento de datos deportivos.*
