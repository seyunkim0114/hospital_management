package com.hospital.hospital.prescription;

import java.util.Date;

public class PrescriptionResult {
    private Integer prescription_id;
    private Date nextTimetoPrescribe;
    private String medicine_name;
    private String recommendation;
    private String special_notes;
    private Integer clinician_id;

    public PrescriptionResult() {}

    public PrescriptionResult(Integer prescription_id, Date nextTimetoPrescribe, 
        String medicine_name, String recommendation, String special_notes, Integer clinician_id) {
            this.prescription_id = prescription_id;
            this.nextTimetoPrescribe = nextTimetoPrescribe;
            this.medicine_name = medicine_name;
            this.recommendation = recommendation;
            this.special_notes = special_notes;
            this.clinician_id = clinician_id;
        }

    public Integer getPrescription_id() {
        return prescription_id;
    }

    public void setPrescription_id(Integer prescription_id) {
        this.prescription_id = prescription_id;
    }

    public Date getNextTimetoPrescribe() {
        return nextTimetoPrescribe;
    }

    public void setNextTimetoPrescribe(Date nextTimetoPrescribe) {
        this.nextTimetoPrescribe = nextTimetoPrescribe;
    }

    public String getMedicine_name() {
        return medicine_name;
    }

    public void setMedicine_name(String medicine_name) {
        this.medicine_name = medicine_name;
    }

    public String getRecommendation() {
        return recommendation;
    }

    public void setRecommendation(String recommendation) {
        this.recommendation = recommendation;
    }

    public String getSpecial_notes() {
        return special_notes;
    }

    public void setSpecial_notes(String special_notes) {
        this.special_notes = special_notes;
    }

    public Integer getClinician_id() {
        return clinician_id;
    }

    public void setClinician_id(Integer clinician_id) {
        this.clinician_id = clinician_id;
    }

    @Override
    public String toString() {
        return "PrescriptionResult [prescription_id=" + prescription_id + ", nextTimetoPrescribe=" + nextTimetoPrescribe
                + ", medicine_name=" + medicine_name + ", recommendation=" + recommendation + ", special_notes="
                + special_notes + ", clinician_id=" + clinician_id + "]";
    }
    

}
