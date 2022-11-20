package com.hospital.hospital;

import java.util.List;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import com.hospital.hospital.doctor.Doctor;


@SpringBootApplication
@RestController
public class HospitalApplication {

	public static void main(String[] args) {
		SpringApplication.run(HospitalApplication.class, args);
	}

	@GetMapping
	public List<Doctor> hello() {
		return List.of(
			new Doctor(
				1, "doctor", "ppp"
			)
		);
	}
}
