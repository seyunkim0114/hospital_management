package com.hospital.hospital.patient;

import java.util.List;

import org.hibernate.query.NativeQuery;
// import org.springframework.data.jdbc.repository.query.Query;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface PatientRepository extends CrudRepository<Patient, Integer> {

}

// public interface PatientRepository 
//         extends JpaRepository<Patient, Integer> {
    
//     @Query(nativeQuery = true, value = "SELECT * FROM patient")
//     List<Patient> findAll();

//     @Query(nativeQuery = true, value="SELECT * FROM patient where patient_id > 350")
//     List<Patient> findByIdGT300();
 
//     @Query(
//         value = """
//             select p.patient_id, p.firstname, p.lastname, p.dob, p.admitted, p.discharged
//             from nurse n, responsible r, room, stays_in s, patient p
//             where n.clinician_id = r.clinician_id and
//                 r.room_id = room.room_id and
//                 room.room_id = s.room_id and
//                 s.patient_id = p.patient_id and 
//                 n.clinician_id = ?#{[0]}
//             order by n.clinician_id
//         """,
//         nativeQuery = true
//     )
//     List<Patient> findAllPatientsByNurseId(Integer nurseId);

// }
