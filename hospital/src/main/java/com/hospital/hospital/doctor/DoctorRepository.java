package com.hospital.hospital.doctor;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface DoctorRepository 
        extends JpaRepository<Doctor, Long> {

        // List<Doctor> findAll();
} 