import { useEffect } from 'react';
import './App.css';
import axios from 'axios'

function App() {
  var data = JSON.stringify({
    "collection": "Sub-Arrays",
    "database": "NEUTest",
    "dataSource": "NEUCluster",
    "projection": {
        "_id": 1
    }
});
var config = {
    method: 'post',
    url: 'https://data.mongodb-api.com/app/data-lwvft/endpoint/data/v1/action/findOne',
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Request-Headers': '*',
      'api-key': 'fLPItnpNimgOY7vAhs1j5Vg3OMDsY2F9qzxlucX5Ha3Q9PaqGKZdZKd7RWN3bf0E',
    },
    data: data
};
  const getData = async () => {
    await axios(config)
      .then(function (response) {
        console.log(JSON.stringify(response.data));
      })
      .catch(function (error) {
        console.log(error);
      });
  }

  useEffect(() => {
    getData()
  }, [])
  return (
    <div className="App">
      <header className="App-header">
        <p>
          Prueba Técnica NEU
        </p>
      </header>
    </div>
  );
}

export default App;
