from sqlalchemy.schema import CreateSchema
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, ForeignKey, Date, Integer, String, Column, MetaData, Table, Boolean
from sqlalchemy import CheckConstraint, insert, Enum
from sqlalchemy.orm import sessionmaker, relationship


import enum
# from sqlalchemy import Column


engine = create_engine(
    "mysql+pymysql://root:google9090@127.0.0.1/hospital_management",
    echo=True
)

# engine.execute(CreateSchema('hospital_management'))

conn = engine.connect()
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

meta = MetaData()

doctors = Table(
    'doctors', meta,
    Column('did', Integer, primary_key=True),
    Column('lastname', String(30)),
    Column('firstname', String(30))
)

# hospital = Table(
#     'hospital', meta,
#     Column('room_id', Integer, primary_key=True),
#     Column('type', String)
# )

# roomTypes = ['gen', 'icu', 'picu', 'pr','pt', 'er', 'trauma']
# hospital = Table(
#     'hospital', meta,
#     Column('room_id', Integer, primary_key=True),
#     Column('room_type', String(10), CheckConstraint("room_type in room_types"))
# )

meta.create_all(engine)

class RoomTypesEnum(enum.Enum):
    gen = 1
    icu = 2
    picu = 3
    pr = 4
    pt = 5
    er = 6
    trauma = 7

class Hospital(Base):
    """
    gen: general 
    icu: intensive care unit
    picu: pediatrics icu
    bm: behavioral and mental
    pr: physical rehabilitation
    pt: physical therapy
    er: emergency
    """
    # roomTypes = ['gen', 'icu', 'picu', 'pr','pt', 'er', 'trauma']

    __tablename__ = 'hospital'

    room_id = Column(Integer, primary_key=True)
    type = Column(Enum(RoomTypesEnum), nullable=False)

    def __repr__(self):
        return f'<hospital(room_id={self.room_id}, type={self.room_type}'


"""
Define Patient Table
"""
class Patient(Base):
    __tablename__ = "patient"

    patient_id = Column(Integer, primary_key=True)
    room_id = Column(Integer, ForeignKey("hospital.room_id"))
    dob = Column(Date)
    # doctor_id = Column(Integer, ForeignKey("doctor"))
    # address
    guardian_first_name = Column(String)
    guardian_last_name = Column(String)
    guardian_contact = Column(Integer)
    patient_contact = Column(Integer)
    symptoms = Column(String, nullable=False)
    diagnosis = Column(String)
    # department = Column(String, foreign_key=True)
    discharged = Column(Boolean, nullable=False)
    
    Hospital = relationship(patient_id, )

    def __repr__(self):
        return ""

     

"""
Define Schedule Table
    This table will hold general information of the patient's medication tracking
"""
class RepeatTypes(enum.Enum):
    once = 1
    daily = 2
    weekly = 3
    monthly = 4
    yearly = 5


class Schedule(Base):
    __tablename__ = "schedule"

    patient_id = Column(Integer, primary_key=True, foreign_key=True)
    med_id = Column(Integer, primary_key=True)
    schedule_id = Column(Integer, primary_key=True)
    scheduled_by = Column(Integer, foreign_key=True)
    on_sunday = Column(Boolean)
    on_monday = Column(Boolean)
    on_tuesday = Column(Boolean)
    on_wednesday = Column(Boolean)
    on_thursday = Column(Boolean)
    on_friday = Column(Boolean)
    on_saturday = Column(Boolean)
    repeat_type = Column(Enum(RepeatTypes), nullable=False)
    is_deleted = Column(Boolean)

    # patient = relationship("Patient", back_populates="shecule")
    
    def __repr__(self):
        return ""

# class Doctors(Base):
#     __tablename__ = 'doctors'

#     did = Column('did', Integer, primary_key=True)
#     firstname = Column('firstname', String)
#     lastname = Column('lastname', String)

#     def __repr__(self):
#         return f'<Doctor(did={self.did}, firstname={self.firstname}, lastname={self.lastname}'
Base.metadata.create_all(bind=engine)



conn.close()