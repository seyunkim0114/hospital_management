import './App.css';
import Appbar from './components/Appbar';
import * as React from 'react';
import DenseTable from './components/DenseTable';

function App() {
  return (
    <div className="App">
      <Appbar/>
      Your Patients
      <DenseTable/>
    </div>
  );
}

export default App;
