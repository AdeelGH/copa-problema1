import React, { useState } from 'react'
import './styles.css';
import { Link } from 'react-router-dom';

const Problema1 = () => {
  const [var1, setVar1] = useState(false);
  const [var2, setVar2] = useState(false);
  const [total, setTotal] = useState(false);

  function calculateSum() {
    let res = 0.0
    res = var1 + var2
    res = +res.toFixed(2);
    setTotal(res);
  }

  function calculateSubstraction() {
    let res = 0.0
    res = var1 - var2
    res = +res.toFixed(2);
    setTotal(res);
  }

  function calculateMultiplication() {
    let res = 0.0
    res = var1 * var2
    res = +res.toFixed(2);
    setTotal(res);
  }

  function calculateDivision() {
    let res = 0.0
    res = var1 / var2
    res = +res.toFixed(2);
    setTotal(res);
  }

  return (
    <div className="App">
      <h1>Operaciones con Dos Números</h1>
      <div className="number-inputs">
        <input
          type="number"
          value={var1}
          onChange={e => setVar1(+e.target.value)}
          onfocus=''
        />
        <input
          type="number"
          value={var2}
          onChange={e => setVar2(+e.target.value)}
          onfocus=''
        />
      </div>
      <div class="btn-group">
        <button onClick={calculateSum}>Suma</button>
        <button onClick={calculateSubstraction}>Resta</button>
        <button onClick={calculateMultiplication}>Multiplicación</button>
        <button onClick={calculateDivision}>División</button>
      </div>
      <h2>{total}</h2>
      <Link to="/" style={{ color: '#FFF' }}>Regresar</Link>
    </div>
  )
}

export default Problema1;
