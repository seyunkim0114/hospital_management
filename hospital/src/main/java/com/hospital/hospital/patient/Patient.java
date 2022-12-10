package com.hospital.hospital.patient;

// import java.sql.Date;
import java.util.Date;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;
import javax.print.attribute.standard.DateTimeAtCompleted;

import org.hibernate.query.criteria.internal.expression.function.CurrentDateFunction;

@Entity
// @Table(name="patient")
public class Patient {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Integer patient_id;

    private String firstname;
    private String lastname;
    private Date dob;
    // private Date admitted;
    // private Date discharged;

    // Default constructor
    public Patient() {}

    public Patient(Integer patient_id, String firstname, String lastname, Date dob) {
        this.patient_id = patient_id;
        this.firstname = firstname;
        this.lastname = lastname;
        this.dob = dob;
    }

    // public Patient (String firstname, String lastname, Date dob) {
    //     this.firstname = firstname;
    //     this.lastname = lastname;
    //     this.dob = dob;
    // }

    public Integer getPatient_id() {
        return patient_id;
    }

    public void setPatient_id(Integer patient_id) {
        this.patient_id = patient_id;
    }

    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }

    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }

    public Date getDob() {
        return dob;
    }

    public void setDob(Date dob) {
        this.dob = dob;
    }

    @Override
    public String toString() {
        return "Patient{" +
                "patient_id=" + patient_id + '\'' +
                ", firstname=" + firstname + '\'' +
                ", lastname=" + lastname + '\'' +
                ", dob=" + dob + '\'' +
                "}";
    }


}
