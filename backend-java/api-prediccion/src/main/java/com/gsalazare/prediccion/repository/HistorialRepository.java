package com.gsalazare.prediccion.repository;

import com.gsalazare.prediccion.model.HistorialPrediccion;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface HistorialRepository extends JpaRepository<HistorialPrediccion, Long> {
    // Hereda todos los métodos CRUD automáticos (save, findAll, deñete, etc.)
}