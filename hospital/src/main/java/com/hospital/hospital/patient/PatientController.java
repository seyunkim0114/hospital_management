package com.hospital.hospital.patient;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping(path="patient/patient_id")
@CrossOrigin
public class PatientController {
    
    private final PatientService patientService;

    @Autowired
    public PatientController(PatientService patientService) {
        this.patientService = patientService;
    }

    @GetMapping("/allpatients")
    public List<Patient> getPatients() {
        return patientService.getPatients();
    }

    // @GetMapping("/patientsft300")
    // public List<Patient> getPatientsGT300() {
    //     return patientService.getPatientsGT300();
    // }

    // @GetMapping("/bynurseid")
    // public List<Patient> findAllPatientsByNurseId(Integer nurseId) {
    //     return patientService.findAllPatientsByNurseId(11);
    // }
    
}
