import './App.css';
import Appbar from './components/Appbar';
import * as React from 'react';
import { BrowserRouter as Router, Routes, 
  Route, Redirect,} from "react-router-dom";

import YourPatients from './components/YourPatients';
import UpcomingPrescriptions from './components/UpcomingPrescriptions'
import PatientsToPrescribe from './components/PatientsToPrescribe'
import RegisterClinician from './components/RegisterClinician'
import LogIn from './components/LogIn';
function App() {
  return (
    <>
      <Router>
        <Appbar/>
        <Routes>
          <Route path="/41" element={<PatientsToPrescribe/>} />
          <Route path="/" element={<LogIn/>} />
          {/* <Redirect to="/" /> */}
        </Routes>
      </Router>
    </>

  );
}

export default App;
