package com.hospital.hospital.prescription;

import java.util.Date;
import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

@Repository
public interface PrescriptionRepository extends JpaRepository<Prescription, Integer> {
    
    @Query(nativeQuery=true, value = "SELECT * FROM prescription")
    List<Prescription> findAll();

    @Query(value = """
            SELECT ADDDATE(p.start_date, INTERVAL p.med_interval HOUR) newdate
            FROM prescription p
            """, nativeQuery=true)
    List<Date> findAddDateToStartDate();

}
