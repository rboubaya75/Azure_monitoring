import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import React from 'react';

import './App.css';
import Charts from './Charts'
import Home from './Components/pages/home';
import Navbar from './Components/navbar/navbar';
import Services from './Components/pages/services';
import Subscriptions from './Components/pages/subscriptions';
//import thumb from "./azure.png";

function App() {
  return (
    <>
      <Router>
        <div className="App">
          <Navbar />
        </div>
        <div className='container'>
          <Switch>
            <Route path='/' exact component={Home} />
            <Route path='/subscriptions' component={Subscriptions} />
            <Route path='/services' component={Services} />
          </Switch>
        </div>
      </Router>
    </>
  );
}

export default App;