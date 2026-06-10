package com.gsalazare.prediccion.config;

import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.info.Contact;
import io.swagger.v3.oas.models.info.Info;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class SwaggerConfig {

    @Bean
    public OpenAPI customOpenAPI() {
        return new OpenAPI()
                .info(new Info()
                        .title("API del Sistema de Predicción Deportiva con IA")
                        .version("1.0")
                        .description("Esta API permite analizar y predecir resultados de fútbol integrando modelos de Machine Learning (Python/FastAPI) y datos en tiempo real (SofaScore).")
                        .contact(new Contact()
                                .name("Gianfranco Salazar")
                                .email("tu.correo@ejemplo.com") // Pon aquí tu correo real si lo deseas
                                .url("https://github.com/gsalarzare") // Enlace a tu GitHub
                        )
                );
    }
}