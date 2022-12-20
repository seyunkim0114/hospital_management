# hospital_management

**Project Idea**  
The project is about developing a 3rd party web application that notifies you of the upcoming medications to provide for the patients. The main users of the application are the clinicians of hospitals who prescribe and provide medications. This application also tracks the record of medications provided recently by each clinician.

**Functionalities**  
* Clinicians can log in with their username, password, and clinician id and access personalized pages for various activities.  
* Display upcoming medications the clinicians are responsible to provide for their patients
* Once the medication has been provided, the users can mark it as completed and the information is automatically added to the database and shown on the page. 
* Only authorized medical personnels (in this project, they are doctors and APRN nurses) can prescribe medicine
* Clinicians can be promoted to different positions

**How to run**
Git clone the repository
'''
git clone https://github.com/seyunkim0114/hospital_management.git
'''

Navigate to /flaskr, install requirements, and run backend
'''
cd flaskr
pip install -r requirement.txt
flask run 
//run export FLASK_APP=__init__.py if see "cannot find flask app" error message
'''

Navigate to /hospital_app to run frontend
'''
cd ../hospital_app
npm start
''' 

**Data population**
* Medication data referenced from [https://www.who.int/groups/expert-committee-on-selection-and-use-of-essential-medicines/essential-medicines-lists]
* Other data in the database are generated randomly.
* The current database contains a small subset of the data available. To use all data, run populate_database2.ipynb

