import React from 'react'
import './styles.css';
import { Link } from 'react-router-dom';

const Problema2 = () => {
  return (
    <div className="App">
      <h1>¿Qué es el DOM?</h1>
      <p align = "justify">
      El DOM (Document Object Model), es una representación creada para interactuar con páginas web de una manera más eficiente, que organiza estas en partes simples ordenadas jerárquicamente llamadas objetos. Esto permite que programadores puedan cambiar el contenido, el estilo y aspectos de la página web sin modificar directamente el código HTML, por medio de los objetos y nodos que forman parte del modelo.
      </p>
      <br></br>
      <Link to="/" style={{ color: '#FFF' }}>Regresar</Link>
    </div>
  )
}

export default Problema2;
