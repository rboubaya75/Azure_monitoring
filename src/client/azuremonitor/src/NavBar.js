import './NavBar.css';
import axios from "axios";
import { useEffect, useState } from 'react';

function NavBar() {
    const [couts, setCouts] = useState([]);

    useEffect(() => {
        const f = async() => {
            const res = await axios("https://brtazuremonitor.azurewebsites.net/api/cost/general/subscriptions")
            setCouts(res.data);
            console.log(res.data)
        };
        f()
    }, []);
    return (
        <div>

        </div>
        // <div class='wrapper'>
        //     <div class='navbar'>
        //         <button>Home</button>
        //         <button>Subscriptions</button>
        //         <button>Services</button>
        //     </div>
        // </div>

    )
}

export default NavBar;