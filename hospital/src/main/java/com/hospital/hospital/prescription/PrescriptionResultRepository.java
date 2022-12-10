package com.hospital.hospital.prescription;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface PrescriptionResultRepository extends CrudRepository<PrescriptionResult, Integer>{
    
}
