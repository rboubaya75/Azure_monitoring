import axios from "axios";
import { useEffect, useState } from 'react';
import Chart from "react-google-charts";

const pieOptions = {
    title: "",
    pieHole: 0,
    slices: [
      {
        color: "#2BB673"
      },
      {
        color: "#d91e48"
      },
      {
        color: "#007fad"
      },
      {
        color: "#e9a227"
      }
    ],
    legend: {
      alignment: "center",
      textStyle: {
        color: "233238",
        fontSize: 14
      }
    },
    tooltip: {
      showColorCode: true
    },
    chartArea: {
      left: 0,
      top: 0,
      width: "50%",
      height: "80%"
    },
    fontName: "Roboto"
};
  
function Charts() {
    const [costs, setCosts] = useState([]);

    useEffect(async () => {
        const f = async() => {
            const res = await axios("https://brtazuremonitor.azurewebsites.net/api/cost/general/services")
            const tmp = [...res.data].map(e => [e.name, parseInt(e.total)])
            tmp.splice(0, 0, ['Name', 'Total'])
            setCosts(tmp);
        };
        f()
      }, []);
    return (
        <div className="App">
            <Chart
            chartType="PieChart"
            data={costs}
            options={pieOptions}
            graph_id="PieChart"
            width={"100%"}
            height={"400px"}
            legend_toggle
            />
        </div>
      );
}

export default Charts;