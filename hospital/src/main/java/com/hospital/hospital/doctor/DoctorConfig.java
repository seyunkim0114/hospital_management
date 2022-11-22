package com.hospital.hospital.doctor;

import java.util.List;

import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;


@Configuration
public class DoctorConfig {
    @Bean
    CommandLineRunner commandLineRunner(DoctorRepository repository) {
        return args -> {
            Doctor sam = new Doctor(
                1L, 
                "Hello",
                "hello"
            );

            repository.saveAll(List.of(sam));

        };
        
    }
}

