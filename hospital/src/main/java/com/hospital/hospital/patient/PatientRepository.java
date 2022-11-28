package com.hospital.hospital.patient;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface PatientRepository 
        extends JpaRepository<Patient, Integer> {
    
    List<Patient> findAll();
    
}
