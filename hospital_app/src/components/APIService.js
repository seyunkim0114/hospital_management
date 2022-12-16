export default class APIService{
    // Insert an article
    static InsertPrescribedData(body){
        return fetch('http://localhost:5000/addlogs',{
            'method':'POST',
             headers : {
            'Content-Type':'application/json'
      },
      body:JSON.stringify(body)
    })
    .then(response => response.json())
    .catch(error => console.log(error))
    }

    static insertUserAuth(body){
        return fetch('http://localhost:5000/register',{
            'method':'POST',
            headers : {
            'Content-Type':'application/json'
      },
      body:JSON.stringify(body)
    })
    .then(response => response.json())
    .catch(error => console.log(error))
    }


    static getUserAuth(body){
        return fetch('http://localhost:5000/register',{
            'method':'GET',
            headers : {
            'Content-Type':'application/json'
      },
      body:JSON.stringify(body)
    })
    .then(response => response.json())
    .catch(error => console.log(error))
    }
}


