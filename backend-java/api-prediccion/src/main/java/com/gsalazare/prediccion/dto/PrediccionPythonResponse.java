package com.gsalazare.prediccion.dto;

import java.util.Map;

public class PrediccionPythonResponse {
    private String equipo_local;
    private String equipo_visita;
    private Map<String, String> prediccion_final;

    // Getters y Setters
    public String getEquipo_local() { return equipo_local; }
    public void setEquipo_local(String equipo_local) { this.equipo_local = equipo_local; }

    public String getEquipo_visita() { return equipo_visita; }
    public void setEquipo_visita(String equipo_visita) { this.equipo_visita = equipo_visita; }

    public Map<String, String> getPrediccion_final() { return prediccion_final; }
    public void setPrediccion_final(Map<String, String> prediccion_final) { this.prediccion_final = prediccion_final; }
}