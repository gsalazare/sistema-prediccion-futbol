package com.gsalazare.prediccion.service;

import com.gsalazare.prediccion.dto.PrediccionPythonResponse;
import com.gsalazare.prediccion.model.HistorialPrediccion;
import com.gsalazare.prediccion.repository.HistorialRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.time.LocalDateTime;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Service
public class PrediccionService {

    @Autowired
    private HistorialRepository historialRepository;

    // Herramienta de Java para hacer peticiones web
    private final RestTemplate restTemplate = new RestTemplate();

    public HistorialPrediccion obtenerYGuardarPrediccion(String idLocal, String idVisita) {
        // 1. Armamos el paquete que le enviaremos a Python
        String pythonUrl = "http://localhost:8000/predecir";
        Map<String, String> requestBody = new HashMap<>();
        requestBody.put("id_local", idLocal);
        requestBody.put("id_visita", idVisita);

        // 2. JAVA LLAMA A PYTHON (Hacemos el POST)
        PrediccionPythonResponse respuestaIA = restTemplate.postForObject(
                pythonUrl,
                requestBody,
                PrediccionPythonResponse.class
        );

        if (respuestaIA == null) {
            throw new RuntimeException("El motor de IA en Python no respondió.");
        }

        // 3. Extraemos los datos que nos devolvió Python
        String ganador = respuestaIA.getPrediccion_final().get("ganador");
        String goles = respuestaIA.getPrediccion_final().get("cantidad_goles");

        // 4. Guardamos todo en nuestra base de datos H2
        HistorialPrediccion nuevoRegistro = new HistorialPrediccion();
        nuevoRegistro.setEquipoLocal(respuestaIA.getEquipo_local());
        nuevoRegistro.setEquipoVisita(respuestaIA.getEquipo_visita());
        nuevoRegistro.setPrediccionGanador(ganador);
        nuevoRegistro.setPrediccionGoles(goles);
        nuevoRegistro.setFechaConsulta(LocalDateTime.now());

        return historialRepository.save(nuevoRegistro);
    }

    public List<HistorialPrediccion> obtenerTodoElHistorial() {
        return historialRepository.findAll();
    }
}