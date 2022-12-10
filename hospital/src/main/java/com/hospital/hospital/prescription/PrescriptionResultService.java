package com.hospital.hospital.prescription;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class PrescriptionResultService {
    public final PrescriptionResultRepository prescriptionResultRepository;

    @Autowired
    public PrescriptionResultService(PrescriptionRepository prescriptionRepository) {
        this.prescriptionResultRepository = prescriptionResultRepository;
    }

    // public List<PrescriptionResult> getPrescriptionResults() {
    //     // reuturn

    // }
}
