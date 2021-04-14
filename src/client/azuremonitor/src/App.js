import React from 'react';
import Navbar from './Components/navbar/navbar';
import './App.css';
import Home from './Components/pages/home';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Services from './Components/pages/services';
import Subscriptions from './Components/pages/subscriptions';
//import thumb from "./azure.png";


function App() {
  return (
    <>

      <Router>
      <div className="App">
      <Navbar />  </div>
         
        <Switch>
          <Route path='/' exact component={Home} />
          <Route path='/subscriptions' component={Subscriptions} />
          <Route path='/services' component={Services} />
          
        </Switch>
        
      </Router>
       
    </>
  );
}

export default App;




