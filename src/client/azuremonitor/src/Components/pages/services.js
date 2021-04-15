import React, { useState } from 'react';
import '../../App.css';
import Sidebar from '../Sidebar/Sidebar';
import Charts from '../../Charts'

export default function Services() {
  const [name, setName] = useState('')

  const updateName = (e) => {
    setName(e.target.innerText)
  }

  return(
    <>
      <Sidebar page='services' updateName={updateName}/>
      {name && <Charts page='services' name={name} />}
    </>
  );
}