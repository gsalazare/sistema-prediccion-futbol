package com.gsalazare.prediccion.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class WebConfig implements WebMvcConfigurer {

    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/**") // Aplica para todas las rutas
                .allowedOrigins("http://localhost:3000") // Permite el origen de React
                .allowedMethods("GET", "POST", "PUT", "DELETE", "OPTIONS") // Permite todos los verbos
                .allowedHeaders("*"); // Permite todos los headers
    }
}