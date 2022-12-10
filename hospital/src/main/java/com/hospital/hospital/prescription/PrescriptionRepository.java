package com.hospital.hospital.prescription;

import java.util.Date;
import java.util.List;
import java.util.Map;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface PrescriptionRepository extends CrudRepository<Prescription, Integer>{

}
// public interface PrescriptionRepository extends JpaRepository<Prescription, Integer> {
    
//     @Query(nativeQuery=true, value = "SELECT * FROM prescription")
//     List<Prescription> findAll();

//     @Query(value = """
//             SELECT ADDDATE(p.start_date, INTERVAL p.med_interval HOUR) newdate
//             FROM prescription p
//             """, nativeQuery=true)
//     List<Date> findAddDateToStartDate();

//     @Query(
//         value = """
//             select p.prescription_id, adddate(p.start_date, interval p.med_interval hour) \"Time to Prescription\", 
//             p.medicine_name, r.recommendation, p.special_notes, pd.clinician_id \"Prescriber Id\"
//             from prescription p, med_rec r, prescribed pd
//             where adddate(p.start_date, interval p.med_interval hour) < adddate(cast(\"2022-11-15 00:00:00\" as datetime), interval 12 hour)
//                     and adddate(p.start_date, interval p.med_interval hour) > cast(\"2022-11-15 00:00:00\" as datetime) 
//                     and r.medicine_name = p.medicine_name
//                     and pd.prescription_id = p.prescription_id
//             order by \"Time to Prescribe\";
//                 """,
//         nativeQuery = true
//     )
//     List<PrescriptionResult> findAllNextDateTimeToPrescribe();
// }
