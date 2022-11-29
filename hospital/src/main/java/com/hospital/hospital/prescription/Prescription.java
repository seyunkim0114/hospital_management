package com.hospital.hospital.prescription;

import java.util.Date;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name="prescription")
public class Prescription {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Integer prescription_id;

    private String medicine_name;
    private Integer med_interval;
    private Date start_date;
    private Date end_date;
    private Boolean is_deleted;
    private String special_notes;

    public Prescription() {}

    public Prescription(Integer prescription_id, String medicine_name, Integer med_interval, Date start_date,
                            Date end_date, Boolean is_deleted, String special_notes) {
                                this.prescription_id = prescription_id;
                                this.medicine_name = medicine_name;
                                this.med_interval = med_interval;
                                this.start_date = start_date;
                                this.end_date = end_date;
                                this.is_deleted = is_deleted;
                                this.special_notes = special_notes;
                            }

    public Prescription(String medicine_name, Integer med_interval, String special_notes) {
        // this.prescription_id = prescription_id;
        this.medicine_name = medicine_name;
        this.med_interval = med_interval;
        // this.end_date = end_date;
        // this.start_date = curtime();
        this.special_notes = special_notes;
    }

    public Integer getPrescription_id() {
        return prescription_id;
    }

    public void setPrescription_id(Integer prescription_id) {
        this.prescription_id = prescription_id;
    }

    public String getMedicine_name() {
        return medicine_name;
    }

    public void setMedicine_name(String medicine_name) {
        this.medicine_name = medicine_name;
    }

    public Integer getMed_interval() {
        return med_interval;
    }

    public void setMed_interval(Integer med_interval) {
        this.med_interval = med_interval;
    }

    public Date getStart_date() {
        return start_date;
    }

    public void setStart_date(Date start_date) {
        this.start_date = start_date;
    }

    public Date getEnd_date() {
        return end_date;
    }

    public void setEnd_date(Date end_date) {
        this.end_date = end_date;
    }

    public Boolean getIs_deleted() {
        return is_deleted;
    }

    public void setIs_deleted(Boolean is_deleted) {
        this.is_deleted = is_deleted;
    }

    public String getSpecial_notes() {
        return special_notes;
    }

    public void setSpecial_notes(String special_notes) {
        this.special_notes = special_notes;
    }

    @Override
    public String toString() {
        return "Prescription [prescription_id=" + prescription_id + ", medicine_name=" + medicine_name
                + ", med_interval=" + med_interval + ", start_date=" + start_date + ", end_date=" + end_date
                + ", is_deleted=" + is_deleted + ", special_notes=" + special_notes + "]";
    }

}