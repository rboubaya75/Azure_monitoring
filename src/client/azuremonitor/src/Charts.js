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
  
function Charts(props) {
  const [costs, setCosts] = useState([]);

  useEffect(async () => {
    const f = async() => {
          const res = await axios(`https://brtazuremonitor.azurewebsites.net/api/cost/general/${props.page}/${props.name}`)
          const tmp = res.data.map(e => [e.name, parseInt(e.total)])
          setCosts([['Name', 'Total'], ...tmp]);
    };
    f()
  }, []);
  return (
    <div className="charts">
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