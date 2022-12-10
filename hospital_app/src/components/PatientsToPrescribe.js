import { DataGrid } from '@mui/x-data-grid';
import React, { useEffect, useState } from 'react';


function createData(patient_id, lastname, firstname, room_id, prescription_id, clinician_id, room_type) {
    return { patient_id, lastname, firstname, room_id, prescription_id, clinician_id, room_type };
}

const columns = [
  { field: 'patient_id', headerName: 'Patient ID', width: 100 },
  { field: 'lastName', headerName: 'Last name', width: 130 },
  { field: 'firstName', headerName: 'First name', width: 130 },
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
  { field: 'room_type', headerName: "Ward", width: 100 }
];

// const rows = [
//   { id: 1, lastName: 'Snow', firstName: 'Jon', age: 35 },
//   { id: 2, lastName: 'Lannister', firstName: 'Cersei', age: 42 },
//   { id: 3, lastName: 'Lannister', firstName: 'Jaime', age: 45 },
//   { id: 4, lastName: 'Stark', firstName: 'Arya', age: 16 },
//   { id: 5, lastName: 'Targaryen', firstName: 'Daenerys', age: null },
//   { id: 6, lastName: 'Melisandre', firstName: null, age: 150 },
//   { id: 7, lastName: 'Clifford', firstName: 'Ferrara', age: 44 },
//   { id: 8, lastName: 'Frances', firstName: 'Rossini', age: 36 },
//   { id: 9, lastName: 'Roxie', firstName: 'Harvey', age: 65 },
// ];

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
    patients.map(patient=>(
        // rows.push(patient)
        rows.push(createData(patient.patient_id, patient.lastname, patient.firstname, patient.room_id, 
            patient.prescription_id, patient.clinician_id, patient.room_type ))
    ))
    
    

  return (
    <div style={{ height: 400, width: '100%' }}>
      <DataGrid
        rows={rows}
        columns={columns}
        pageSize={5}
        rowsPerPageOptions={[5]}
        getRowId={(rows)=>rows.clinician_id}
        checkboxSelection
      />
    </div>
  );
}