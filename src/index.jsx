import React from 'react'
import './styles.css';
import { Link } from 'react-router-dom';

const MainPage = () => {
  return (
    <div className="App">
      <h1>Inicio</h1>
      <ul>
        <li><Link to="/problema1">Problema1</Link></li>
        <br></br>
        <li><Link to="/problema2">Problema2</Link></li>
        <br></br>
        <li><Link to="/problema3">Problema3</Link></li>
        <br></br>
        <li><Link to="/problema4">Problema4</Link></li>
        <br></br>
        <li><Link to="/problema5">Problema5</Link></li>
      </ul>
    </div>
  )
}

export default MainPage;
