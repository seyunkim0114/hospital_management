from flask import Flask, request, session, redirect, url_for, render_template, flash, jsonify
from flask import Blueprint
from sqlalchemy import func, text, or_, and_, not_
from datetime import datetime, timedelta

import sys
import logging
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

from .models import Prescription, Patient, Room, responsible, Nurse, StaysIn, Completed, Medication, has
from .extensions import db

scheduler = BackgroundScheduler()
main = Blueprint("main", __name__)

# Get prescription of prescription_id id
@main.route("/prescription_<int:id>", methods=["GET"])
def get_prescriptions(id):
    session = db.session
    query = session.query(Prescription.prescription_id, Prescription.medicine_name) \
        .filter(Prescription.prescription_id == id).all()

    query_json = []
    for q in query:
        query_json.append({
            "prescription_id": str(q[0]),
            "medicine_name": str(q[1])
        })
    
    return query_json
    # return jsonify(prescriptions)

# Get patient id, medicine name for patients who have prescriptions
@main.route("/patients", methods=["GET"])
def getPatientsAndPrescriptions():
    session = db.session
    query = session.query(Patient.patient_id, Prescription.prescription_id, Prescription.medicine_name). \
        filter(Prescription.patient_id == Patient.patient_id).all()
    query_json = []
    # print(len(query))
    for q in query:
        query_json.append({
            "patient_id": str(q[0]),
            "prescription_id": str(q[1]),
            "medicine_name": str(q[2]),
        })
    return query_json

# Get information of nurse with clinician_id id
@main.route("/nurse_<int:id>", methods=["GET"])
def getNurseById(id):
    session = db.session
    query = session.query(Nurse.clinician_id, Nurse.lastname, Nurse.firstname, Nurse.position) \
        .filter(Nurse.clinician_id == id).all()

    query_json = []
    for q in query:
        query_json.append({
            "clinician_id": str(q[0]),
            "firstname": str(q[1]),
            "lastname": str(q[2]),
            "position": str(q[3])
            # "startshift": str(q[4]),
            # "endshift": str(q[5])
        })
    # return jsonify(query)
    return query_json

@main.route("/nurses_responsible", methods=["GET"])
# @scheduler.scheduled_job(trigger = 'cron', minute = '*', args=[id])
def getNursesResponsibleForPrescriptionNow():
    session = db.session
    now = datetime.now()
    # time_now = now.strftime("%H:%M:%S")
    # time_now = now.time()
    time_now = datetime(2022,12,1,9,21,0,0)
    """
    diff_date = now - state_date
    diff_hour = diff_date.total_seconds / 3600

    if diff_hour % med_interval < 1

 
    """
    ontimes =  session.query(Prescription.prescription_id, Prescription.start_date) \
        .filter(Prescription.med_interval - func.time_to_sec(func.timediff(now, Prescription.start_date))/3600 % Prescription.med_interval < 10).subquery("ontimes")
    # query_json = []
    # for q in query:
    #     query_json.append({
    #         'prescription_id': str(q[0]),
    #         'hour_diff': str(q[1])
    #     })

    # query = session.query(Patient.patient_id, Patient.lastname, Patient.firstname, Nurse.clinician_id, \
    #     Prescription.prescription_id, Room.room_id,  Room.room_type) \
    #         .filter(ontimes.c.prescription_id == Prescription.prescription_id) \
    #         .filter(Prescription.patient_id == Patient.patient_id) \
    #             .filter(Patient.room_id == Room.room_id) \
    #                 .filter(Room.room_id == responsible.c.room_id) \
    #                     .filter(responsible.c.clinician_id == Nurse.clinician_id) \
    #                         .filter(Nurse.startshift > now) \
    #                             .filter(Nurse.endshift < now).all()
    
    query = session.query(Prescription.prescription_id, Patient.patient_id, Room.room_id, Nurse.clinician_id, \
        Patient.lastname, Patient.firstname, Room.room_type) \
        .filter(ontimes.c.prescription_id == Prescription.prescription_id) \
            .filter(Prescription.patient_id == Patient.patient_id) \
                .filter(and_(Patient.patient_id == StaysIn.patient_id, StaysIn.discharged == None)) \
                    .filter(StaysIn.room_id == Room.room_id) \
                        .filter(Room.room_id == responsible.c.room_id) \
                            .filter(responsible.c.clinician_id == Nurse.clinician_id) \
                                    .filter( or_(and_(time_now > Nurse.startshift, time_now < Nurse.endshift), \
                                        and_(not_(and_(time_now > Nurse.endshift, time_now < Nurse.startshift)), \
                                            Nurse.startshift > Nurse.endshift) )).all()

    query_json = []
    for q in query:
        query_json.append({
            "prescription_id": str(q[0]),
            "lastname": str(q[4]),
            "firstname": str(q[5]),
            "patient_id": str(q[1]),
            "room_id": str(q[2]),
            "clinician_id": str(q[3]),
            "room_type": str(q[6])
        })


    return query_json

@main.route("/completions", methods=["GET", "POST"])
def get_completions():
    """
    Returns the prescribed log of the last 30 days from now  
    Return JSON
        completion_id
        patient_id
        lastname
        firstname
        prescription_id
        completed_at
    """
    session = db.session

    now = datetime.now()
    # time_now = now.strftime("%H:%M:%S")

    # query = session.query(Completed.completion_id).all()
    query = session.query(Completed.completion_id, Completed.patient_id, Patient.lastname, Patient.firstname, Completed.prescription_id, \
        Completed.completed_at).\
            filter(Completed.patient_id == Patient.patient_id) \
                .filter(Completed.completed_at > now - timedelta(days=30))
    
    query_json = []
    for q in query:
        query_json.append({
            "completion_id": str(q[0]),
            "patient_id": str(q[1]),
            "lastname": str(q[2]),
            "firstname": str(q[3]),
            "prescription_id": str(q[4]),
            "completed_at": str(q[5])
        })

    return query_json


@main.route("/addlogs", methods=["POST"])
def add_logs():
    """
    Retrieves:
        patient_id
        clinician_id
        prescription_id
        completed_at
    """
    session = db.session

    patient_id = request.json[0]['patient_id']
    # completion_id = request.json[0]["completion_id"]
    clinician_id = request.json[0]['clinician_id']
    prescription_id = request.json[0]['prescription_id']
    # completed_at = {"completed_at": datetime.now()}
    completed_at = datetime.now()

    completion = Completed(
        # completion_id = completion_id
        patient_id = patient_id,
        clinician_id = clinician_id,
        prescription_id = prescription_id,
        completed_at = completed_at
    )
    
    session.add(completion)
    session.commit()

    return {
        "patient_id": patient_id,
        "clinician_id": clinician_id,
        "prescription_id": prescription_id,
        "completed_at": completed_at
    }


@main.route("/fullprescriptions", methods=["GET"])
def get_full_prescriptions():
    session = db.session

    query = session.query(Prescription.prescription_id, Prescription.patient_id, Medication.medicine_name, \
        Medication.recommendation, Prescription.special_notes
        ).filter(Prescription.prescription_id == has.c.prescription_id) \
            .filter(has.c.medicine_id == Medication.medicine_id).all()

    query_json = []
    for q in query:
        query_json.append({
            "prescription_id": str(q[0]),
            "patient_id": str(q[1]),
            "medicine_name": str(q[2]),
            "recomemndation": str(q[3]),
            "special_notes": str(q[4])
        })    
    
    return query_json

@main.route("/hi")
def home():
    return "helo"


