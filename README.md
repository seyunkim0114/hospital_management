# hospital_management

**Project Idea**
The project is about developing a 3rd party web application that notifies you of the upcoming medications to provide for the patients. The main users of the application are the clinicians of hospitals who prescribe and provide medications. This application also tracks the record of medications provided recently by each clinician.

**How to run**
Navigate to /flaskr
Install the necessary packages pip -r install requirement.txt
Run flask run 
If it gives you error, run export FLASK_APP=__init__.py
Navigate to /hospital_app
Run npm start


**Functionalities**
Display upcoming medications the clinicians are responsible to provide for their patients
Once the medication has been provided, the users can mark it as completed and add to the record
Only authorized medical personnels (in the scope of this project, they are doctors and senior nurses) can prescribe medicine
Clinicians can be promoted to different positions

**Changes from the initial design**
To keep a record of every patient admitted, the admitted and discharged attributes of type datetime are added to the stays in entity, replacing the boolean discharged in the patient entity
Instead of having 3 separate tables for clinician (supertable) and nurses (subtable) and doctors (subtable), they are represented as one supertable. This change is made because in this project nurses and doctors share similar attributes. However, it is recommended to have 3 tables if the project is to be extended to further reflect the real hospital environment. 
SCHEDULE TABLE FOR REFLECT FLEXIBLE SHIFTS FOR CLINICIANS

**Data population**
Medication data referenced from https://www.who.int/groups/expert-committee-on-selection-and-use-of-essential-medicines/essential-medicines-lists
Other data in the database are generated randomly.
The current database contains a small subset of the data available. To use all data, run populate_database2.ipynb

<!-- **Bugs**
Hnmm

**Breakdown of work**
Seyun Kim
Database schema design
Implement schema modeling and queries in backend using Flask and frontend using React.js
Database population
Documentation
Jaewon Cho -->



**Conclusion**
The requirement analysis and logical design are crucial
Learned how a website works


