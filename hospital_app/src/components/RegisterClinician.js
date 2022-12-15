import { useState, useEffect } from 'react';



// function addRegisteredClinician(lastname, firstname, position){

//   console.log(clinician_id["clinician_id"])
//   fetch('http://localhost:5000/newclinicians', {
//     'method':'POST',
//     headers : {
//     'Content-Type':'application/json',
//     mode : 'cors',
//     crossDomain:true
//     },
//   body : JSON.stringify({
//     lastname: lastname,
//     firstname: firstname,
//     clinician_id: clinician_id["clinician_id"],
//     // username: username,
//     // password: password,
//     position: position
//   })
//   })
// }


export default function RegisterClinician() {

  // States for registration
  const [lastname, setLastname] = useState('');
  const [firstname, setFirstname] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [position, setPosition] = useState('');
  const [ids, setIds] = useState([]);

  // States for checking the errors
  const [submitted, setSubmitted] = useState(false);
  const [error, setError] = useState(false);


  // const addRegisteredClinician = () => {
  //   // console.log("addregistered", data.target)
  //   fetch('http://localhost:5000/newclinicians', {
  //     'method':'POST',
  //     headers : {
  //     'Content-Type':'application/json',
  //     // mode : 'cors',
  //     // crossDomain:true
  //     },
  //   body : JSON.stringify({
  //     lastname: lastname,
  //     firstname: firstname,
  //     // username: username,
  //     // password: password,
  //     position: position
  //   })
  //   })
  // }

  useEffect(()=>{
    fetch("http://127.0.0.1:5000/clinician_ids")
    .then(res=>res.json())
    .then((result)=>{
        setIds(result)
        console.log(result)
    })
  }, [])

  // const clinician_id = ids[Math.floor(Math.random()*ids.length)];


  // Handling the name change
  const handleLastname = (e) => {
    setLastname(e.target.value);
    setSubmitted(false);
  };

  const handleFirstname = (e) => {
    setFirstname(e.target.value);
    setSubmitted(false);
  };

  // Handling the position change
  const handlePosition = (e) => {
    setPosition(e.target.value);
    setSubmitted(false);
  }

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
    if (firstname === '' || lastname === '' || username === '' || password === '' || position === '') {
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
      <h1>User {firstname} {lastname} successfully registered!!</h1>
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
      <label className="label">Last Name</label>
      <input onChange={handleLastname} className="input"
      value={lastname} type="text" />

      <label className="label">First Name</label>
      <input onChange={handleFirstname} className="input"
      value={firstname} type="text" />

      <label className="label">Position</label>
      <input onChange={handlePosition} className="input"
      value={position} type="text" />

      <label className="label">Username</label>
      <input onChange={handleUsername} className="input"
      value={username} type="email" />

      <label className="label">Password</label>
      <input onChange={handlePassword} className="input"
      value={password} type="password" />

      <button onClick={(e)=>{
        handleSubmit(e); 
        // addRegisteredClinician(lastname, firstname, position);
      }} className="btn" type="submit">
      Submit
      </button>
    </form>
    </div>
  );
}
