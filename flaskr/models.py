from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from dataclasses import dataclass
from datetime import time, datetime as dt
import datetime
import enum

from .extensions import db

@dataclass
class Prescription(db.Model):
    prescription_id: int
    medicine_name: str
    patient_id: int
    med_interval: int
    start_date: datetime.datetime
    end_date: datetime.datetime
    # is_deleted: bool
    # special_notes: str

    prescription_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    medicine_name = db.Column(db.String(20), nullable=False) 
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.patient_id'))
    med_interval = db.Column(db.Integer)
    start_date = db.Column(db.DATETIME)
    end_date = db.Column(db.DATETIME)
    # is_deleted = db.Column(db.Boolean)
    # special_notes = db.Column(db.String(300))
    patientsRel = db.relationship('Patient', backref='patient')


# @dataclass
# class Prescribed(db.Model):
#     # clinician_id: int
#     prescription_id: int
#     patient_id: int

#     # clinician_id = db.Column(db.Integer, primary_key=True)
#     prescription_id = db.Column(db.Integer, primary_key=True)
#     patient_id = db.Column(db.Integer, db.ForeignKey('Patient.patient_id'), primary_key=True)

#     patientsRel = db.relationship('Patient', back_populates='prescribedRel')

@dataclass
class Patient(db.Model):
    patient_id: int
    firstname: str
    # lastname: str

    patient_id = db.Column(db.Integer, primary_key=True)
    lastname = db.Column(db.String, nullable=False)
    firstname = db.Column(db.String, nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey("room.room_id"))
    # lastname = db.Column(db.String, nullable=False)

    staysinRel = db.relationship('StaysIn', backref="patient")

# Define Room.room_type check constraint with Enum
class RoomTypes(enum.Enum):
    gen = "gen"
    er = "er"
    icu = "icu"
    picu = "picu"
    nicu = "nicu"


@dataclass
class Room(db.Model):
    room_id = db.Column(db.Integer, primary_key=True)
    room_type = db.Column(db.Enum(RoomTypes))

    patients = db.relationship('StaysIn', backref='room')

@dataclass
class StaysIn(db.Model):
    room_id = db.Column(db.Integer, db.ForeignKey('room.room_id'), primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.patient_id'), primary_key=True)
    admitted = db.Column(db.DATETIME, nullable=False, default=dt.now()) 
    discharged = db.Column(db.DATETIME, nullable=True) # default NULL



# Define Nurse.NursePositions check constraint with Enum
class NursePositions(enum.Enum):
    junior = "junior"
    senior = "senior"


# Model many-to-many relationship between nurse and room
responsible = db.Table('responsible', \
    db.Column('clinician_id', db.Integer, db.ForeignKey('nurse.clinician_id')),
    db.Column('room_id', db.Integer, db.ForeignKey(Room.room_id))
)

@dataclass
class Nurse(db.Model):
    clinician_id: int
    firstname: str
    lastname: str
    position: str
    startshift: time
    endshift: time


    clinician_id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    position = db.Column(db.Enum(NursePositions))
    startshift = db.Column(db.Time)
    endshift = db.Column(db.Time)

    rooms = db.relationship('Room', secondary=responsible, backref='nurse')


# class Responsible(db.Model):
#     clinician_id = db.Column(db.Integer, db.ForeignKey(Nurse.clinician_id), \
#         primary_key=True)

#     room_id = db.Column(db.Integer, db.ForeignKey(Room.room_id), \
#         primary_key=True)

#     nurses = db.relationship('Nurse')
#     rooms = db.relatinoship('Room')



