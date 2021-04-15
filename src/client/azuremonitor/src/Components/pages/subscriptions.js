import React, { useState } from 'react';
import '../../App.css';
import Sidebar from '../Sidebar/Sidebar';
import Charts from '../../Charts'


export default function Subscriptions() {
  const [name, setName] = useState('')

  const updateName = (e) => {
    setName(e.target.innerText)
  }

  return(
    <>
      <Sidebar page='subscriptions' updateName={updateName} />
      {name && <Charts page='subscriptions' name={name} />}
    </>
    );
  }