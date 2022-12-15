import { useState } from 'react';

import authenticate from ''

export default function WriteAccess() {

  // States for registration
  const [medicineName, setMedicineName] = useState('');
  const [medInterval, setMedInterval] = useState('');
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');
  const [specialNote, setSpecialNote] = useState('');

  // States for checking the errors
  const [submitted, setSubmitted] = useState(false);
  const [error, setError] = useState(false);

  // Handling the password change
  const handleMedicineName = (e) => {
    setMedicineName(e.target.value);
    setSubmitted(false);
  }

  const handleMedInterval = (e) => {
    setMedInterval(e.target.value);
    setSubmitted(false);
  };

  const handleStartDate = (e) => {
    setStartDate(e.target.value);
    setSubmitted(false);
  };

  const handleEndDate = (e) => {
    setEndDate(e.target.value);
    setSubmitted(false);
  };

  const handleSpecialNote = (e) => {
    setSpecialNote(e.target.value);
    setSubmitted(false);
  };

  // Handling the form submission
  const handleSubmit = (e) => {
    e.preventDefault();
    if (medicineName === '' || medInterval === '' || startDate === '' || endDate === '') {
    setError(true);
    } else {
    setSubmitted(true);
    setError(false);
    }
  };

  // Showing success message
  const successMessage = () => {
    return (
    <div
      className="success"
      style={{
      display: submitted ? '' : 'none',
      }}>
      <h1>Successfully Prescribed!</h1>
    </div>
    );
  };

  // Showing error message if error is true
  const errorMessage = () => {
    return (
    <div
      className="error"
      style={{
      display: error ? '' : 'none',
      }}>
      <h1>Please enter all the fields</h1>
    </div>
    );
  };

  return (
    <div className="form">
    <div>
      <h1>Prescribe</h1>
    </div>

    {/* Calling to the methods */}
    <div className="messages">
      {errorMessage()}
      {successMessage()}
    </div>

    <form>
      {/* Labels and inputs for form data */}

      <label className="label">Medicine Name</label>
      <input onChange={handleMedicineName} className="input"
      value={medicineName} type="Submit" />

      <label className="label">Medicine Interval</label>
      <input onChange={handleMedInterval} className="input"
      value={medInterval} type="Submit" />

      <label className="label">Start Date</label>
      <input onChange={handleStartDate} className="input"
      value={startDate} type="Submit" />

      <label className="label">End Date</label>
      <input onChange={handleEndDate} className="input"
      value={endDate} type="Submit" />

      <label className="label">Special Note</label>
      <input onChange={handleSpecialNote} className="input"
      value={specialNote} type="Submit" />


      <button onClick={handleSubmit} className="btn" type="submit">
      Submit
      </button>
    </form>
    </div>
  );
}