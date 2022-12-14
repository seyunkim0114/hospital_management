import { useSlotProps } from '@mui/base';
import { Button } from '@mui/material';
import { DataGrid } from '@mui/x-data-grid';
import React, { useEffect, useState } from 'react';
import CompletionLog from './CompletionLog';
// import APIService from '../Components/APIService'


function createPrescriptionData(patient_id, lastname, firstname, room_id, prescription_id, 
    medicine_name, recommendation, special_notes, clinician_id, room_type) {
    return { patient_id, lastname, firstname, room_id, prescription_id, 
        medicine_name, recommendation, special_notes, clinician_id, room_type };
}

const columns = [
  { field: 'patient_id', headerName: 'Patient ID', width: 150 },
  { field: 'lastname', headerName: 'Last Name', width: 150 },
  { field: 'firstname', headerName: 'First Name', width: 150 },
  {
    field: 'prescription_id',
    headerName: 'Prescription ID',
    // description: 'This column has a value getter and is not sortable.',
    sortable: false,
    width: 150,
    type: 'number'
    // valueGetter: (params) =>
    //   `${params.row.firstName || ''} ${params.row.lastName || ''}`,
  },
  { field: 'medicine_name', headerName: "Medication", width: 150 },
  { field: 'recommendation', headerName: "Recommendation", width: 200},
  { field: 'special_notes', headerName: "Note", width: 200},
  { field: 'clinician_id', headerName: "Clinician ID", width: 150, type: "number"},
  { field: 'room_id', headerName: 'Room', type: 'number', width: 150 },
  { field: 'room_type', headerName: "Ward", width: 150, 
    valueGetter: (param) => param.row.room_type.substring(param.row.room_type.indexOf('.')+1)  }
];


function handleCheckboxSelect(data) {
    // console.log(JSON.stringify(data))
    // e.preventDefault();
    fetch('http://localhost:5000/addlogs', {
            'method':'POST',
            headers : {
            'Content-Type':'application/json',
            mode : 'cors',
            crossDomain:true
            },
        body : JSON.stringify(data)
    })
}


export default function PatientsToPrescribe() {
    const[patients, setPatients] = useState([]);
    // const[rows, setRows] = useState([])
    const[deletedRows, setDeletedRows] = useState([]);
    const[selectionModel, setSelectionModel] = useState([]);
    
    const rows = [];
    
    useEffect(()=>{
        fetch("http://127.0.0.1:5000/nurses_responsible")
        .then(res=>res.json())
        .then((result)=>{
            setPatients(result)
        })
    }, [])

    // console.log(patients)
    patients.map(patient=>{
        if(patient.clinician_id == 106){
            rows.push(createPrescriptionData(patient.patient_id, patient.lastname, patient.firstname, patient.room_id, 
                patient.prescription_id, patient.medicine_name, patient.recommendation, 
                patient.special_notes, patient.clinician_id, patient.room_type ))
        }
    })
    

    const handleRowSelection = (e) => {
        console.log(e)
        setDeletedRows([...deletedRows, ...rows.filter(
            (r) => r.prescription_id === e.data.prescription_id
        )])
    }

    const deleteSelectedRow = (e) => {
        setPatients(
            rows.filter(
                (r) => deletedRows.filter(
                    (sr) => sr.prescription_id === r.prescription_id).length < 1)
            );
    };
    

  return (
    <div style={{ height: 400, width: '100%' }}>
        Upcoming Prescriptions
        <div style={{ display: "flex", justifyContent: 'flex-end'}}>
            <button 
                style={{ width: "100px", height: "30px",}}
                onClick={deleteSelectedRow} >
                DONE
            </button>
        </div>
            
        <DataGrid
            rows={rows}
            columns={columns}
            pageSize={5}
            rowsPerPageOptions={[5]}
            getRowId={(rows)=>rows.prescription_id}
            allowDelete={true}
            checkboxSelection
            onSelectionModelChange={(ids) => {
                const selectedIDs = new Set(ids);
                const selectedRowData = rows.filter((row) => 
                    selectedIDs.has(row.prescription_id.toString())
                );
                handleCheckboxSelect(selectedRowData);
                // console.log(selectedRowData);                
            }}
            onRowSelected={handleRowSelection}
        />
      

      Your prescribed log
      <CompletionLog/>
    </div>
  );
}