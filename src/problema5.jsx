import React from 'react'
import './styles.css';
import { Link } from 'react-router-dom';

const Problema5 = () => {
  return (
    <div className="App">
      <h1>Travelling Salesperson</h1>
      <a href="./code_solutions/copa-travelling-salesperson.py" download="copa-travelling-salesperson.py">Descargar Código de Python</a>
      <br></br>
      <br></br>
      <Link to="/" style={{ color: '#FFF' }}>Regresar</Link>
    </div>
  )
}

export default Problema5;
