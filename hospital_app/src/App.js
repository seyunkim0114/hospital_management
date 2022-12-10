import './App.css';
import Appbar from './components/Appbar';
import * as React from 'react';
import { BrowserRouter as Router, Routes, 
  Route, Redirect,} from "react-router-dom";

import YourPatients from './components/YourPatients';
import UpcomingPrescriptions from './components/UpcomingPrescriptions'
import PatientsToPrescribe from './components/PatientsToPrescribe'

function App() {
  return (
    <>
      <Router>
        <Appbar/>
        <Routes>
          <Route path="/101" element={<PatientsToPrescribe/>} />
          {/* <Redirect to="/" /> */}
        </Routes>
      </Router>
    </>
    // <div className="App">
    //   <Appbar/>
    //   {/* Upcoming Prescriptions
    //   <UpcomingPrescriptions/> */}
    //   Your Patients
    //   <PatientsToPrescribe/>

    // </div>
  );
}

export default App;
