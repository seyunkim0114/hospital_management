package com.hospital.hospital.doctor;

public class Doctor {
    private Integer doctor_id;
    private String firstname;
    private String lastname;
    
    public Doctor () {
    }

    public Doctor (Integer doctor_id, String firstname, String lastname) {
        this.doctor_id = doctor_id;
        this.firstname = firstname;
        this.lastname = lastname;
    }

    public Doctor (String firstname, String lastname) {
        this.firstname = firstname;
        this.lastname = lastname;
    }

    public Integer getDoctor_id() {
        return doctor_id;
    }

    public String getFirstname() {
        return firstname;
    }
    
    public String getLastname() {
        return lastname;
    }

    public void setDoctor_id(Integer doctor_id) {
        this.doctor_id = doctor_id;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }

    @Override
    public String toString() {
        return "Doctor{" +
                "doctor_id=" + doctor_id +
                ", firstname" + firstname + '\'' +
                ", lastname" + lastname + '\'' +
                "}";
                
    }
}
