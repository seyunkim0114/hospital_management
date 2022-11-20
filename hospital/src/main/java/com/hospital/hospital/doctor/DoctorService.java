package com.hospital.hospital.doctor;

import java.util.List;

import org.springframework.stereotype.Component;
import org.springframework.stereotype.Service;

@Service
public class DoctorService {
    
	public List<Doctor> getDoctors() {
		return List.of(
			new Doctor(
				1, "doctor", "ppp"
			)
		);
	}
}

