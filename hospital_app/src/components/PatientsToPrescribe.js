import { DataGrid } from '@mui/x-data-grid';
import React, { useEffect, useState } from 'react';


function createData(patient_id, lastname, firstname, room_id, prescription_id, clinician_id, room_type) {
    return { patient_id, lastname, firstname, room_id, prescription_id, clinician_id, room_type };
}

const columns = [
  { field: 'patient_id', headerName: 'Patient ID', width: 100 },
  { field: 'lastname', headerName: 'Last Name', width: 100 },
  { field: 'firstname', headerName: 'First Name', width: 100 },
  { field: 'room_id', headerName: 'Room', type: 'number', width: 90 },
  {
    field: 'prescription_id',
    headerName: 'Prescription ID',
    // description: 'This column has a value getter and is not sortable.',
    sortable: false,
    width: 90,
    type: 'number'
    // valueGetter: (params) =>
    //   `${params.row.firstName || ''} ${params.row.lastName || ''}`,
  },
  { field: 'clinician_id', headerName: "Clinician ID", width: 90, type: "number"},
  { field: 'room_type', headerName: "Ward", width: 100, 
    valueGetter: (param) => param.row.room_type.substring(param.row.room_type.indexOf('.')+1)  }
];


export default function PatientsToPrescribe() {
    const[patients, setPatients] = useState([]);
    const rows = [];

    useEffect(()=>{
        fetch("http://127.0.0.1:5000/nurses_responsible")
        .then(res=>res.json())
        .then((result)=>{
            setPatients(result)
        })
    }, [])

    console.log(patients)
    patients.map(patient=>{
        if(patient.clinician_id == 101){
            rows.push(createData(patient.patient_id, patient.lastname, patient.firstname, patient.room_id, 
                patient.prescription_id, patient.clinician_id, patient.room_type ))
        }
        // rows.push(patient)
        console.log(rows)
        
    })
    
    

  return (
    <div style={{ height: 400, width: '100%' }}>
      <DataGrid
        rows={rows}
        columns={columns}
        pageSize={5}
        rowsPerPageOptions={[5]}
        getRowId={(rows)=>rows.prescription_id}
        checkboxSelection
      />
    </div>
  );
}