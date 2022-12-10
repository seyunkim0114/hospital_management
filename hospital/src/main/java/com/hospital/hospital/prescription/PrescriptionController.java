package com.hospital.hospital.prescription;

import java.text.DateFormat;
import java.text.SimpleDateFormat;

import java.util.Date;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping(path = "prescription")
public class PrescriptionController {
    
    private final PrescriptionService prescriptionService;

    @Autowired
    public PrescriptionController(PrescriptionService prescriptionService) {
        this.prescriptionService = prescriptionService;
    }
    
    @GetMapping("/getprescription")
    public List<Prescription> getPrescription() {
        return prescriptionService.getPrescription();
    }

    // @GetMapping("/findAddDateToStartDate")
    // public List<Date> getAddDateToStartDate() {
    //     return prescriptionService.getAddDateToStartDate();
    // }

    // @GetMapping("/findAllNextDateTimeToPrescribe")
    // public List<PrescriptionResult> findAllNextDateTimeToPrescribe() {        
    //     return prescriptionService.findAllNextDateTimeToPrescribe();

    // }
}
