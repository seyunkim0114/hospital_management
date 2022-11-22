package com.hospital.hospital.doctor;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class DoctorService {
    
    private final DoctorRepository doctorRepository;
    
    @Autowired
    public DoctorService(DoctorRepository doctorRepository) {
        this.doctorRepository = doctorRepository;
    }

    public List<Doctor> getDoctors() {
        return doctorRepository.findAll();
        // return List.of(
        //     new Doctor(1L, "mariam", "hello")
        // );
    }
}

