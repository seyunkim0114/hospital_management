use hospital;

select * from prescription;

select * from prescribed;

-- return patient_id, medicine name, recommendation, special_notes, nurse_id, other_nurse_id 
set @nexttime=0;
set @currenttime = cast("2022-11-15 00:00:00" as datetime);


-- return 
-- prescription information, next time to give medicine 
-- if the time to give medicine is within 12 hours
select p.prescription_id, adddate(p.start_date, interval p.med_interval hour) "Time to Prescription", p.medicine_name, r.recommendation, p.special_notes, pd.clinician_id "Prescriber Id"
from prescription p, med_rec r, prescribed pd
where adddate(p.start_date, interval p.med_interval hour) < adddate(@currenttime, interval 12 hour)
		and adddate(p.start_date, interval p.med_interval hour) > @currenttime
        and r.medicine_name = p.medicine_name
        and pd.prescription_id = p.prescription_id
order by "Time to Prescribe";