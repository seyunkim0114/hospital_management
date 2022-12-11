from flask import Flask, request, session, redirect, url_for, render_template, flash, jsonify
from flask import Blueprint
from sqlalchemy import func, text, or_
from datetime import datetime
# from flask_marshamllow import Marshmallow

from .models import Prescription, Patient, Room, responsible, Nurse
from .extensions import db


main = Blueprint("main", __name__)
# use session.query not model.query to make it serializable
session = db.session

# Get prescription of prescription_id id
@main.route("/prescription_<int:id>", methods=["GET"])
def get_prescriptions(id):
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
def getNursesResponsibleForPrescriptionNow():
    now = datetime.now()
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
    
    query = session.query(Prescription.prescription_id, Patient.patient_id, Room.room_id, Nurse.clinician_id) \
        .filter(ontimes.c.prescription_id == Prescription.prescription_id) \
            .filter(Prescription.patient_id == Patient.patient_id) \
                .filter(Patient.room_id == Room.room_id) \
                    .filter(Room.room_id == responsible.c.room_id) \
                        .filter(responsible.c.clinician_id == Nurse.clinician_id) \
                            .filter(or_(now > Nurse.startshift, now < Nurse.endshift)).all()
                                # .filter(Nurse.endshift < now).all()

    query_json = []
    for q in query:
        query_json.append({
            "prescription_id": str(q[0]),
            "patient_id": str(q[1]),
            "room_id": str(q[2]),
            "clinician_id": str(q[3])
        })

    # query_json = []
    # for q in query:
    #     query_json.append({
    #         "patient_id": str(q[0]),
    #         "lastname": str(q[1]),
    #         "firstname": str(q[2]),
    #         "clinician_id": str(q[3]),
    #         "prescription_id": str(q[4]),
    #         "room_id": str(q[5]),
    #         "room_type": str(q[6])
    #     })
    
    return query_json








@main.route("/hi")
def home():
    return "helo"