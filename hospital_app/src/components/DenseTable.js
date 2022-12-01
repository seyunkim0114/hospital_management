// import * as React from 'react';
import React, { useEffect, useState } from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

function createData(patient_id, firstname, lastname, DOB, admitted) {
  return { patient_id, firstname, lastname, DOB, admitted };
}



// const rows = [
//   createData('Frozen yoghurt', 159, 6.0, 24, 4.0),
//   createData('Ice cream sandwich', 237, 9.0, 37, 4.3),
//   createData('Eclair', 262, 16.0, 24, 6.0),
//   createData('Cupcake', 305, 3.7, 67, 4.3),
//   createData('Gingerbread', 356, 16.0, 49, 3.9),
// ];

export default function DenseTable() {
  // const[patients, setPatients] = useState([]);

  // useEffect(()=>{
  //   fetch("http://localhost:8080/patient/patient_id/allpatients")
  //   .then(res=>res.json())
  //   .then((result)=>{
  //     setPatients(result);
  //   }
  // )
  // }, [])

  const[patients, setPatients] = useState([]);
  const rows= [];

  useEffect(()=>{
    fetch("http://localhost:8080/patient/patient_id/allpatients")
    .then(res=>res.json())
    .then((result)=>{
      setPatients(result);
    }
  )
  }, [])

  // console.log(patients);
  patients.map(patient=>(
    rows.push(createData(patient.patient_id, patient.firstname, patient.lastname, patient.dob, patient.admitted))
  ))

  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} size="small" aria-label="a dense table">
        <TableHead>
          <TableRow>
            <TableCell>Patient_Id</TableCell>
            <TableCell align="right">Firstname</TableCell>
            <TableCell align="right">Lastname</TableCell>
            <TableCell align="right">Date of Birth</TableCell>
            <TableCell align="right">Admitted Day</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow
              key={row.patient_id}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell component="th" scope="row">
                {row.patient_id}
              </TableCell>
              <TableCell align="right">{row.firstname}</TableCell>
              <TableCell align="right">{row.lastname}</TableCell>
              <TableCell align="right">{row.DOB}</TableCell>
              <TableCell align="right">{row.admitted}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}