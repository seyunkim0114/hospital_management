package com.hospital.hospital.prescription;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

import javax.websocket.server.ServerEndpoint;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Service
public class PrescriptionService {
    
    public final PrescriptionRepository prescriptionRepository;

    @Autowired
    public PrescriptionService(PrescriptionRepository prescriptionRepository) {
        this.prescriptionRepository = prescriptionRepository;
    }

    public List<Prescription> getPrescription() {
        List<Prescription> prescriptions = new ArrayList<Prescription>();
        prescriptionRepository.findAll().forEach(prescription -> prescriptions.add(prescription));
        return prescriptions;
    }

    // public List<Date> getAddDateToStartDate() {
    //     return prescriptionRepository.findAddDateToStartDate();
    // }

    // public List<PrescriptionResult> findAllNextDateTimeToPrescribe() {
    //     return prescriptionRepository.findAllNextDateTimeToPrescribe();
    // }
}
