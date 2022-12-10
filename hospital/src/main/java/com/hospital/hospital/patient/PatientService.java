package com.hospital.hospital.patient;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.propertyeditors.PathEditor;
import org.springframework.stereotype.Service;

@Service
public class PatientService {
    
    private final PatientRepository patientRepository;

    @Autowired
    public PatientService(PatientRepository patientRepository) {
        this.patientRepository = patientRepository;
    }

    public List<Patient> getPatients() {
        List<Patient> patients = new ArrayList<Patient>();
        patientRepository.findAll().forEach(patient -> patients.add(patient));
        return patients;
    }

    // public List<Patient> getPatientsGT300() {
    //     return patientRepository.findByIdGT300();
    // }

    // public List<Patient> findAllPatientsByNurseId(Integer nurseId) {
    //     return patientRepository.findAllPatientsByNurseId(nurseId);
    // }
    
}


