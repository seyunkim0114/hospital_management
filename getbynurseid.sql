use hospital;

select * from patient;

select * from stays_in;

set @clinician_id=11;
select n.clinician_id, p.patient_id, p.firstname, p.lastname, p.dob, p.admitted, p.discharged
from nurse n, responsible r, room, stays_in s, patient p
where n.clinician_id = r.clinician_id and
		r.room_id = room.room_id and
		room.room_id = s.room_id and
        s.patient_id = p.patient_id and 
        n.clinician_id = @clinician_id
order by n.clinician_id;