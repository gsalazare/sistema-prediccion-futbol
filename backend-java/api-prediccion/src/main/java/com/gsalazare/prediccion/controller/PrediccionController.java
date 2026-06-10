package com.gsalazare.prediccion.controller;

import com.gsalazare.prediccion.model.HistorialPrediccion;
import com.gsalazare.prediccion.service.PrediccionService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/partidos")
@Tag(name = "Motor de Predicción", description = "Endpoints para la gestión e interacción con los modelos de IA y SofaScore")
public class PrediccionController {

    @Autowired
    private PrediccionService prediccionService;

    @PostMapping("/analizar")
    @Operation(
            summary = "Predecir un partido",
            description = "Recibe los IDs de dos equipos (Local y Visita), consulta su estado actual en SofaScore y utiliza modelos de IA (Python) para predecir el ganador y la cantidad de goles."
    )
    public HistorialPrediccion analizarPartido(@RequestBody Map<String, String> equiposIds) {
        // Extraemos los IDs que nos envía el cliente (Postman, Android o Web)
        String idLocal = equiposIds.get("idLocal");
        String idVisita = equiposIds.get("idVisita");

        // Delegamos todo el trabajo pesado al Servicio
        return prediccionService.obtenerYGuardarPrediccion(idLocal, idVisita);
    }

    @GetMapping("/historial")
    @Operation(
            summary = "Obtener el historial",
            description = "Devuelve todos los análisis y predicciones previas que han sido guardadas en la base de datos H2."
    )
    public List<HistorialPrediccion> verHistorial() {
        return prediccionService.obtenerTodoElHistorial();
    }
}