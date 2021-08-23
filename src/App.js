/*App.js*/
import React, { Component } from "react";
import './styles.css';
//Paginas
import MainPage from "./index.jsx";
import Problema1 from "./problema1.jsx";
import Problema2 from "./problema2";
import Problema3 from "./problema3";
import Problema4 from "./problema4";
import Problema5 from "./problema5";
import {
  BrowserRouter as Router,
  Route,
  Switch
} from "react-router-dom";

class App extends Component {
  render() {
    return (
      <Router>
            <Switch>
                <Route exact path='/' component={MainPage} />
                <Route exact path='/problema1' component={Problema1} />
                <Route exact path='/problema2' component={Problema2} />
                <Route exact path='/problema3' component={Problema3} />
                <Route exact path='/problema4' component={Problema4} />
                <Route exact path='/problema5' component={Problema5} />
            </Switch>
    </Router>
    );
  }
}

export default App;