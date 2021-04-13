import React from 'react';
import '../../App.css';
import {useState} from 'react';
import Charts from '../../Charts';





export default function Home() {
    const [click, setClick] = useState(true)
    
    return (
        <div className="Container">
            <p className="title"> Welcome to the monitoring App</p>
            
        </div>
    )
}