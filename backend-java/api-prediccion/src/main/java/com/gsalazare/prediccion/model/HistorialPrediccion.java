package com.gsalazare.prediccion.model;

import jakarta.persistence.*;

import java.time.LocalDateTime;

@Entity
@Table(name = "historial_predicciones")
public class HistorialPrediccion {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String equipoLocal;
    private String equipoVisita;
    private String prediccionGanador;
    private String prediccionGoles;
    private LocalDateTime fechaConsulta;

    // Hibernate necesita un constructor vacío obligatorio
    public HistorialPrediccion() {
    }

    // Constructor para registrar datos fácilmente
    public HistorialPrediccion(String equipoLocal, String equipoVisita, String prediccionGanador, String prediccionGoles) {
        this.equipoLocal = equipoLocal;
        this.equipoVisita = equipoVisita;
        this.prediccionGanador = prediccionGanador;
        this.prediccionGoles = prediccionGoles;
        this.fechaConsulta = LocalDateTime.now();
    }

    // Getters y Setters para que JPA pueda mapear los campos
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getEquipoLocal() {
        return equipoLocal;
    }

    public void setEquipoLocal(String equipoLocal) {
        this.equipoLocal = equipoLocal;
    }

    public String getEquipoVisita() {
        return equipoVisita;
    }

    public void setEquipoVisita(String equipoVisita) {
        this.equipoVisita = equipoVisita;
    }

    public String getPrediccionGanador() {
        return prediccionGanador;
    }

    public void setPrediccionGanador(String prediccionGanador) {
        this.prediccionGanador = prediccionGanador;
    }

    public String getPrediccionGoles() {
        return prediccionGoles;
    }

    public void setPrediccionGoles(String prediccionGoles) {
        this.prediccionGoles = prediccionGoles;
    }

    public LocalDateTime getFechaConsulta() {
        return fechaConsulta;
    }

    public void setFechaConsulta(LocalDateTime fechaConsulta) {
        this.fechaConsulta = fechaConsulta;
    }
}