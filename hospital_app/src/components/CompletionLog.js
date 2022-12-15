// Code reference: https://codesandbox.io/s/signupregistration-form-reactmaterialui-fr71m?file=/src/index.js

// import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import React, { useEffect, useState } from 'react';


function createData(patient_id, firstname, lastname, prescription_id, completed_at) {
    return { patient_id, firstname, lastname, prescription_id, completed_at };
  }

function createCompletionData(completion_id, patient_id, lastname, firstname, prescription_id, completed_at) {
    return { completion_id, patient_id, lastname, firstname, prescription_id, completed_at };
}

    
export default function CompletionLog() {
    const[completions, setCompletions] = useState([]);
    const comps = [];

    useEffect(()=>{
        fetch("http://127.0.0.1:5000/completions")
        .then(res=>res.json())
        .then((result)=>{
            setCompletions(result)
            // console.log('hello', result)
        })
    })

    completions.map(completion=>{
        comps.push(createCompletionData(completion.completion_id, completion.patient_id, completion.lastname, 
            completion.firstname, completion.prescription_id, completion.completed_at))
    })

  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>Completion ID</TableCell>
            <TableCell>Patient ID</TableCell>
            <TableCell align="right">Last Name</TableCell>
            <TableCell align="right">First Name&nbsp;(g)</TableCell>
            <TableCell align="right">Prescription ID</TableCell>
            <TableCell align="right">Time of Completion (GMT)</TableCell>
            {/* <TableCell align="right">Protein&nbsp;(g)</TableCell> */}
          </TableRow>
        </TableHead>
        <TableBody>
          {comps.map((completed) => (
            <TableRow
              key={completed.completion_id}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              {/* <TableCell component="th" scope="row">
                {completed.name}
              </TableCell> */}
              <TableCell align="right">{completed.completion_id}</TableCell>
              <TableCell align="right">{completed.patient_id}</TableCell>
              <TableCell align="right">{completed.lastname}</TableCell>
              <TableCell align="right">{completed.firstname}</TableCell>
              <TableCell align="right">{completed.prescription_id}</TableCell>
              <TableCell align="right">{completed.completed_at}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}
