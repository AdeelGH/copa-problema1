import React from 'react'
import './styles.css';
import { Link } from 'react-router-dom';

const Problema4 = () => {
  return (
    <div className="App">
      <h1>SQL</h1>
      <a href="./code_solutions/copa-sql.txt" download="copasql.txt">Descargar Queries SQL</a>
      <br></br>
      <br></br>
      <Link to="/" style={{ color: '#FFF' }}>Regresar</Link>
    </div>
  )
}

export default Problema4;
