from flask import Flask, request, session, redirect, url_for, render_template, flash, jsonify
from flask import Blueprint
from sqlalchemy import func, text, or_, and_, not_
from datetime import datetime, timedelta

import uuid
import hashlib
import sys
import logging

from .models import Prescription, Patient, Room, responsible, StaysIn, Completed, Medication, Clinician, Shift, User_Auth
from .extensions import db, scheduler


main = Blueprint("main", __name__)

# Get prescription of prescription_id id
@main.route("/prescription_<int:id>", methods=["GET"])
def getPrescriptionByPrescriptionId(id):
    session = db.session
    # query = session.query(Prescription.prescription_id, Prescription.medicine_name) \
    #     .filter(Prescription.prescription_id == id).all()
    query = session.query(Prescription).filter(Prescription.prescription_id == id).all()
    # query_json = []
    # for q in query:
    #     query_json.append({
    #         "prescription_id": str(q[0]),
    #         "medicine_name": str(q[1])
    #     })
    
    # return query_json
    return jsonify(query)

# Get patient id, medicine name for patients who have prescriptions
@main.route("/patients", methods=["GET"])
def getPatientsAndPrescriptions():
    session = db.session
    query = session.query(Patient.patient_id, Prescription.prescription_id, Medication.medicine_name). \
        filter(Prescription.patient_id == Patient.patient_id) \
            .filter(Prescription.medicine_id == Medication.medicine_id).all()

    query_json = []

    for q in query:
        query_json.append({
            "patient_id": str(q[0]),
            "prescription_id": str(q[1]),
            "medicine_name": str(q[2]),
        })

    return query_json

# Get information of nurse with clinician_id id
@main.route("/clinician_<int:id>", methods=["GET"])
def getClinicianById(id):
    session = db.session

    query = session.query(Clinician.clinician_id, Clinician.lastname, Clinician.firstname, Clinician.position) \
            .filter(Clinician.clinician_id == id).all()

    query_json = []
    for q in query:
        query_json.append({
            "clinician_id": str(q[0]),
            "firstname": str(q[1]),
            "lastname": str(q[2]),
            "position": str(q[3]),
        })
 
    return query_json

@main.route('/nurses_responsible', methods=['GET'])
# @main.route("/nurses_responsible", methods=["GET"])
def getNursesResponsibleForPrescriptionNow():
    session = db.session
    # time_now = datetime.now()
    # time_now = now.strftime("%H:%M:%S")
    # time_now = now.time()
    time_now = datetime(2023,1,8,19,16,0,0)

    ontimes =  session.query(Prescription.prescription_id, Prescription.start_date) \
        .filter(Prescription.med_interval - func.time_to_sec(func.timediff(time_now, Prescription.start_date))/3600 % Prescription.med_interval < 10).subquery("ontimes")
    
    query = session.query(Prescription.prescription_id, Patient.patient_id, Room.room_id, Clinician.clinician_id, \
        Patient.lastname, Patient.firstname, Room.room_type, Medication.medicine_name, Medication.recommendation, \
            Prescription.special_notes) \
                .filter(ontimes.c.prescription_id == Prescription.prescription_id) \
                    .filter(Prescription.medicine_id == Medication.medicine_id) \
                        .filter(Prescription.patient_id == Patient.patient_id) \
                            .filter(and_(Patient.patient_id == StaysIn.patient_id, StaysIn.discharged == None)) \
                                .filter(StaysIn.room_id == Room.room_id) \
                                    .filter(Room.room_id == responsible.c.room_id) \
                                        .filter(responsible.c.clinician_id == Clinician.clinician_id) \
                                            .filter(Shift.clinician_id == Clinician.clinician_id) \
                                                .filter( or_(and_(time_now > Shift.startshift, time_now < Shift.endshift), \
                                                    and_(not_(and_(time_now > Shift.endshift, time_now < Shift.startshift)), \
                                                        Shift.startshift > Shift.endshift) )).all()

    # query = session.query(Prescription.prescription_id, Medication.medicine_id, Patient.patient_id, Room.room_id, Shift.clinician_id) \
    #             .filter(ontimes.c.prescription_id == Prescription.prescription_id) \
    #                 .filter(Prescription.medicine_id == Medication.medicine_id) \
    #                     .filter(Prescription.patient_id == Patient.patient_id) \
    #                         .filter(and_(Patient.patient_id == StaysIn.patient_id, StaysIn.discharged == None)) \
    #                             .filter(StaysIn.room_id == Room.room_id) \
    #                                 .filter(Room.room_id == responsible.c.room_id) \
    #                                     .filter(responsible.c.clinician_id == Clinician.clinician_id) \
    #                                         .filter(Shift.clinician_id == Clinician.clinician_id) \
    #                                             .filter( or_(and_(time_now > Shift.startshift, time_now < Shift.endshift), \
    #                                                 and_(not_(and_(time_now > Shift.endshift, time_now < Shift.startshift)), \
    #                                                     Shift.startshift > Shift.endshift) )).all()

    query_json = []
    for q in query:
        query_json.append({
            "prescription_id": str(q[0]),
            "lastname": str(q[4]),
            "firstname": str(q[5]),
            "patient_id": str(q[1]),
            "room_id": str(q[2]),
            "clinician_id": str(q[3]),
            "room_type": str(q[6]),
            "medicine_name": str(q[7]),
            "recommendation": str(q[8]),
            "special_notes": str(q[9])
        })

    return query_json
    

@main.route("/completions", methods=["GET", "POST"])
def getCompletedAll():
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
def insertCompleted():
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
    # firstname = request.json["firstname"]
    # lastname = request.json["lastname"]
    completed_at = datetime.now()

    completion = Completed(
        # completion_id = completion_id
        patient_id = patient_id,
        clinician_id = clinician_id,
        prescription_id = prescription_id,
        completed_at = completed_at
        # lastname = lastname,
        # firstname = firstname
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
def getPresciptionsAll():
    session = db.session

    query = session.query(Prescription.prescription_id, Prescription.patient_id, Medication.medicine_name, \
        Medication.recommendation, Prescription.special_notes
        ).filter(Prescription.medicine_id == Medication.medicine_id).all()

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

@main.route("/newclinicians", methods=["POST"])
def getNewClinician():
    """
    Retrieves
        lastname
        firstname
        position

    """
    session = db.session

    lastname = request.json["lastname"]
    firstname = request.json["firstname"]
    clinician_id = request.json["clinician_id"]
    # print(clinician_id)
    clinician_type = request.json["position"]

    clinician = Clinician(
        clinician_id = int(clinician_id),
        lastname = lastname,
        firstname = firstname,
        startshift = datetime.now().time(),
        endshift = datetime.now().time(),
        clinician_type = clinician_type
    )

    session.add(clinician)
    session.commit()

    return {
        # "clinician_id": clinician_id,
        "lastname": lastname,
        "firstname": firstname,
        "clinician_type": clinician_type
    }

@main.route("/clinician_ids", methods=["GET"])
def getClinicianIdsAll():
    session = db.session

    query = session.query(Clinician.clinician_id).all()
    
    query_json = []
    for q in query:
        query_json.append({
            "clinician_id": str(q[0])
        })
    
    return query_json

@main.route("/hi")
def home():
    return "helo"


@main.route("/authenticate", methods=['GET'])
def authenticate():
    clinicianId = request.json['clinicianId']
    password = request.json['password']

    session = db.session
    query = session.query(User_Auth.password, User_Auth.salt).\
        filter(User_Auth.clinician_id == clinicianId)

    query_json = []
    for q in query:
        query_json.append({
            "username": str(q[0]),
            "password": str(q[1]),
            "salt": str(q[2])
        })
    
    return query_json['password'][0] == hashlib.sha256(query_json['salt'][0].encode() + password.encode()).hexdigest(), clinicianId
    

@main.route("/register", methods=["POST"], strict_slashes=False)
def register():
    clinicianId = request.json['clinicianId']
    p = request.json['password']
    salt = uuid.uuid4().hex
    password = hashlib.sha256(salt.encode() + p.encode()).hexdigest()

    auth = User_Auth(
        clinicianId = clinicianId,
        # username = username,
        password = password,
        salt = salt
        )

    session.add(auth)
    session.commit()

    return {
        "clinicianId": clinicianId,
        "password": password,
        "salt": salt
    }

@scheduler.task('interval', id="job_sync", hours=1)
def upcomingTask():
    """
    Check every hour for new upcoming prescriptions
    """
    print("Scheduler ")
    with scheduler.app.app_context():
        # db = get_schedule_db(scheduler.app.config["DATABASE"])
        # getUpcomingPrescriptions()
        getNursesResponsibleForPrescriptionNow()