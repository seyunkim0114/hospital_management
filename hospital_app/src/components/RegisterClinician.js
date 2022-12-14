// Code reference: https://codesandbox.io/s/signupregistration-form-reactmaterialui-fr71m?file=/src/index.js

import { useState } from 'react';

export default function RegisterClinician() {

  // States for registration
  const [name, setName] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  // States for checking the errors
  const [submitted, setSubmitted] = useState(false);
  const [error, setError] = useState(false);

  // Handling the name change
  const handleName = (e) => {
    setName(e.target.value);
    setSubmitted(false);
  };

  // Handling the email change
  const handleUsername = (e) => {
    setUsername(e.target.value);
    setSubmitted(false);
  };

  // Handling the password change
  const handlePassword = (e) => {
    setPassword(e.target.value);
    setSubmitted(false);
  };

  // Handling the form submission
  const handleSubmit = (e) => {
    e.preventDefault();
    if (name === '' || username === '' || password === '') {
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
      <h1>User {name} successfully registered!!</h1>
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
      <h1>User Registration</h1>
    </div>

    {/* Calling to the methods */}
    <div className="messages">
      {errorMessage()}
      {successMessage()}
    </div>

    <form>
      {/* Labels and inputs for form data */}
      <label className="label">Name</label>
      <input onChange={handleName} className="input"
      value={name} type="text" />

      <label className="label">username</label>
      <input onChange={handleUsername} className="input"
      value={username} type="email" />

      <label className="label">Password</label>
      <input onChange={handlePassword} className="input"
      value={password} type="password" />

      <button onClick={handleSubmit} className="btn" type="submit">
      Submit
      </button>
    </form>
    </div>
  );
}
