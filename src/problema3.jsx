import React from 'react'
import './styles.css';
import { Link } from 'react-router-dom';

const Problema3 = () => {
  return (
    <div className="App">
      <h1>Grafica y Limpieza de Dato</h1>
      <img id="img1" src="./code_solutions/vuelos-por-dia.png" alt="Gráfica Vuelos por Día" width="304" height="228"></img>
      <img id="img1" src="./code_solutions/vuelos-por-dia-int.png" alt="Gráfica Vuelos por Día (int)" width="304" height="228"></img>
      <br></br>
      <br></br>
      <a href="./code_solutions/copa-limpiador.py" download="copa-limpiador.py">Descargar Código de Python</a>
      <br></br>
      <br></br>
      <a href="./code_solutions/INRANGE_sample.txt" download="INRANGE_sample.txt">Archivo Original</a>
      <br></br>
      <br></br>
      <a href="./code_solutions/INRANGE_CLEAN.csv" download="INRANGE_CLEAN.csv">Archivo Procesado</a>
      <br></br>
      <br></br>
      <Link to="/" style={{ color: '#FFF' }}>Regresar</Link>
    </div>
  )
}

export default Problema3;
