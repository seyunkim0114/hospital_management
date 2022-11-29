package com.hospital.hospital.patient;

import java.util.List;

// import org.springframework.data.jdbc.repository.query.Query;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

@Repository

public interface PatientRepository 
        extends JpaRepository<Patient, Integer> {
    
    @Query(nativeQuery = true, value = "SELECT * FROM patient")
    List<Patient> findAll();

    @Query(nativeQuery = true, value="SELECT * FROM patient where patient_id > 350")
    List<Patient> findByIdGT300();
 


}
